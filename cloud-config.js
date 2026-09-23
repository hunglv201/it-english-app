/* Nói Nghề — cấu hình máy chủ (Supabase). Để trống = app chạy như trước, chỉ lưu trên máy.
 * url + anonKey là thông tin CÔNG KHAI (an toàn nằm ở RLS), được phép commit.
 * TUYỆT ĐỐI không dán service_role key hay key AI vào đây — những key đó chỉ nằm trong Supabase secrets.
 * turnstileSiteKey: site key Cloudflare Turnstile (công khai) — chống tạo tài khoản khách hàng loạt; để trống = tắt.
 */
window.NN_CLOUD_CONFIG = {
  url: '',          // https://<project-ref>.supabase.co
  anonKey: '',      // anon / publishable key
  turnstileSiteKey: '',
  vapidPublicKey: ''  // khoá công khai VAPID cho Web Push (npx web-push generate-vapid-keys); để trống = tắt nhắc qua máy chủ
};
