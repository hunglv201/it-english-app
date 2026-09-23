// node tests/sync-core.test.mjs — test lõi đồng bộ (không cần trình duyệt)
import { createRequire } from 'module';
import assert from 'assert/strict';
const require = createRequire(import.meta.url);
const S = require('../sync-core.js');
let n = 0; const t = (name, fn) => { fn(); n++; };

const store = () => ({
  cfg: { track: 'hotel', role: 'fo', level: 'B1', autoSpeak: true, focus: ['p1'], remind: '20:00', voiceName: 'Samantha' },
  stats: { done: 12, streak: 3, lastDay: '2026-09-20', placed: true },
  srs: { 'deploy': { ease: 2.3, int: 1, reps: 1, due: 100 }, 'a|b%c': { ease: 2.5, int: 3, reps: 2, due: 200 } },
  psrs: { 'Could you help me?': { ease: 2.3, int: 0, reps: 0, due: 5, vi: 'Giúp tôi?', src: 'phrase', n: 1 } },
  hist: { '2026-09-19': 4, '2026-09-20': 2 },
  days: { done: { 1: true, 2: true }, cur: 3 }, daysTrack: 'hotel',
  trackDays: { it: { days: { done: { 1: true }, cur: 2 }, focus: [] } },
  today: { date: '2026-09-20', done: { vocab: true, listen: true } },
  saved: [{ en: 'B', note: '', ts: 2 }, { en: 'A|x', note: 'n', ts: 1 }],
  myVocab: [{ t: 'zeta', vi: 'z' }, { t: 'alpha', vi: 'a' }],
  standups: [{ date: '2026-09-20', score: 7 }],
  events: [{ id: 1, date: '2026-10-01', type: 'meeting', note: '' }],
  reports: [{ at: '2026-09-20T01:00:00Z', track: 'hotel', kind: 'vocab', type: 'Sai nghĩa', text: 'x' }],
  convos: [{ id: 5, name: 'Chat', score: 80, turns: [{ r: 'u', t: 'hi' }] }],
  photoLessons: [{ at: '2026-09-20', kind: 'email', summary: 'Mail', n: 3 }],
  customPack: { label: 'Nghề X', phases: [1] }, theme: 'dark',
  ai: { provider: 'gemini', key: 'SECRET', model: '' }, pendingJD: 'x'
});

t('toFlat bỏ key AI và cfg riêng máy', () => {
  const f = S.toFlat(store(), { coins: 5, cleared: [1, 2] });
  const s = JSON.stringify(f);
  assert.ok(!s.includes('SECRET') && !s.includes('pendingJD') && !s.includes('Samantha') && !s.includes('20:00'));
  assert.equal(f['srs|a%7Cb%25c'].reps, 2);
  assert.equal(f['tdays|hotel|done|2'], true);
  assert.deepEqual(f['tdays|hotel|focus'], ['p1']);
  assert.equal(f['tdays|it|cur'], 2);
  assert.equal(f['today|2026-09-20|vocab'], true);
  assert.ok(!('turns' in f['convos|5']));
  assert.equal(f['game|coins'], 5);
});

t('fromFlat ∘ toFlat = đồng nhất, giữ phần không đồng bộ', () => {
  const s0 = store(); const f = S.toFlat(s0, { coins: 5 });
  const s1 = { ai: s0.ai, cfg: { voiceName: 'Samantha', remind: '20:00' }, convos: [{ id: 5, turns: [{ r: 'u', t: 'hi' }] }], myVocab: [{ t: 'alpha' }, { t: 'zeta' }] };
  const game = S.fromFlat(f, s1, 'hotel');
  assert.deepEqual(S.toFlat(s1, game), f);
  assert.equal(s1.ai.key, 'SECRET');
  assert.equal(s1.cfg.voiceName, 'Samantha');
  assert.deepEqual(s1.convos[0].turns, [{ r: 'u', t: 'hi' }]);
  assert.deepEqual(s1.myVocab.map(x => x.t), ['alpha', 'zeta']); // giữ thứ tự cũ trên máy
  assert.deepEqual(s1.saved.map(x => x.en), ['B', 'A|x']);
  assert.deepEqual(s1.days, { done: { 1: true, 2: true }, cur: 3 });
  assert.deepEqual(Object.keys(s1.trackDays), ['it']);
});

t('fromFlat mở ngành khác: days/trackDays đổi chỗ', () => {
  const f = S.toFlat(store());
  const s = {}; S.fromFlat(f, s, 'it');
  assert.equal(s.days.cur, 2); assert.equal(s.trackDays.hotel.days.cur, 3); assert.equal(s.daysTrack, 'it');
});

t('diff: thêm / sửa / xoá kèm base', () => {
  const ops = S.diff({ a: 1, b: { x: 2 } }, { b: { x: 1 }, c: 3 });
  assert.deepEqual(ops, [{ p: 'a', v: 1 }, { p: 'b', v: { x: 2 }, b: { x: 1 } }, { p: 'c', d: true, b: 3 }]);
  assert.deepEqual(S.diff({ o: { a: 1, b: 2 } }, { o: { b: 2, a: 1 } }), []); // thứ tự khoá không tính
});

