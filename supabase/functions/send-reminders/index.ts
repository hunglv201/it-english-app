// Edge Function `send-reminders` — chạy 15 phút/lần (GitHub Action backend-reminders.yml hoặc pg_cron + pg_net).
// Không dùng JWT người dùng: xác thực bằng header `x-cron-secret` = secret CRON_SECRET.
// claim_reminders() (bọc due_reminders) quyết định ai cần nhắc (≤ 1 push/ngày/người, giờ học thích ứng, kéo người vắng ngày 1–4, lần cuối ngày 7,
// tổng kết tuần tối Chủ nhật, lời nhắc từ bạn học). Secrets: VAPID_PUBLIC_KEY, VAPID_PRIVATE_KEY, VAPID_SUBJECT (mailto:…).
// v4.2: tổng kết tuần qua EMAIL (người dùng tự bật, chỉ tài khoản Google) — claim_weekly_emails(); gửi qua Resend.
// Secrets: RESEND_API_KEY, EMAIL_FROM ("Nói Nghề <hello@ten-mien-cua-ban>", tên miền đã xác minh ở Resend), APP_URL (mặc định GitHub Pages).
// Thiếu VAPID → bỏ phần push; thiếu RESEND → bỏ phần email.
import webpush from "npm:web-push@3.6.7";
import { adminClient } from "../_shared/common.ts";

type Due = { user_id: string; kind: string; days_away: number | null; streak_n: number; freeze_n: number; track: string;
  week_days: number | null; last_week_days: number | null; from_nick: string | null };

const TRACK_VI: Record<string, string> = { office: "công sở", it: "IT", hotel: "khách sạn", sales: "bán hàng", factory: "nhà máy",
  logistics: "logistics", finance: "tài chính", marketing: "marketing", health: "y tế", construction: "xây dựng", aviation: "hàng không", education: "giáo dục", legal: "pháp lý", custom: "nghề của bạn" };

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

type WeeklyMail = { user_id: string; email: string; nick: string | null; track: string; week_days: number; last_week_days: number;
  streak_n: number; tasks_week: number; unsub_token: string };

const escHtml = (x: string) => x.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c] as string));

/** Email tổng kết tuần: ngắn, ấm áp, không doạ; có link huỷ nhận 1 chạm. */
export function weeklyEmail(m: WeeklyMail, appUrl: string): { subject: string; html: string; text: string; unsub: string } {
  const a = m.week_days || 0, b = m.last_week_days || 0;
  const goal = Math.min(7, Math.max(a, 3) + (a >= b ? 1 : 0));
  const nganh = TRACK_VI[m.track] || "nghề của bạn";
  const base = appUrl.replace(/\/+$/, "") + "/";
  const unsub = base + "?unsub=" + encodeURIComponent(m.unsub_token);
  const open = base + "?from=weekly";
  const hi = m.nick ? "Chào " + m.nick + "," : "Chào bạn,";
  const trend = !b ? "" : a > b ? "Nhiều hơn tuần trước " + (a - b) + " ngày 👏" : a === b ? "Đều như tuần trước 👍" : "Tuần trước " + b + " ngày — tuần tới lấy lại nhịp nhé.";
  const lines = [
    "Tuần này bạn học tiếng Anh " + nganh + " " + a + " ngày" + (m.tasks_week ? ", xong " + m.tasks_week + " việc" : "") + ".",
    trend,
    m.streak_n >= 2 ? "Chuỗi hiện tại: " + m.streak_n + " ngày 🔥" : "",
    "Mục tiêu tuần tới: " + goal + " ngày — mỗi ngày 5 phút là đủ.",
  ].filter(Boolean);
  const subject = "📊 Tuần này bạn học " + a + " ngày · Nói Nghề";
  const text = hi + "\n\n" + lines.join("\n") + "\n\nMở app: " + open + "\n\nKhông muốn nhận email này nữa: " + unsub;
  const html = '<!doctype html><html lang="vi"><body style="margin:0;background:#f4f6fb;font-family:Arial,Helvetica,sans-serif;color:#1b2233">'
    + '<div style="max-width:520px;margin:0 auto;padding:24px 16px"><div style="background:#fff;border-radius:16px;padding:24px 22px">'
    + '<div style="font-size:13px;color:#4f7bff;font-weight:700;letter-spacing:.04em">NÓI NGHỀ · TỔNG KẾT TUẦN</div>'
    + '<p style="font-size:16px;margin:14px 0 6px">' + escHtml(hi) + "</p>"
    + '<div style="font-size:40px;font-weight:800;margin:6px 0">' + a + '<span style="font-size:18px;font-weight:600;color:#667"> / 7 ngày</span></div>'
    + lines.map((l) => '<p style="font-size:15px;line-height:1.5;margin:6px 0">' + escHtml(l) + "</p>").join("")
    + '<p style="margin:20px 0 4px"><a href="' + escHtml(open) + '" style="display:inline-block;background:#1f4fff;color:#fff;text-decoration:none;font-weight:700;padding:12px 20px;border-radius:12px">Học 5 phút ngay</a></p>'
    + '</div><p style="font-size:12px;color:#889;line-height:1.5;margin:14px 6px">Bạn nhận email này vì đã bật "Tổng kết tuần qua email" trong app. '
    + '<a href="' + escHtml(unsub) + '" style="color:#667">Huỷ nhận</a> (1 chạm, không cần đăng nhập).</p></div></body></html>';
  return { subject, html, text, unsub };
}

