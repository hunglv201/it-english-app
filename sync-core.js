/* Nói Nghề v4.0 — lõi đồng bộ (hàm thuần, không phụ thuộc trình duyệt; test bằng node: tests/sync-core.test.mjs)
 * Dữ liệu học được "làm phẳng" thành bản đồ path -> value để gửi từng thay đổi nhỏ lên server (apply_changes)
 * và gộp đúng khi 2 máy cùng sửa. Luật gộp resolve() phải GIỐNG HỆT nn_resolve() trong
 * supabase/migrations/20260920000002_sync.sql.
 */
(function (root) {
  'use strict';
  var SEP = '|';
  function esc(s) { return String(s).replace(/%/g, '%25').replace(/\|/g, '%7C'); }
  function unesc(s) { return String(s).replace(/%7C/g, '|').replace(/%25/g, '%'); }
  function path() { return Array.prototype.map.call(arguments, esc).join(SEP); }
  function split(p) { return String(p).split(SEP).map(unesc); }

  // Khoá cfg chỉ thuộc về từng máy (giọng đọc, nhắc học) hoặc đã nằm ở chỗ khác (focus → tdays)
  var CFG_LOCAL = { voiceName: 1, voiceURI: 1, remind: 1, focus: 1 };
  // Danh sách có khoá riêng: [tên trong store, tên nhóm, hàm lấy khoá, trường thời gian để sắp xếp (desc), bỏ trường]
  var LISTS = [
    ['saved', 'saved', function (x) { return x.en; }, 'ts'],
    ['myVocab', 'myVocab', function (x) { return x.t; }, null],
    ['standups', 'standups', function (x) { return x.date; }, 'date'],
    ['events', 'events', function (x) { return x.id; }, null],
    ['reports', 'reports', function (x) { return x.at; }, 'at'],
    ['convos', 'convos', function (x) { return x.id; }, 'id', ['turns']],
    ['photoLessons', 'photos', function (x) { return (x.at || '') + '~' + String(x.summary || '').slice(0, 40); }, 'at']
  ];
  var SCALARS = ['customPack', 'theme', 'swipeSeen'];

  var MAX_PATH = 900; // server nhận path ≤ 1000 ký tự; dài hơn thì không đồng bộ (hiếm: câu rất dài)
  function hash(str) { var h = 5381; for (var i = 0; i < str.length; i++) h = ((h << 5) + h + str.charCodeAt(i)) | 0; return (h >>> 0).toString(36); }
  function lkey(L, x) { // khoá của mục trong danh sách; khoá quá dài → rút gọn + băm (giá trị vẫn giữ đầy đủ)
    var k = L[2](x); if (k === undefined || k === null || k === '') return null;
    k = String(k); return k.length > 240 ? k.slice(0, 160) + '~' + hash(k) : k;
  }
  function clean(v) { // bỏ undefined / hàm, giữ JSON thuần; null → undefined
    if (v === undefined || v === null || typeof v === 'function') return undefined;
    try { var s = JSON.stringify(v); return s === undefined ? undefined : JSON.parse(s); } catch (e) { return undefined; }
  }
  function put(f, p, v) { if (p.length > MAX_PATH) return; v = clean(v); if (v !== undefined) f[p] = v; }
  function omit(o, keys) { var r = {}; for (var k in o) if (!keys || keys.indexOf(k) < 0) r[k] = o[k]; return r; }

  /** store (+ game save) → bản đồ phẳng */
  function toFlat(store, game) {
    var f = {}, k;
    store = store || {};
    var cfg = store.cfg || {};
    for (k in cfg) if (!CFG_LOCAL[k]) put(f, path('cfg', k), cfg[k]);
    var st = store.stats || {};
    for (k in st) put(f, path('stats', k), st[k]);
    ['srs', 'psrs', 'hist'].forEach(function (g) { var m = store[g] || {}; for (var kk in m) put(f, path(g, kk), m[kk]); });
    // tiến độ lộ trình theo ngành: days (ngành đang mở) + trackDays (các ngành khác)
    var td = {};
    var tds = store.trackDays || {};
    for (k in tds) td[k] = { days: (tds[k] || {}).days || {}, focus: (tds[k] || {}).focus };
    if (store.daysTrack && store.days) td[store.daysTrack] = { days: store.days, focus: cfg.focus };
    for (k in td) {
      var d = td[k].days || {}, done = d.done || {};
      for (var n in done) if (done[n]) put(f, path('tdays', k, 'done', n), true);
      if (d.cur) put(f, path('tdays', k, 'cur'), d.cur);
      if (td[k].focus && td[k].focus.length) put(f, path('tdays', k, 'focus'), td[k].focus);
    }
    if (store.today && store.today.date) {
      var dn = store.today.done || {};
      for (k in dn) if (dn[k]) put(f, path('today', store.today.date, k), true);
    }
    LISTS.forEach(function (L) {
      (store[L[0]] || []).forEach(function (x) {
        if (!x || typeof x !== 'object') return;
        var key = lkey(L, x); if (key === null) return;
        put(f, path(L[1], key), L[4] ? omit(x, L[4]) : x);
      });
    });
    SCALARS.forEach(function (s) { put(f, path(s), store[s]); });
    if (game && typeof game === 'object') for (k in game) put(f, path('game', k), game[k]);
    return f;
  }

  /** Ghi bản đồ phẳng vào store (giữ nguyên phần không đồng bộ: key AI, lượt chat đầy đủ…). Trả về game (hoặc null). */
  function fromFlat(flat, store, curTrack) {
    var g = {}, p, s;
    for (p in flat) {
      s = split(p);
      (g[s[0]] = g[s[0]] || []).push([s, flat[p]]);
    }
    function each(name, fn) { (g[name] || []).forEach(function (e) { fn(e[0], e[1]); }); }
    // cfg: giữ khoá riêng của máy
    var cfg = {}, k;
    for (k in store.cfg || {}) if (CFG_LOCAL[k]) cfg[k] = store.cfg[k];
    each('cfg', function (s, v) { cfg[s[1]] = v; });
    var stats = {};
    each('stats', function (s, v) { stats[s[1]] = v; });
    store.stats = stats;
    ['srs', 'psrs', 'hist'].forEach(function (name) {
      var m = {}, old = store[name] || {};
      for (var ok in old) if (path(name, ok).length > MAX_PATH) m[ok] = old[ok]; // khoá quá dài không đồng bộ → giữ nguyên trên máy
      each(name, function (s, v) { m[s[1]] = v; }); store[name] = m;
    });
    // tdays → days (ngành đang mở) + trackDays
    var td = {};
    each('tdays', function (s, v) {
      var t = td[s[1]] = td[s[1]] || { days: { done: {}, cur: 1 } };
      if (s[2] === 'done') t.days.done[s[3]] = true;
      else if (s[2] === 'cur') t.days.cur = v;
      else if (s[2] === 'focus') t.focus = v;
    });
    var cur = curTrack || store.daysTrack || cfg.track || 'office';
    var mine = td[cur] || { days: { done: {}, cur: 1 } };
    store.days = mine.days; cfg.focus = mine.focus || [];
    delete td[cur];
    store.trackDays = td;
    store.daysTrack = cur;
    store.cfg = cfg;
    // hôm nay: ưu tiên ngày đang dùng trên máy (máy khác lệch nửa đêm/múi giờ không được thay mất), không có thì lấy ngày mới nhất
    var today = null, myDate = store.today && store.today.date;
    each('today', function (s) { if (s[1] === myDate) today = { date: myDate, done: {} }; });
    if (!today) each('today', function (s) { if (!today || s[1] > today.date) today = { date: s[1], done: {} }; });
    if (today) each('today', function (s) { if (s[1] === today.date) today.done[s[2]] = true; });
    if (today) store.today = today; else delete store.today;
    // danh sách: giữ thứ tự cũ, cập nhật giá trị, bỏ mục đã xoá, thêm mục mới
    LISTS.forEach(function (L) {
      var byKey = {}, order = [];
      each(L[1], function (s, v) { byKey[s[1]] = v; order.push(s[1]); });
      var old = store[L[0]] || [], out = [], seen = {};
      old.forEach(function (x) {
        if (!x || typeof x !== 'object') return;
        var key = lkey(L, x);
        if (key === null || !(key in byKey) || seen[key]) return;
        seen[key] = 1;
        var nv = byKey[key];
        if (L[4]) { nv = Object.assign({}, nv); L[4].forEach(function (f2) { if (x[f2] !== undefined) nv[f2] = x[f2]; }); }
        out.push(nv);
      });
      order.forEach(function (key) { if (!seen[key]) { seen[key] = 1; out.push(byKey[key]); } });
      if (L[3]) {
        var tf = L[3];
        out.sort(function (a, b) { var x = a[tf], y = b[tf]; return x === y ? 0 : (x === undefined ? 1 : y === undefined ? -1 : (x < y ? 1 : -1)); });
      }
      if (out.length || store[L[0]]) store[L[0]] = out;
    });
    SCALARS.forEach(function (name) {
      var has = false;
      each(name, function (s, v) { store[name] = v; has = true; });
      if (!has) delete store[name];
    });
    var game = null;
    each('game', function (s, v) { game = game || {}; game[s[1]] = v; });
    return game;
  }

  function same(a, b) {
    if (a === b) return true;
    if (a === undefined || b === undefined || a === null || b === null) return false;
    if (typeof a !== 'object' || typeof b !== 'object') return a === b;
    return canon(a) === canon(b);
  }
  function canon(v) {
    if (v === null || typeof v !== 'object') return JSON.stringify(v);
    if (Array.isArray(v)) return '[' + v.map(canon).join(',') + ']';
    return '{' + Object.keys(v).sort().map(function (k) { return JSON.stringify(k) + ':' + canon(v[k]); }).join(',') + '}';
  }
  function num(x) { return typeof x === 'number' && isFinite(x) ? x : null; }

  /** Luật gộp khi server có e, máy gửi v (cả hai đều đã đổi so với bản gốc). Giống nn_resolve (SQL). */
  function resolve(p, e, v) {
    if (e === undefined || e === null) return v;
    if (v === undefined || v === null) return e;
    var s = split(p), top = s[0];
    if (top === 'srs' || top === 'psrs') {
      var er = num(e && e.reps) || 0, vr = num(v && v.reps) || 0;
      if (vr > er) return v;
      if (vr < er) return e;
      return (num(v && v.due) || 0) >= (num(e && e.due) || 0) ? v : e;
    }
    if (top === 'hist' || (top === 'stats' && num(e) !== null && num(v) !== null) || (top === 'tdays' && s[2] === 'cur')) {
      return Math.max(num(e) || 0, num(v) || 0);
    }
    return v;
  }

  /** Thay đổi của máy so với bản đã đồng bộ (shadow) → danh sách {p, v | d, b} */
  function diff(local, shadow) {
    var ops = [], p, newest = '';
    for (p in local) {
      if (p.lastIndexOf('today|', 0) === 0) { var dd = p.split(SEP)[1]; if (dd > newest) newest = dd; }
      if (!same(local[p], shadow[p])) {
        var o = { p: p, v: local[p] };
        if (shadow[p] !== undefined) o.b = shadow[p];
        ops.push(o);
      }
    }
    // "hôm nay": máy chỉ giữ ngày của mình → không xoá việc hôm nay của máy khác (lệch nửa đêm / múi giờ); chỉ dọn ngày cũ > 2 ngày
    var cut = newest ? new Date(Date.parse(newest) - 2 * 864e5).toISOString().slice(0, 10) : '';
    for (p in shadow) if (local[p] === undefined) {
      if (p.lastIndexOf('today|', 0) === 0 && !(cut && p.split(SEP)[1] < cut)) continue;
      ops.push({ p: p, d: true, b: shadow[p] });
    }
    return ops;
  }

  /** Gộp bản server mới kéo về. mode: 'merge' (mặc định) | 'account' (lấy server) | 'device' (giữ máy).
   *  Trả { local: bản đồ mới cho máy, shadow: bản gốc mới, changed: số path thay đổi trên máy } */
  function mergePull(local, shadow, server, mode) {
    mode = mode || 'merge';
    var out = {}, changed = 0, p, keys = {};
    if (mode === 'account') {
      for (p in server) out[p] = server[p];
    } else if (mode === 'device') {
      for (p in local) out[p] = local[p];
    } else {
      for (p in local) keys[p] = 1; for (p in shadow) keys[p] = 1; for (p in server) keys[p] = 1;
      for (p in keys) {
        var l = local[p], s = shadow[p], v = server[p], r;
        if (same(l, s) || (l === undefined && s === undefined)) r = v;          // máy không sửa → lấy server
        else if (same(v, s) || (v === undefined && s === undefined)) r = l;     // server không đổi → giữ bản máy
        else if (l === undefined) r = v;                                         // máy xoá, server sửa → giữ
        else if (v === undefined) r = l;                                         // server xoá, máy sửa → giữ
        else r = resolve(p, v, l);
        if (r !== undefined) out[p] = r;
      }
    }
    for (p in out) if (!same(out[p], local[p])) changed++;
    for (p in local) if (out[p] === undefined) changed++;
    var sh = {}; for (p in server) sh[p] = server[p];
    return { local: out, shadow: sh, changed: changed };
  }

  /** Mức "có tiến độ đáng kể" để quyết định có hỏi gộp hay không */
  function progressScore(flat) {
    var n = 0;
    for (var p in flat) { var t = p.split(SEP)[0]; if (t === 'srs' || t === 'psrs' || t === 'tdays' || t === 'saved' || t === 'myVocab' || t === 'hist') n++; }
    return n;
  }

  var api = { esc: esc, unesc: unesc, path: path, split: split, toFlat: toFlat, fromFlat: fromFlat, diff: diff, resolve: resolve,
              mergePull: mergePull, same: same, progressScore: progressScore, CFG_LOCAL: CFG_LOCAL };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.NNSync = api;
})(typeof window !== 'undefined' ? window : globalThis);
