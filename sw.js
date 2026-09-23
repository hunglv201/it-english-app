/* Nói Nghề (IT English) — service worker (offline app shell) */
const CACHE = 'it-english-v4.2.0';
const ASSETS = [
  './', 'index.html', 'data.gen.js', 'phrases.gen.js', 'roles.gen.js',
  'packs/office.gen.js', 'packs/hotel.gen.js', 'packs/sales.gen.js', 'packs/factory.gen.js',
  'packs/logistics.gen.js', 'packs/finance.gen.js', 'packs/marketing.gen.js', 'packs/health.gen.js', 'packs/construction.gen.js', 'packs/aviation.gen.js', 'packs/education.gen.js', 'packs/legal.gen.js', 'packs/custom.js',
  'ja/keigo.js',
  'cloud-config.js', 'sync-core.js', 'cloud.js', 'vendor/supabase.min.js',
  'chinh-sach.html', 'dieu-khoan.html', 'xoa-du-lieu.html',
  'manifest.webmanifest', 'icon-192.png', 'icon-512.png'
];

self.addEventListener('install', function (e) {
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(ASSETS).catch(function () {}); }));
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
    }).then(function () { return self.clients.claim(); })
  );
});

// v4.0 đợt A: nhắc học Web Push từ máy chủ (Edge Function send-reminders)
self.addEventListener('push', function (e) {
  var d = {};
  try { d = e.data ? e.data.json() : {}; } catch (err) { d = { body: e.data ? e.data.text() : '' }; }
  e.waitUntil(self.registration.showNotification(d.title || 'Nói Nghề', {
    body: d.body || 'Luyện tiếng Anh 5 phút hôm nay nhé.', icon: 'icon-192.png', badge: 'icon-192.png',
    tag: d.tag || 'noinghe', renotify: false, data: { url: d.url || './' }
  }));
});

// Nhắc học: bấm vào thông báo thì mở/focus app
self.addEventListener('notificationclick', function (e) {
  e.notification.close();
  e.waitUntil(
    self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then(function (list) {
      for (var i = 0; i < list.length; i++) { if ('focus' in list[i]) return list[i].focus(); }
      if (self.clients.openWindow) return self.clients.openWindow('./');
    })
  );
});

self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') return;
  var url;
  try { url = new URL(req.url); } catch (err) { return; }
  // Chỉ xử lý tài nguyên cùng nguồn; font CDN, API AI và máy chủ Supabase để mạng lo (không cache)
  if (url.origin !== location.origin) return;

  var isHTML = req.mode === 'navigate' || url.pathname.endsWith('.html') || url.pathname.endsWith('/') || url.pathname.endsWith('cloud-config.js');
  if (isHTML) {
    // network-first: luôn ưu tiên bản mới, offline thì dùng cache
    e.respondWith(
      fetch(req).then(function (res) {
        var copy = res.clone();
        caches.open(CACHE).then(function (c) { c.put(req, copy); }).catch(function () {});
        return res;
      }).catch(function () {
        return caches.match(req).then(function (h) { return h || caches.match('index.html'); });
      })
    );
  } else {
    // cache-first cho data/js/icon (đổi ít, tải nhanh, chạy offline)
    e.respondWith(
      caches.match(req).then(function (h) {
        return h || fetch(req).then(function (res) {
          var copy = res.clone();
          caches.open(CACHE).then(function (c) { c.put(req, copy); }).catch(function () {});
          return res;
        });
      })
    );
  }
});