/** Gửi qua Resend /emails/batch (≤ 100 thư/lần, hợp giới hạn ~2 request/giây). Lỗi tạm (429/5xx/mạng) → release để lượt sau gửi lại;
 *  lỗi 4xx khác (địa chỉ sai, tên miền chưa xác minh) → không thử lại tuần này. Idempotency-Key theo lô tránh gửi trùng khi timeout. */
async function sendWeeklyEmails(db: ReturnType<typeof adminClient>, deadline: number) {
  const key = Deno.env.get("RESEND_API_KEY"), from = Deno.env.get("EMAIL_FROM");
  if (!key || !from) return null;
  const appUrl = Deno.env.get("APP_URL") || "https://hunglv201.github.io/it-english-app/";
  const { data, error } = await db.rpc("claim_weekly_emails", {});
  if (error) return { error: "claim_weekly_emails failed" };
  const list = (data || []) as WeeklyMail[];
  let sent = 0, failed = 0, retry = 0;
  const release = async (ms: WeeklyMail[]) => { for (const m of ms) await db.rpc("release_weekly_email", { p_user: m.user_id }); };
  for (let i = 0; i < list.length; i += 100) {
    const chunk = list.slice(i, i + 100);
    if (Date.now() > deadline) { await release(list.slice(i)); retry += list.length - i; break; }   // hết thời gian → lượt sau
    const week = new Date().toISOString().slice(0, 10);
    const body = chunk.map((m) => { const e = weeklyEmail(m, appUrl);
      return { from, to: [m.email], subject: e.subject, html: e.html, text: e.text, headers: { "List-Unsubscribe": "<" + e.unsub + ">" } }; });
    let status = 0;
    try {
      const r = await fetch("https://api.resend.com/emails/batch", {
        method: "POST",
        headers: { authorization: "Bearer " + key, "content-type": "application/json",
          "Idempotency-Key": "weekly-" + week + "-" + chunk.map((m) => m.user_id.slice(0, 8)).join("").slice(0, 200) },
        body: JSON.stringify(body), signal: AbortSignal.timeout(15000),
      });
      status = r.status;
    } catch (_e) { status = -1; }
    if (status >= 200 && status < 300) sent += chunk.length;
    else if (status === -1 || status === 429 || status >= 500) { retry += chunk.length; await release(chunk); }
    else failed += chunk.length;
    if (i + 100 < list.length) await new Promise((r) => setTimeout(r, 600));
  }
  return { due: list.length, sent, failed, retry };
}

async function sendPushes(db: ReturnType<typeof adminClient>): Promise<Record<string, unknown>> {
  // nhận việc nguyên tử (đánh dấu "đã nhắc hôm nay" trước khi gửi) → 2 lượt chạy chồng nhau không gửi trùng
  const { data: due, error } = await db.rpc("claim_reminders", {});
  if (error) return { error: "claim_reminders failed" };
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
  return { due: (due || []).length, sent, gone, failed };
}

Deno.serve(async (req) => {
  const secret = Deno.env.get("CRON_SECRET");
  if (!secret || req.headers.get("x-cron-secret") !== secret) return new Response("forbidden", { status: 403 });
  const t0 = Date.now();
  const db = adminClient();
  const pub = Deno.env.get("VAPID_PUBLIC_KEY"), priv = Deno.env.get("VAPID_PRIVATE_KEY");
  let push: Record<string, unknown> | string = "not configured";
  if (pub && priv) {
    webpush.setVapidDetails(Deno.env.get("VAPID_SUBJECT") || "mailto:admin@example.com", pub, priv);
    push = await sendPushes(db);
  }
  // email chạy SAU push và có hạn giờ (Edge Function bị dừng ở ~150 giây) → push không bao giờ bị email làm trễ/mất
  const mail = await sendWeeklyEmails(db, t0 + 90_000);
  if (!(pub && priv) && !mail) return new Response("vapid not configured", { status: 500 });
  if (typeof push === "object" && push.error) return new Response(JSON.stringify({ push, email: mail }), { status: 500, headers: { "content-type": "application/json" } });
  return new Response(JSON.stringify({ push, email: mail }), { headers: { "content-type": "application/json" } });
});
