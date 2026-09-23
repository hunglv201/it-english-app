// Máy chủ giả cho test cloud (thay Supabase): auth khách/Google + apply_changes/get_state/report/AI.
// Luật apply_changes chép theo supabase/migrations/20260920000002_sync.sql (dùng chung resolve() của sync-core.js).
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const S = require('../sync-core.js');

export function fakeServer() {
  const users = new Map(); // uid -> {anon, email, state:{}, rev, applied:Set, reports:[], ai:0}
  let seq = 0;
  const newUser = (anon, email) => { const id = '00000000-0000-4000-8000-' + String(++seq).padStart(12, '0'); users.set(id, { anon, email: email || '', state: {}, rev: 0, applied: new Set(), reports: [], ai: 0, calls: 0 }); return id; };
  const sess = (id) => { const u = users.get(id); if (!u) return null; return { user: { id, is_anonymous: u.anon, email: u.email, user_metadata: u.anon ? {} : { full_name: 'Test ' + u.email.split('@')[0] } } }; };
  const apply = (u, id, changes) => {
    if (u.applied.has(id)) { const vals = {}; changes.forEach(c => { vals[c.p] = u.state[c.p] === undefined ? null : u.state[c.p]; }); return { rev: u.rev, prev: u.rev, dup: true, vals }; }
    const prev = u.rev, vals = {};
    for (const c of changes) {
      const cur = u.state[c.p]; const b = c.b === undefined || c.b === null ? undefined : c.b;
      const nv = c.d ? undefined : c.v;
      let fin;
      if (S.same(cur, b) || (cur === undefined && b === undefined)) fin = nv;
      else if (c.d) fin = cur;
      else fin = S.resolve(c.p, cur, nv);
      if (fin === undefined) delete u.state[c.p]; else u.state[c.p] = fin;
      vals[c.p] = fin === undefined ? null : fin;
    }
    u.rev++; u.applied.add(id);
    return { rev: u.rev, prev, vals };
  };
  const api = {
    users, calls: [],
    handle(method, a) {
      api.calls.push(method + (a && a.name ? ':' + a.name : ''));
      if (method === 'session') return a.uid && users.has(a.uid) ? sess(a.uid) : null;
      if (method === 'anon') return sess(newUser(true));
      if (method === 'link') { // khách liên kết Google
        const other = [...users.entries()].find(([id, u]) => u.email === a.email && id !== a.uid);
        if (other) return { error: 'identity_already_exists' };
        const u = users.get(a.uid); u.anon = false; u.email = a.email; return sess(a.uid);
      }
      if (method === 'google') { const f = [...users.entries()].find(([, u]) => u.email === a.email); return sess(f ? f[0] : newUser(false, a.email)); }
      const u = users.get(a.uid);
      if (!u) throw new Error('not_authenticated');
      if (method === 'rpc') {
        const g = a.args || {};
        if (a.name === 'apply_changes' && api.failNext) { const m = api.failNext; api.failNext = null; if (m === 'bad') return { error: 'weird' }; throw new Error(m); }
        if (a.name === 'apply_changes') { if (process.env.NN_DEBUG) console.log('APPLY', a.uid.slice(-2), g.p_changes.length, JSON.stringify(g.p_changes.map(c => c.p)).slice(0, 300)); const rr = apply(u, g.p_id, g.p_changes); if (process.env.NN_DEBUG) console.log('  ->', JSON.stringify(rr.vals['srs|deploy'])); return rr; }
        if (a.name === 'get_state') return { rev: u.rev, state: JSON.parse(JSON.stringify(u.state)) };
        if (a.name === 'get_rev') return u.rev;
        if (a.name === 'report_content') { if (!u.reports.some(r => r.at === g.r.at)) u.reports.push(g.r); return { ok: true }; }
        if (a.name === 'my_ai_quota') return { limit: u.anon ? 10 : 20, used: u.ai };
        // v4.0 đợt A/C — bản giả đơn giản (logic thật + quyền: supabase/tests/db2.test.sql)
        const nick = (x) => String(x || '').replace(/[<>"&]/g, '').trim().slice(0, 24);
        const days = (id) => Object.keys((users.get(id) || { state: {} }).state).filter(p => p.startsWith('hist|')).length;
        const tasks = (id) => Object.entries((users.get(id) || { state: {} }).state).filter(([p]) => p.startsWith('hist|')).reduce((t, [, v]) => t + (+v || 0), 0);
        const row = (id, n) => ({ nick: n, me: id === a.uid, days: days(id), tasks: tasks(id), streak: +(users.get(id).state['stats|streak'] || 0) });
        api.push = api.push || {}; api.classes = api.classes || []; api.invites = api.invites || {}; api.buddies = api.buddies || []; api.nudges = api.nudges || [];
        if (a.name === 'save_push') { api.push[a.uid] = Object.assign(api.push[a.uid] || {}, { sub: g.p_sub }); return { ok: true }; }
        if (a.name === 'set_reminder') { api.push[a.uid] = Object.assign(api.push[a.uid] || {}, { mode: g.p_mode, fixed: g.p_fixed_min, tz: g.p_tz_offset }); return { ok: true }; }
        if (a.name === 'touch_reminder') { api.push[a.uid] = Object.assign(api.push[a.uid] || {}, { first: g.p_first_min }); return null; }
        if (a.name === 'delete_push') { if (api.push[a.uid]) delete api.push[a.uid].sub; return null; }
        if (a.name === 'set_league') { if (g.p_on && nick(g.p_nick).length < 2) return { error: 'bad_nick' }; u.league = g.p_on ? nick(g.p_nick) : null; return { ok: true }; }
        if (a.name === 'league_board') { if (!u.league) return { on: false }; return { on: true, rows: [...users.entries()].filter(([, x]) => x.league).map(([id, x]) => row(id, x.league)) }; }
        if (a.name === 'buddy_invite') { if (!nick(g.p_nick)) return { error: 'bad_nick' }; const code = 'B' + String(++seq).padStart(7, '0').slice(0, 7); api.invites[code] = { uid: a.uid, nick: nick(g.p_nick) }; return { ok: true, code }; }
        if (a.name === 'buddy_accept') { const inv = api.invites[String(g.p_code).toUpperCase()]; if (!inv) return { error: 'not_found' }; if (inv.uid === a.uid) return { error: 'self' }; if (!nick(g.p_nick)) return { error: 'bad_nick' };
          api.buddies.push({ a: inv.uid, b: a.uid, na: inv.nick, nb: nick(g.p_nick) }); delete api.invites[String(g.p_code).toUpperCase()]; return { ok: true, nick: inv.nick }; }
        if (a.name === 'buddy_status') { const bd = api.buddies.find(x => x.a === a.uid || x.b === a.uid);
          if (!bd) { const inv = Object.entries(api.invites).find(([, v]) => v.uid === a.uid); return { paired: false, invite: inv ? inv[0] : null }; }
          const other = bd.a === a.uid ? bd.b : bd.a; return { paired: true, nick: bd.a === a.uid ? bd.nb : bd.na, shared_streak: 0, me_today: days(a.uid) > 0, buddy_today: false, can_nudge: !api.nudges.some(n => n.from === a.uid) }; }
        if (a.name === 'buddy_nudge') { if (api.nudges.some(n => n.from === a.uid)) return { error: 'already' }; api.nudges.push({ from: a.uid }); return { ok: true }; }
        if (a.name === 'buddy_remove') { api.buddies = api.buddies.filter(x => x.a !== a.uid && x.b !== a.uid); return null; }
        if (a.name === 'create_class') { if (u.anon) return { error: 'google_required' }; if (!nick(g.p_name)) return { error: 'bad_name' }; const c = { id: 'c' + (++seq), code: 'K' + String(seq).padStart(7, '0'), name: nick(g.p_name), owner: a.uid, members: [] }; api.classes.push(c); return { ok: true, id: c.id, code: c.code }; }
        if (a.name === 'join_class') { if (g.p_consent !== true) return { error: 'consent_required' }; if (nick(g.p_nick).length < 2) return { error: 'bad_nick' }; const c = api.classes.find(x => x.code === String(g.p_code).toUpperCase()); if (!c) return { error: 'not_found' };
          c.members = c.members.filter(m => m.uid !== a.uid).concat([{ uid: a.uid, nick: nick(g.p_nick), consent: Date.now() }]); return { ok: true, id: c.id, name: c.name }; }
        if (a.name === 'my_classes') return api.classes.filter(c => c.owner === a.uid || c.members.some(m => m.uid === a.uid)).map(c => ({ id: c.id, name: c.name, code: c.owner === a.uid ? c.code : null, owner: c.owner === a.uid, members: c.members.length }));
        if (a.name === 'class_board') { const c = api.classes.find(x => x.id === g.p_class); if (!c || !(c.owner === a.uid || c.members.some(m => m.uid === a.uid))) throw new Error('forbidden'); return c.members.map(m => row(m.uid, m.nick)); }
        if (a.name === 'class_report') { const c = api.classes.find(x => x.id === g.p_class); if (!c || c.owner !== a.uid) throw new Error('forbidden'); return c.members.map(m => ({ nick: m.nick, days_week: days(m.uid), tasks_week: tasks(m.uid), days_30: days(m.uid), last_active: null, track: 'office', joined: '2026-09-23' })); }
        if (a.name === 'leave_class') { api.classes.forEach(c => { if (c.id === g.p_class) c.members = c.members.filter(m => m.uid !== a.uid); }); return null; }
        if (a.name === 'delete_class') { api.classes = api.classes.filter(c => !(c.id === g.p_class && c.owner === a.uid)); return null; }
        throw new Error('unknown rpc ' + a.name);
      }
      if (method === 'fn') {
        if (a.name === 'ai') { const lim = u.anon ? 10 : 20; if (u.ai >= lim) return { __status: 429, body: { ok: false, error: 'daily_limit', limit: lim, remaining: 0 } }; u.ai++; u.calls++; return { text: 'Cloud AI says hi (' + a.body.turns.length + ' turns' + (a.body.image ? ', image' : '') + ')', remaining: lim - u.ai, limit: lim }; }
        if (a.name === 'delete-account') { if (a.body.confirm !== 'DELETE') return { __status: 400, body: { error: 'confirm_required' } }; users.delete(a.uid); return { ok: true }; }
      }
      throw new Error('unknown ' + method);
    }
  };
  return api;
}

// Chạy trong trang: adapter giống supabaseAdapter() của cloud.js, gọi server giả qua window.nnFake (exposeFunction)
export const adapterInit = () => {
  window.NN_CLOUD_ADAPTER = function () {
    const cbs = [];
    const uid = () => localStorage.getItem('fake-auth') || '';
    const call = async (m, a) => { const r = await window.nnFake(m, Object.assign({ uid: uid() }, a || {})); if (r && r.__err) { const e = new Error(r.__err); throw e; } return r; };
    const fire = (ev, s) => cbs.forEach(cb => { try { cb(ev, s); } catch (e) {} });
    const go = (url) => { setTimeout(() => { location.href = url; }, 30); };
    return {
      getSession: () => uid() ? call('session') : Promise.resolve(null),
      onAuth: (cb) => cbs.push(cb),
      signInAnon: async () => { const s = await call('anon'); localStorage.setItem('fake-auth', s.user.id); fire('SIGNED_IN', s); return s; },
      linkGoogle: async (to) => { const r = await call('link', { email: window.__googleEmail }); if (r && r.error) go(to + '?error=server_error&error_code=' + r.error + '&error_description=Identity+is+already+linked+to+another+user'); else go(to); },
      signInGoogle: async (to) => { const s = await call('google', { email: window.__googleEmail }); localStorage.setItem('fake-auth', s.user.id); go(to); },
      signOut: async () => { localStorage.removeItem('fake-auth'); fire('SIGNED_OUT', null); },
      rpc: (name, args) => call('rpc', { name, args }),
      fn: async (name, body) => { const r = await call('fn', { name, body }); if (r && r.__status) { const e = new Error('http ' + r.__status); e.status = r.__status; e.body = r.body; throw e; } return r; }
    };
  };
};
