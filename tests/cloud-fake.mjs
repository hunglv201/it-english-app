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
