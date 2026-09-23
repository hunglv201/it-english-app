// Edge Function `send-reminders` — chạy 15 phút/lần (GitHub Action backend-reminders.yml hoặc pg_cron + pg_net).
// Không dùng JWT người dùng: xác thực bằng header `x-cron-secret` = secret CRON_SECRET.
// claim_reminders() (bọc due_reminders) quyết định ai cần nhắc (≤ 1 push/ngày/người, giờ học thích ứng, kéo người vắng ngày 1–4, lần cuối ngày 7,
// tổng kết tuần tối Chủ nhật, lời nhắc từ bạn học). Secrets: VAPID_PUBLIC_KEY, VAPID_PRIVATE_KEY, VAPID_SUBJECT (mailto:…).
import webpush from "npm:web-push@3.6.7";
import { adminClient } from "../_shared/common.ts";

type Due = { user_id: string; kind: string; days_away: number | null; streak_n: number; freeze_n: number; track: string;
  week_days: number | null; last_week_days: number | null; from_nick: string | null };

const TRACK_VI: Record<string, string> = { office: "công sở", it: "IT", hotel: "khách sạn", sales: "bán hàng", factory: "nhà máy",
  logistics: "logistics", finance: "tài chính", marketing: "marketing", health: "y tế", construction: "xây dựng", aviation: "hàng không", custom: "nghề của bạn" };

/** Lời nhắc nhẹ nhàng, không doạ, không gây tội lỗi (docs/TINH-NANG-MOI-2026-09-23.md §2). */
export function message(d: Due): { title: string; body: string; url: string; tag: string } {
  const nganh = TRACK_VI[d.track] || "nghề của bạn";
  const base = { url: "./", tag: "noinghe-" + d.kind };
  switch (d.kind) {
    case "nudge":
      return { ...base, title: "👋 " + (d.from_nick || "Bạn học") + " nhắc bạn", body: "Cùng luyện tiếng Anh 5 phút hôm nay nhé — giữ chuỗi chung của hai bạn." };
    case "daily":
      return d.streak_n >= 2
        ? { ...base, title: "🔥 Chuỗi " + d.streak_n + " ngày đang chờ", body: "5 phút tiếng Anh " + nganh + " là giữ được chuỗi hôm nay." }
        : { ...base, title: "🎙️ 5 phút luyện nói hôm nay?", body: "Một bài ngắn tiếng Anh " + nganh + " đã sẵn sàng." };
    case "winback2":
      return d.freeze_n > 0
        ? { ...base, title: "❄️ Chuỗi của bạn vẫn còn", body: "Đóng băng đã giữ chuỗi cho bạn — học 1 việc 2 phút là nối tiếp." }
        : { ...base, title: "Quay lại 2 phút thôi", body: "Một bài nghe ngắn tiếng Anh " + nganh + " đang chờ bạn 🎧" };
    case "winback3":
      return { ...base, title: "✅ Vài từ đang chờ ôn", body: "Ôn nhanh 2 phút để không quên từ đã học." };
    case "winback4":
      return { ...base, title: "🎧 Bài nghe 1 phút", body: "Tình huống " + nganh + " quen thuộc — nghe và nhắc lại một câu thôi." };
    case "final7":
      return { ...base, title: "Nói Nghề vẫn giữ tiến độ của bạn 👋", body: "Khi nào rảnh thì ghé lại nhé. Đây là lời nhắc cuối — app sẽ không làm phiền nữa." };
    case "weekly": {
      const a = d.week_days ?? 0, b = d.last_week_days ?? 0;
      const goal = Math.min(7, Math.max(a, 3) + (a >= b ? 1 : 0));
      return { ...base, title: "📊 Tuần này bạn học " + a + " ngày", body: (b ? "Tuần trước " + b + " ngày. " : "") + "Tuần tới thử " + goal + " ngày nhé!" };
    }
    default:
      return { ...base, title: "Nói Nghề", body: "Luyện tiếng Anh 5 phút hôm nay nhé." };
  }
}

Deno.serve(async (req) => {
  const secret = Deno.env.get("CRON_SECRET");
  if (!secret || req.headers.get("x-cron-secret") !== secret) return new Response("forbidden", { status: 403 });
  const pub = Deno.env.get("VAPID_PUBLIC_KEY"), priv = Deno.env.get("VAPID_PRIVATE_KEY");
  if (!pub || !priv) return new Response("vapid not configured", { status: 500 });
  webpush.setVapidDetails(Deno.env.get("VAPID_SUBJECT") || "mailto:admin@example.com", pub, priv);

  const db = adminClient();
  // nhận việc nguyên tử (đánh dấu "đã nhắc hôm nay" trước khi gửi) → 2 lượt chạy chồng nhau không gửi trùng
  const { data: due, error } = await db.rpc("claim_reminders", {});
  if (error) return new Response("claim_reminders failed", { status: 500 });
  let sent = 0, gone = 0, failed = 0;
  const one = async (d: Due) => {
    const { data: subs, error: e1 } = await db.rpc("push_targets", { p_user: d.user_id });
    if (e1) { await db.rpc("release_reminder", { p_user: d.user_id }); failed++; return; }
    const payload = JSON.stringify(message(d));
    let any = false;
    for (const s of (subs || []) as { id: number; endpoint: string; p256dh: string; auth: string }[]) {
      try {
        await webpush.sendNotification({ endpoint: s.endpoint, keys: { p256dh: s.p256dh, auth: s.auth } }, payload,
          { TTL: 2 * 3600, urgency: "normal", timeout: 10000 });
        await db.rpc("push_result", { p_id: s.id, p_ok: true, p_gone: false });
        any = true; sent++;
      } catch (e) {
        const code = (e as { statusCode?: number }).statusCode || 0;
        const isGone = code === 404 || code === 410;
        await db.rpc("push_result", { p_id: s.id, p_ok: false, p_gone: isGone });
        if (isGone) gone++; else failed++;
      }
    }
    if (!any) await db.rpc("release_reminder", { p_user: d.user_id }); // không gửi được máy nào → lượt sau thử lại
  };
  const list = (due || []) as Due[];
  for (let i = 0; i < list.length; i += 10) await Promise.all(list.slice(i, i + 10).map(one)); // song song từng nhóm 10 người
  return new Response(JSON.stringify({ due: (due || []).length, sent, gone, failed }), { headers: { "content-type": "application/json" } });
});