t('resolve giống SQL', () => {
  assert.equal(S.resolve('srs|x', { reps: 3, due: 1 }, { reps: 0, due: 9 }).reps, 3);
  assert.equal(S.resolve('srs|x', { reps: 1, due: 1 }, { reps: 1, due: 9 }).due, 9);
  assert.equal(S.resolve('hist|2026-09-20', 5, 2), 5);
  assert.equal(S.resolve('tdays|it|cur', 4, 7), 7);
  assert.equal(S.resolve('stats|done', 4, 7), 7);
  assert.equal(S.resolve('stats|lastDay', '2026-09-19', '2026-09-20'), '2026-09-20');
  assert.equal(S.resolve('cfg|level', 'A2', 'B1'), 'B1');
});

t('mergePull: máy không sửa → lấy server; cả hai sửa → luật gộp; máy mới thêm → giữ', () => {
  const shadow = { 'srs|a': { reps: 1 }, 'cfg|level': 'A2', 'hist|d': 2 };
  const local = { 'srs|a': { reps: 0, due: 1 }, 'cfg|level': 'A2', 'hist|d': 3, 'saved|new': { ts: 1 } };
  const server = { 'srs|a': { reps: 2, due: 5 }, 'cfg|level': 'B1', 'hist|d': 5, 'myVocab|w': { t: 'w' } };
  const r = S.mergePull(local, shadow, server);
  assert.equal(r.local['srs|a'].reps, 2);
  assert.equal(r.local['cfg|level'], 'B1');
  assert.equal(r.local['hist|d'], 5);
  assert.ok(r.local['saved|new'] && r.local['myVocab|w']);
  assert.deepEqual(r.shadow, server);
  // sau gộp, các thay đổi còn phải đẩy lên = chỉ phần máy có mà server chưa có
  assert.deepEqual(S.diff(r.local, r.shadow).map(o => o.p), ['saved|new']);
});

t('mergePull: xoá ở máy, server không đổi → vẫn xoá; server xoá, máy không sửa → xoá', () => {
  const r = S.mergePull({ 'b': 1 }, { 'a': 1, 'b': 1 }, { 'a': 1 });
  assert.deepEqual(r.local, {}); // b bị server xoá; a bị máy xoá
  assert.deepEqual(S.diff(r.local, r.shadow), [{ p: 'a', d: true, b: 1 }]);
});

t('mergePull tài khoản mới (shadow rỗng): gộp theo luật', () => {
  const r = S.mergePull({ 'srs|a': { reps: 5 }, 'x': 1 }, {}, { 'srs|a': { reps: 2 }, 'y': 2 });
  assert.equal(r.local['srs|a'].reps, 5); assert.equal(r.local.x, 1); assert.equal(r.local.y, 2);
});

t('mergePull account / device', () => {
  const a = S.mergePull({ x: 1 }, {}, { y: 2 }, 'account'); assert.deepEqual(a.local, { y: 2 });
  const d = S.mergePull({ x: 1 }, {}, { y: 2 }, 'device'); assert.deepEqual(d.local, { x: 1 });
  assert.deepEqual(S.diff(d.local, d.shadow).length, 2);
});

t('khoá dài: danh sách băm khoá, map bỏ qua; hôm nay không xoá ngày của máy khác', () => {
  const long = 'x'.repeat(300);
  const f = S.toFlat({ saved: [{ en: long, ts: 1 }], psrs: { ['y'.repeat(1000)]: { reps: 1 } } });
  const k = Object.keys(f).find(p => p.startsWith('saved|'));
  assert.ok(k.length < 260 && f[k].en === long);
  assert.ok(!Object.keys(f).some(p => p.startsWith('psrs|')));
  const s2 = { saved: [{ en: long, ts: 1, note: 'old' }] }; S.fromFlat(f, s2); assert.equal(s2.saved.length, 1); assert.equal(s2.saved[0].en, long);
  const ops = S.diff({ 'today|2026-09-21|vocab': true }, { 'today|2026-09-20|vocab': true, 'today|2026-09-10|x': true });
  assert.deepEqual(ops.map(o => o.p + (o.d ? ':del' : '')), ['today|2026-09-21|vocab', 'today|2026-09-10|x:del']);
});

t('fromFlat giữ ngày hôm nay của máy khi server có ngày khác', () => {
  const st = { today: { date: '2026-09-20', done: { vocab: true } } };
  S.fromFlat({ 'today|2026-09-20|vocab': true, 'today|2026-09-21|listen': true }, st);
  assert.deepEqual(st.today, { date: '2026-09-20', done: { vocab: true } });
  const st2 = {}; S.fromFlat({ 'today|2026-09-20|a': true, 'today|2026-09-21|b': true }, st2);
  assert.equal(st2.today.date, '2026-09-21');
});

console.log(`sync-core: ${n} tests passed`);
