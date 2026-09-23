// Dùng chung cho Edge Functions của Nói Nghề.
import { createClient, type SupabaseClient, type User } from "npm:@supabase/supabase-js@2";

const DEFAULT_ORIGINS = "https://hunglv201.github.io,http://localhost:8765,http://127.0.0.1:8765";

export function corsHeaders(req: Request): Record<string, string> {
  const allowed = (Deno.env.get("ALLOWED_ORIGINS") || DEFAULT_ORIGINS).split(",").map((s) => s.trim());
  const origin = req.headers.get("origin") || "";
  return {
    "Access-Control-Allow-Origin": allowed.includes(origin) ? origin : allowed[0],
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Vary": "Origin",
  };
}

export function json(req: Request, body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...corsHeaders(req), "content-type": "application/json; charset=utf-8" },
  });
}

export function adminClient(): SupabaseClient {
  return createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, {
    auth: { persistSession: false, autoRefreshToken: false },
  });
}

/** Lấy user từ JWT trong header Authorization; null nếu thiếu/không hợp lệ. */
export async function getUser(req: Request): Promise<User | null> {
  const auth = req.headers.get("authorization") || "";
  const token = auth.replace(/^Bearer\s+/i, "");
  if (!token) return null;
  const { data, error } = await adminClient().auth.getUser(token);
  if (error || !data?.user) return null;
  return data.user;
}
