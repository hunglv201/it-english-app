// Edge Function `ai` — gọi AI bằng key chung (Gemini, hoặc Claude) cho người chưa có key riêng.
// Kiểm tra JWT → giữ 1 lượt trong hạn mức (ai_take) → gọi nhà cung cấp → ghi token (ai_record).
// Không log nội dung prompt/trả lời. Secrets: GEMINI_API_KEY (hoặc ANTHROPIC_API_KEY + AI_PROVIDER=claude).
import { adminClient, corsHeaders, getUser, json } from "../_shared/common.ts";

type Turn = { role: "user" | "assistant"; content: string };
type Body = { system?: string; turns?: Turn[]; image?: { mime: string; data: string }; maxTokens?: number };

const MAX_CHARS = 24000;
const MAX_IMAGE_B64 = 2_100_000; // ~1,5 MB ảnh
const IMAGE_TYPES = ["image/jpeg", "image/png", "image/webp"];

function validate(b: Body): string | null {
  if (!b || typeof b !== "object" || !Array.isArray(b.turns) || !b.turns.length || b.turns.length > 40) return "bad_turns";
  if (b.system !== undefined && b.system !== null && typeof b.system !== "string") return "bad_system";
  if (b.maxTokens !== undefined && b.maxTokens !== null && typeof b.maxTokens !== "number") return "bad_max_tokens";
  if (b.turns[b.turns.length - 1]?.role !== "user") return "last_turn_must_be_user";
  let n = (b.system || "").length;
  for (const t of b.turns) {
    if (!t || typeof t.content !== "string" || (t.role !== "user" && t.role !== "assistant")) return "bad_turns";
    n += t.content.length;
  }
  if (n > MAX_CHARS) return "too_long";
  if (b.image) {
    if (typeof b.image !== "object" || !IMAGE_TYPES.includes(b.image.mime) || typeof b.image.data !== "string") return "bad_image";
    if (b.image.data.length > MAX_IMAGE_B64) return "image_too_large";
  }
  return null;
}

/** Lỗi phía nhà cung cấp: refund = true khi không phải lỗi của request (mạng, 5xx, 429). */
class UpstreamError extends Error {
  constructor(msg: string, public refund: boolean, public tin = 0, public tout = 0) { super(msg); }
}
function upstream(status: number): UpstreamError {
  return new UpstreamError("upstream_" + status, status >= 500 || status === 429);
}

async function callGemini(b: Body, maxTokens: number) {
  const key = Deno.env.get("GEMINI_API_KEY");
  if (!key) throw new UpstreamError("no_key", true);
  const model = Deno.env.get("GEMINI_MODEL") || "gemini-2.5-flash";
  const contents = b.turns!.map((t) => ({ role: t.role === "assistant" ? "model" : "user", parts: [{ text: t.content }] as unknown[] }));
  if (b.image) contents[contents.length - 1].parts.unshift({ inline_data: { mime_type: b.image.mime, data: b.image.data } });
  const gc: Record<string, unknown> = { temperature: 0.7, maxOutputTokens: maxTokens };
  if (/2\.5|3\.\d/.test(model) && !/lite/.test(model)) gc.thinkingConfig = { thinkingBudget: 0 };
  const body: Record<string, unknown> = { contents, generationConfig: gc };
  if (b.system) body.systemInstruction = { parts: [{ text: b.system }] };
  const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(model)}:generateContent`, {
    method: "POST",
    headers: { "content-type": "application/json", "x-goog-api-key": key },
    body: JSON.stringify(body),
  });
  if (!r.ok) throw upstream(r.status);
  const j = await r.json();
  const text = (j.candidates?.[0]?.content?.parts || []).map((p: { text?: string }) => p.text || "").join("").trim();
  const tin = j.usageMetadata?.promptTokenCount || 0, tout = j.usageMetadata?.candidatesTokenCount || 0;
  if (!text) throw new UpstreamError("empty", false, tin, tout); // đã tốn token → không trả lại lượt
  return { text, tin, tout };
}

async function callClaude(b: Body, maxTokens: number) {
  const key = Deno.env.get("ANTHROPIC_API_KEY");
  if (!key) throw new UpstreamError("no_key", true);
  const model = Deno.env.get("CLAUDE_MODEL") || "claude-haiku-4-5";
  const messages = b.turns!.map((t) => ({ role: t.role, content: t.content as unknown }));
  if (b.image) {
    const last = messages[messages.length - 1];
    last.content = [{ type: "image", source: { type: "base64", media_type: b.image.mime, data: b.image.data } }, { type: "text", text: last.content }];
  }
  const body: Record<string, unknown> = { model, max_tokens: maxTokens, messages };
  if (b.system) body.system = b.system;
  const r = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "content-type": "application/json", "x-api-key": key, "anthropic-version": "2023-06-01" },
    body: JSON.stringify(body),
  });
  if (!r.ok) throw upstream(r.status);
  const j = await r.json();
  const text = (j.content || []).map((p: { text?: string }) => p.text || "").join("").trim();
  const tin = j.usage?.input_tokens || 0, tout = j.usage?.output_tokens || 0;
  if (!text) throw new UpstreamError("empty", false, tin, tout);
  return { text, tin, tout };
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: corsHeaders(req) });
  if (req.method !== "POST") return json(req, { error: "method" }, 405);
  const user = await getUser(req);
  if (!user) return json(req, { error: "not_authenticated" }, 401);

  let b: Body;
  try { b = await req.json(); } catch { return json(req, { error: "bad_json" }, 400); }
  const bad = validate(b);
  if (bad) return json(req, { error: bad }, 400);

  const db = adminClient();
  const { data: take, error: takeErr } = await db.rpc("ai_take", { p_uid: user.id });
  if (takeErr) return json(req, { error: "quota_check_failed" }, 500);
  if (!take?.ok) return json(req, take, 429);

  const maxTokens = Math.min(Math.max(Number(b.maxTokens) || 1024, 64), 4096);
  try {
    const provider = Deno.env.get("AI_PROVIDER") || "gemini";
    const out = provider === "claude" ? await callClaude(b, maxTokens) : await callGemini(b, maxTokens);
    await db.rpc("ai_record", { p_uid: user.id, p_in: out.tin, p_out: out.tout, p_refund: false });
    return json(req, { text: out.text, remaining: take.remaining, limit: take.limit });
  } catch (e) {
    // chỉ trả lại lượt khi lỗi mạng / nhà cung cấp quá tải (tối đa 5 lần/ngày, xem ai_record); luôn ghi token đã tốn
    const u = e instanceof UpstreamError ? e : new UpstreamError(String((e as Error)?.message || e), true);
    await db.rpc("ai_record", { p_uid: user.id, p_in: u.tin, p_out: u.tout, p_refund: u.refund });
    return json(req, { error: "ai_failed", detail: u.message.slice(0, 60) }, 502);
  }
});
