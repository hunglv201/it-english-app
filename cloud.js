/* Nói Nghề v4.0 — kết nối máy chủ (Supabase): tài khoản khách tự động + Google, đồng bộ offline-first, AI qua server, báo lỗi.
 * Chỉ bật khi cloud-config.js có url + anonKey và app chạy trên GitHub Pages/localhost (không bật trong claude.ai).
 * Máy là bản sao làm việc: mọi thao tác ghi localStorage trước, bộ đồng bộ chạy nền đẩy/kéo khi có mạng.
 * Test: window.NN_CLOUD_ADAPTER (factory) thay supabase-js bằng server giả — xem tests/i.mjs.
 */
(function () {
  'use strict';
  var CFG = window.NN_CLOUD_CONFIG || {};
  var host = location.hostname || '';
  var hostOk = /(^|\.)github\.io$|^localhost$|^127\.0\.0\.1$/.test(host) || (CFG.hosts || []).indexOf(host) >= 0;
  var ENABLED = !!(CFG.url && CFG.anonKey) && hostOk && !window.NN_CLOUD_DISABLED;
  var META_KEY = 'noinghe-cloud-v1', GAME_KEY = 'it-english-game-v1';
  var BATCH = 250, RETRY = [5, 15, 60, 300];

  var H = {}; // hook của app: getStore, saveStore, track, appVersion, onState, onPulled, onChoice, onIdentityConflict, onUpdateRequired, onGuestCreated, toast
  var A = null; // adapter (supabase-js hoặc giả lập khi test)
  var M = loadMeta();
  var S = { status: ENABLED ? 'starting' : 'off', user: null, error: null, quota: null, ready: false };
  var busy = false, again = false, timer = null, tries = 0, lastRevCheck = 0, suppressTouch = false;
  var epoch = 0; // tăng mỗi lần đổi tài khoản: kết quả mạng của lượt cũ về muộn thì bỏ, không ghi vào meta tài khoản mới
  function stale(e0) { if (e0 !== epoch) { var x = new Error('stale'); x.stale = true; throw x; } }

  function loadMeta() {
    var m = null;
    try { m = JSON.parse(localStorage.getItem(META_KEY) || 'null'); } catch (e) {}
    m = m || {};
    if (!m.mode) m.mode = 'auto';
    if (!m.shadow) m.shadow = {};
    if (!m.rev) m.rev = 0;
    return m;
  }
  function saveMeta() { try { localStorage.setItem(META_KEY, JSON.stringify(M)); } catch (e) {} }
  function resetMeta(mode) { M = { mode: mode || 'auto', shadow: {}, rev: 0, uid: null, pending: null, lastSync: M.lastSync || null, noticeSeen: M.noticeSeen }; saveMeta(); }
  function rid() { return Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 10); }
  function emit() { if (H.onState) try { H.onState(state()); } catch (e) {} }
  function setStatus(s, err) { S.status = s; S.error = err || null; emit(); }
  function online() { return navigator.onLine !== false; }

  // ---------- dữ liệu máy <-> bản đồ phẳng ----------
  function readGame() { try { return JSON.parse(localStorage.getItem(GAME_KEY) || 'null'); } catch (e) { return null; } }
  function localFlat() { return NNSync.toFlat(H.getStore ? H.getStore() : {}, readGame()); }
  function writeLocal(flat) {
    var st = H.getStore();
    flat = JSON.parse(JSON.stringify(flat)); // tách khỏi shadow: app sửa thẳng object (vd grade()) không được làm đổi shadow
    var game = NNSync.fromFlat(flat, st, H.track);
    try { if (game) localStorage.setItem(GAME_KEY, JSON.stringify(game)); else localStorage.removeItem(GAME_KEY); } catch (e) {}
    suppressTouch = true;
    try { H.saveStore(); } finally { suppressTouch = false; }
  }
  function pendingCount() {
    if (!ENABLED || !S.user) return 0;
    try { return NNSync.diff(localFlat(), M.shadow).length + (M.pending ? M.pending.ops.length : 0); } catch (e) { return 0; }
  }

  // ---------- adapter supabase-js ----------
  function loadScript(src) {
    return new Promise(function (res, rej) {
      var s = document.createElement('script'); s.src = src; s.async = true;
      s.onload = res; s.onerror = function () { rej(new Error('load ' + src)); };
      document.head.appendChild(s);
    });
  }
  function errOf(error, extra) {
    var e = new Error((error && (error.message || error.error_description)) || 'error');
    if (error) { e.code = error.code; e.status = error.status; }
    for (var k in extra || {}) e[k] = extra[k];
    return e;
  }
  function supabaseAdapter() {
    var sb = window.supabase.createClient(CFG.url, CFG.anonKey, {
      auth: { flowType: 'pkce', persistSession: true, autoRefreshToken: true, detectSessionInUrl: true, storageKey: 'noinghe-auth' }
    });
    return {
      getSession: function () { return sb.auth.getSession().then(function (r) { return r.data && r.data.session; }); },
      onAuth: function (cb) { sb.auth.onAuthStateChange(function (ev, session) { cb(ev, session); }); },
      signInAnon: function (captchaToken) {
        return sb.auth.signInAnonymously(captchaToken ? { options: { captchaToken: captchaToken } } : undefined)
          .then(function (r) { if (r.error) throw errOf(r.error); return r.data.session; });
      },
      linkGoogle: function (redirectTo) {
        return sb.auth.linkIdentity({ provider: 'google', options: { redirectTo: redirectTo } })
          .then(function (r) { if (r.error) throw errOf(r.error); });
      },
      signInGoogle: function (redirectTo) {
        return sb.auth.signInWithOAuth({ provider: 'google', options: { redirectTo: redirectTo } })
          .then(function (r) { if (r.error) throw errOf(r.error); });
      },
      signOut: function () { return sb.auth.signOut({ scope: 'local' }).then(function () {}); },
      rpc: function (name, args) {
        return sb.rpc(name, args || {}).then(function (r) { if (r.error) throw errOf(r.error); return r.data; });
      },
      fn: function (name, body) {
        return sb.functions.invoke(name, { body: body }).then(async function (r) {
          if (!r.error) return r.data;
          var status = 0, data = null;
          try { status = r.error.context && r.error.context.status; data = await r.error.context.json(); } catch (e) {}
          throw errOf(r.error, { status: status, body: data });
        });
      }
    };
  }

  // ---------- Cloudflare Turnstile (chống tạo tài khoản khách hàng loạt) ----------
  function captchaToken() {
    if (!CFG.turnstileSiteKey) return Promise.resolve(null);
    return (window.turnstile ? Promise.resolve() : loadScript('https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit'))
      .then(function () {
        return new Promise(function (res, rej) {
          var box = document.createElement('div');
          box.style.cssText = 'position:fixed;left:50%;bottom:90px;transform:translateX(-50%);z-index:9999';
          document.body.appendChild(box);
          var done = function (fn, v) { try { box.remove(); } catch (e) {} fn(v); };
          var to = setTimeout(function () { done(rej, new Error('captcha_timeout')); }, 30000);
          window.turnstile.render(box, {
            sitekey: CFG.turnstileSiteKey, appearance: 'interaction-only', action: 'guest',
            callback: function (t) { clearTimeout(to); done(res, t); },
            'error-callback': function () { clearTimeout(to); done(rej, new Error('captcha_failed')); }
          });
        });
      });
  }

  // ---------- phiên đăng nhập ----------
  function userInfo(session) {
    var u = session && session.user;
    if (!u) return null;
    var md = u.user_metadata || {};
    return { id: u.id, anon: !!u.is_anonymous, email: u.email || '', name: md.full_name || md.name || '', avatar: md.avatar_url || md.picture || '' };
  }

  var adopting = null, adoptBusy = false;
  function adoptSession(x) { // x: session hoặc userInfo
    var u = x && x.user ? userInfo(x) : x;
    if (!u || !u.id) return Promise.resolve();
    if (adopting && adopting.uid === u.id) return adopting.p;
    var p = adoptSession0(u).finally(function () { if (adopting && adopting.p === p) adopting = null; });
    adopting = { uid: u.id, p: p };
    return p;
  }
  async function adoptSession0(u) {
    S.user = u;
    if (H.onAuthChanged) try { H.onAuthChanged(); } catch (e) {}
    if (M.uid === u.id && !M.choice) { M.anon = u.anon; saveMeta(); emit(); return syncNow({ pull: true }); }
    // Tài khoản khác bản sao trên máy (lần đầu, hoặc vừa đăng nhập Google đã có tiến độ).
    // Xoá shadow/uid NGAY (trước khi chờ mạng) để không lượt đồng bộ nào dùng shadow của tài khoản cũ.
    M.uid = null; M.pending = null; M.shadow = {}; M.rev = 0; M.choice = null; saveMeta();
    epoch++;
    adoptBusy = true;
    var mode;
    try {
      var st = await A.rpc('get_state');
      var server = (st && st.state) || {};
      var local = localFlat();
      if (!NNSync.progressScore(server)) mode = 'merge';                 // tài khoản trống → đẩy tiến độ máy lên
      else if (NNSync.progressScore(local) < 5) mode = 'account';       // máy gần như trống → lấy tiến độ tài khoản
      M.uid = u.id; M.anon = u.anon;
      if (!mode) {
        M.choice = { uid: u.id, at: Date.now() }; saveMeta();
        setStatus('paused');
        if (H.onChoice) H.onChoice({ local: NNSync.progressScore(local), server: NNSync.progressScore(server) });
        return;
      }
      saveMeta();
      await pull(mode, st);
    } finally { adoptBusy = false; }
    return syncNow();
  }

  async function createGuest(force) {
    if (!online() || M.mode === 'local') return;
    if (M.uid && !force) { setStatus('relogin'); return; } // máy từng có tài khoản → không tự thay bằng khách mới
    setStatus('syncing');
    var token = null;
    token = await captchaToken(); // lỗi captcha → nơi gọi thử lại sau
    var session = await A.signInAnon(token);
    M.guestAt = Date.now(); saveMeta();
    if (H.onGuestCreated) try { H.onGuestCreated(); } catch (e) {}
    await adoptSession(session);
  }

  function readAuthError() {
    var q = new URLSearchParams(location.search), h = new URLSearchParams((location.hash || '').replace(/^#/, ''));
    var code = q.get('error_code') || h.get('error_code'), err = q.get('error') || h.get('error');
    var desc = q.get('error_description') || h.get('error_description') || '';
    if (!code && !err) return null;
    try {
      ['error', 'error_code', 'error_description'].forEach(function (k) { q.delete(k); });
      var qs = q.toString();
      history.replaceState(null, '', location.pathname + (qs ? '?' + qs : '') + (h.get('error') ? '' : location.hash));
    } catch (e) {}
    return { code: code || err, desc: desc };
  }

  // ---------- đồng bộ ----------
  function schedule(ms) { clearTimeout(timer); timer = setTimeout(function () { syncNow(); }, ms); }
  function touch() { if (!ENABLED || suppressTouch || !S.user || M.choice) return; schedule(3000); }

  async function pushBatch() {
    if (!M.pending) {
      var ops = NNSync.diff(localFlat(), M.shadow);
      if (!ops.length) return false;
      M.pending = { id: rid(), ops: ops.slice(0, BATCH) };
      saveMeta();
    }
    var sent = M.pending, e0 = epoch;
    var res = await A.rpc('apply_changes', { p_id: sent.id, p_changes: sent.ops, p_base_rev: M.rev, p_app_version: H.appVersion || null });
    stale(e0);
    if (res && res.error === 'update_required') { var e = new Error('update_required'); e.min = res.min; throw e; }
    // phản hồi lạ / lỗi → giữ nguyên lô để gửi lại, tuyệt đối không coi thiếu vals là "đã xoá"
    if (!res || res.error || typeof res.rev !== 'number' || !res.vals || typeof res.vals !== 'object') throw new Error((res && res.error) || 'bad_response');
    var vals = (res && res.vals) || {}, now = localFlat(), fixes = {}, nfix = 0;
    sent.ops.forEach(function (o) {
      var fin = vals[o.p]; if (fin === null) fin = undefined;
      if (fin === undefined) delete M.shadow[o.p]; else M.shadow[o.p] = fin;
      var mine = o.d ? undefined : o.v;
      // server gộp khác bản đã gửi (máy khác sửa cùng lúc) và máy chưa sửa tiếp → nhận bản đã gộp
      if (!NNSync.same(fin, mine) && NNSync.same(now[o.p], mine)) { fixes[o.p] = fin; nfix++; }
    });
    var others = res.dup || (res.prev !== undefined && res.prev !== M.rev);
    M.rev = res.rev; M.pending = null; saveMeta();
    if (nfix) {
      for (var p in fixes) { if (fixes[p] === undefined) delete now[p]; else now[p] = fixes[p]; }
      writeLocal(now);
      if (H.onPulled) try { H.onPulled(nfix); } catch (e) {}
    }
    return others ? 'pull' : true;
  }

  async function pull(mode, st) {
    var e0 = epoch;
    st = st || await A.rpc('get_state');
    stale(e0);
    if (!st || typeof st.rev !== 'number' || !st.state || typeof st.state !== 'object') throw new Error('bad_response');
    var server = (st && st.state) || {};
    var m = NNSync.mergePull(localFlat(), M.shadow, server, mode);
    M.shadow = m.shadow; M.rev = (st && st.rev) || 0; M.choice = null; saveMeta();
    if (m.changed) {
      writeLocal(m.local);
      if (H.onPulled) try { H.onPulled(m.changed); } catch (e) {}
    }
    lastRevCheck = Date.now();
  }

  async function sendReports() {
    var st = H.getStore && H.getStore();
    var list = ((st && st.reports) || []).filter(function (r) { return r && !r.cloud; }).slice(0, 10);
    var n = 0;
    for (var i = 0; i < list.length; i++) {
      var r = list[i];
      var res = await A.rpc('report_content', { r: { at: r.at, track: r.track, kind: r.kind, type: r.type, text: r.text, note: r.note, where: r.where, v: H.appVersion } });
      if (res && res.error) break;
      r.cloud = 1; n++;
    }
    if (n) H.saveStore();
    return n;
  }

  async function syncNow(opts) {
    opts = opts || {};
    if (!ENABLED || !A || adoptBusy) return;
    if (S.user && M.uid !== S.user.id && !M.choice) { // lần nhận tài khoản trước chưa xong (lỗi mạng) → làm lại
      try { await adoptSession(S.user); tries = 0; }
      catch (e) { setStatus(online() ? 'error' : 'offline', String((e && e.message) || e).slice(0, 120)); schedule(1000 * RETRY[Math.min(tries++, RETRY.length - 1)]); }
      return;
    }
    if (!S.user) { // chưa có tài khoản (lần trước tạo khách lỗi) → thử lại, giãn dần
      if (M.mode === 'local' || M.uid || !online() || busy) return;
      busy = true;
      try { await createGuest(); tries = 0; }
      catch (e) { setStatus(online() ? 'error' : 'offline', String((e && e.message) || e).slice(0, 120)); schedule(1000 * RETRY[Math.min(tries++, RETRY.length - 1)]); }
      finally { busy = false; }
      if (S.user) return syncNow(opts);
      return;
    }
    if (M.choice) { setStatus('paused'); return; }
    if (!online()) { setStatus('offline'); return; }
    if (busy) { again = true; return; }
    busy = true; clearTimeout(timer);
    setStatus('syncing');
    try {
      var needPull = !!opts.pull, r, loops = 0;
      while (loops++ < 40 && (r = await pushBatch())) { if (r === 'pull') needPull = true; }
      if (!needPull && Date.now() - lastRevCheck > 60000) {
        lastRevCheck = Date.now();
        var rv = await A.rpc('get_rev');
        if (rv !== M.rev) needPull = true;
      }
      if (needPull) { await pull('merge'); while (loops++ < 80 && await pushBatch()) {} }
      await sendReports();
      M.lastSync = Date.now(); saveMeta(); tries = 0;
      setStatus('ok');
    } catch (e) {
      if (e && e.stale) { /* đã đổi tài khoản giữa chừng — lượt mới sẽ chạy */ }
      else if (e && e.message === 'update_required') {
        setStatus('update');
        if (H.onUpdateRequired) try { H.onUpdateRequired(e.min); } catch (x) {}
      } else {
        setStatus(online() ? 'error' : 'offline', String((e && e.message) || e).slice(0, 120));
        schedule(1000 * RETRY[Math.min(tries++, RETRY.length - 1)]);
      }
    } finally {
      busy = false;
      if (again) { again = false; schedule(800); }
    }
  }

  // ---------- khởi động ----------
  async function init() {
    if (!ENABLED) { emit(); return; }
    try {
      if (window.NN_CLOUD_ADAPTER) A = window.NN_CLOUD_ADAPTER(CFG);
      else { if (!window.supabase) await loadScript('vendor/supabase.min.js'); A = supabaseAdapter(); }
    } catch (e) { setStatus('error', 'load'); return; }
    var authErr = readAuthError();
    var session = null;
    try { session = await A.getSession(); } catch (e) {}
    S.ready = true;
    A.onAuth(function (ev, sess) {
      if (ev === 'SIGNED_OUT') { S.user = null; if (M.uid) setStatus('relogin'); else emit(); return; }
      var u = userInfo(sess);
      if (!u) return;
      if (S.user && S.user.id === u.id) { S.user = u; emit(); return; }  // làm mới token / cập nhật thông tin
      adoptSession(u).catch(function (e) { setStatus('error', e.message); }); // kể cả TOKEN_REFRESHED sau khi mất mạng lúc mở app
    });
    if (authErr && /identity_already_exists|already/i.test(authErr.code + ' ' + authErr.desc)) {
      if (H.onIdentityConflict) try { H.onIdentityConflict(); } catch (e) {}
    } else if (authErr && H.toast) H.toast('Đăng nhập chưa xong: ' + (authErr.desc || authErr.code));
    try {
      if (session) await adoptSession(session);
      else if (M.uid) setStatus('relogin');          // từng có tài khoản mà mất phiên → không tự tạo khách mới
      else if (M.mode !== 'local') await createGuest();
      else setStatus('local');
    } catch (e) { setStatus(online() ? 'error' : 'offline', String(e.message || e)); schedule(1000 * RETRY[Math.min(tries++, RETRY.length - 1)]); }
    M.linking = null; saveMeta();
    window.addEventListener('online', function () {
      if (S.user) syncNow({ pull: true });
      else if (M.uid) A.getSession().then(function (s) { if (s) return adoptSession(s); }).catch(function () {});
      else if (M.mode !== 'local') createGuest().catch(function () {});
    });
    window.addEventListener('offline', function () { if (S.user) setStatus('offline'); });
    document.addEventListener('visibilitychange', function () {
      if (!S.user) return;
      if (document.hidden) syncNow(); else if (Date.now() - lastRevCheck > 30000) syncNow({ pull: true });
    });
    setInterval(function () { if (S.user && !busy && pendingCount()) syncNow(); }, 60000);
  }

  // ---------- thao tác cho giao diện ----------
  function redirectUrl() { return location.origin + location.pathname; }
  async function linkGoogle() {
    if (!online()) throw new Error('offline');
    if (S.user) await syncNow();
    M.linking = { from: M.uid, at: Date.now() }; M.mode = 'auto'; saveMeta();
    if (S.user && S.user.anon) return A.linkGoogle(redirectUrl());
    return A.signInGoogle(redirectUrl());
  }
  async function signInGoogle() {
    if (!online()) throw new Error('offline');
    if (S.user) await syncNow();
    M.mode = 'auto'; saveMeta();
    return A.signInGoogle(redirectUrl());
  }
  async function signOut() {
    try { await syncNow(); } catch (e) {}
    try { await A.signOut(); } catch (e) {}
    S.user = null; S.quota = null; resetMeta('local');
    if (H.onAuthChanged) try { H.onAuthChanged(); } catch (e) {}
    setStatus('local');
  }
  async function startGuest() { M.mode = 'auto'; saveMeta(); await createGuest(true); }
  async function deleteAccount() {
    await A.fn('delete-account', { confirm: 'DELETE' });
    try { await A.signOut(); } catch (e) {}
    S.user = null; S.quota = null; resetMeta('local');
    if (H.onAuthChanged) try { H.onAuthChanged(); } catch (e) {}
    setStatus('local');
  }
  async function choose(mode) { // 'merge' | 'account' | 'device'
    if (!M.choice) return;
    M.shadow = {}; M.rev = 0; saveMeta();
    await pull(mode === 'device' ? 'device' : mode === 'account' ? 'account' : 'merge');
    return syncNow();
  }
  async function ai(req) {
    if (!S.user) throw new Error('no-session');
    if (!online()) throw new Error('offline');
    try {
      var r = await A.fn('ai', req);
      if (r && r.limit) S.quota = { remaining: r.remaining, limit: r.limit };
      return r;
    } catch (e) {
      var b = e.body || {};
      if (e.status === 429) {
        S.quota = { remaining: b.remaining || 0, limit: b.limit || 0 };
        var x = new Error(b.error === 'rate_limited' ? 'ai_rate_limited' : b.error === 'global_limit' ? 'ai_busy' : 'ai_daily_limit'); x.quota = S.quota; throw x;
      }
      throw e;
    }
  }
  async function quota() {
    if (!S.user || !online()) return S.quota;
    try { var q = await A.rpc('my_ai_quota'); S.quota = { remaining: Math.max(0, q.limit - q.used), limit: q.limit }; } catch (e) {}
    return S.quota;
  }

  function state() {
    return {
      enabled: ENABLED, ready: S.ready, status: S.status, error: S.error, mode: M.mode,
      user: S.user, signedIn: !!S.user, anon: !!(S.user && S.user.anon), google: !!(S.user && !S.user.anon),
      pending: pendingCount(), lastSync: M.lastSync || null, choice: !!M.choice, quota: S.quota,
      relogin: !S.user && !!M.uid, wasAnon: !!M.anon,
      guestAt: M.guestAt || null, noticeSeen: !!M.noticeSeen
    };
  }

  window.NNCloud = {
    enabled: ENABLED,
    bind: function (hooks) { for (var k in hooks) H[k] = hooks[k]; },
    init: init, touch: touch, syncNow: syncNow, state: state,
    linkGoogle: linkGoogle, signInGoogle: signInGoogle, signOut: signOut, startGuest: startGuest,
    deleteAccount: deleteAccount, choose: choose, ai: ai, quota: quota,
    aiReady: function () { return ENABLED && !!S.user; },
    markNotice: function () { M.noticeSeen = true; saveMeta(); }
  };
})();
