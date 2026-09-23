// Edge Function `delete-account` — người dùng tự xoá tài khoản: xoá auth.users → mọi bảng cascade.
// Báo lỗi nội dung giữ lại nhưng bỏ liên kết (user_id = null). Lưu vết bằng mã băm id (không giữ dữ liệu cá nhân).
import { adminClient, corsHeaders, getUser, json } from "../_shared/common.ts";

async function sha256(s: string): Promise<string> {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return Array.from(new Uint8Array(buf)).map((x) => x.toString(16).padStart(2, "0")).join("");
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: corsHeaders(req) });
  if (req.method !== "POST") return json(req, { error: "method" }, 405);
  const user = await getUser(req);
  if (!user) return json(req, { error: "not_authenticated" }, 401);
  let body: { confirm?: string } = {};
  try { body = await req.json(); } catch { /* bỏ qua */ }
  if (body.confirm !== "DELETE") return json(req, { error: "confirm_required" }, 400);

  const db = adminClient();
  const { error } = await db.auth.admin.deleteUser(user.id);
  if (error) return json(req, { error: "delete_failed" }, 500);
  await db.from("deletion_log").insert({ user_hash: await sha256(user.id), source: "app" });
  return json(req, { ok: true });
});
