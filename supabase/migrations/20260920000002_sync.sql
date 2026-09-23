-- Nói Nghề v4.0 · 0002 — đồng bộ theo thay đổi (outbox) + gộp khi 2 máy cùng sửa
-- Client gửi lô thay đổi: [{p: path, v: value | d: true (xoá), b: value lúc client đọc lần cuối (null = chưa có)}]
-- Path: các đoạn nối bằng '|' (client đã mã hoá '|' và '%' trong khoá). Đoạn đầu = nhóm dữ liệu:
--   cfg|k · stats|k · srs|từ · psrs|câu · hist|ngày · tdays|ngành|done|n · tdays|ngành|cur · today|ngày|việc
--   saved|câu · myVocab|từ · standups|ngày · events|id · reports|at · convos|id · photos|khoá · game|k · customPack · theme …
-- Không xung đột (giá trị server = b) → áp thẳng. Xung đột (máy khác đã sửa) → nn_resolve (giống hệt cloud.js).

create or replace function public.nn_num(x jsonb) returns numeric
language sql immutable as $$
  select case when jsonb_typeof(x) = 'number' then (x #>> '{}')::numeric else null end
$$;

-- luật gộp khi cả server (e) và client (v) đều có giá trị mới cho cùng path
create or replace function public.nn_resolve(p text, e jsonb, v jsonb) returns jsonb
language plpgsql immutable as $$
declare top text := split_part(p, '|', 1);
        er numeric; vr numeric;
begin
  if e is null then return v; end if;
  if v is null then return e; end if;
  if top in ('srs', 'psrs') then          -- thẻ ôn: giữ bản ôn nhiều lần hơn; hoà → hạn ôn muộn hơn
    er := coalesce(public.nn_num(e->'reps'), 0); vr := coalesce(public.nn_num(v->'reps'), 0);
    if vr > er then return v; end if;
    if vr < er then return e; end if;
    if coalesce(public.nn_num(v->'due'), 0) >= coalesce(public.nn_num(e->'due'), 0) then return v; end if;
    return e;
  elsif top = 'hist' or (top = 'stats' and public.nn_num(e) is not null and public.nn_num(v) is not null)
        or (top = 'tdays' and split_part(p, '|', 3) = 'cur') then
    return to_jsonb(greatest(coalesce(public.nn_num(e), 0), coalesce(public.nn_num(v), 0)));
  end if;
  return v;   -- mặc định: bản ghi sau thắng
end $$;

create or replace function public.nn_ver(v text) returns int[]
language sql immutable as $$
  select array(select coalesce(nullif(regexp_replace(x, '\D', '', 'g'), ''), '0')::int
               from unnest(string_to_array(split_part(coalesce(v, '0'), '-', 1), '.')) x)
$$;

create or replace function public.apply_changes(p_id text, p_changes jsonb, p_base_rev bigint default null, p_app_version text default null)
returns jsonb
language plpgsql security definer set search_path = public as $$
declare
  uid uuid := auth.uid();
  st jsonb; r bigint; prev bigint;
  c jsonb; p text; cur jsonb; nv jsonb; fin jsonb; isdel boolean;
  vals jsonb := '{}'::jsonb;
  minv text; trk text; seg text[];
  ok_v int := 0; fail_v int := 0; ok_p int := 0; fail_p int := 0;
  n int;
begin
  if uid is null then raise exception 'not_authenticated' using errcode = '28000'; end if;
  if p_id is null or length(p_id) > 64 then raise exception 'bad_change_id'; end if;
  if jsonb_typeof(p_changes) <> 'array' then raise exception 'bad_changes'; end if;
  n := jsonb_array_length(p_changes);
  if n > 300 then raise exception 'too_many_changes'; end if;
  select value #>> '{}' into minv from app_config where key = 'min_app_version';
  if p_app_version is not null and minv is not null and public.nn_ver(p_app_version) < public.nn_ver(minv) then
    return jsonb_build_object('error', 'update_required', 'min', minv);
  end if;

  insert into user_state (user_id) values (uid) on conflict do nothing;
  select state, rev into st, r from user_state where user_id = uid for update;
  prev := r;

  -- lô đã áp trước đó (client gửi lại vì mất phản hồi) → trả giá trị hiện tại, không áp lần 2
  if exists (select 1 from applied_changes a where a.user_id = uid and a.change_id = p_id) then
    for c in select * from jsonb_array_elements(p_changes) loop
      p := c->>'p'; vals := vals || jsonb_build_object(p, st->p);
    end loop;
    return jsonb_build_object('rev', r, 'prev', r, 'dup', true, 'vals', vals);
  end if;

  for c in select * from jsonb_array_elements(p_changes) loop
    p := c->>'p';
    if p is null or p = '' then continue; end if;
    cur := st->p;
    if length(p) > 1000 then vals := vals || jsonb_build_object(p, cur); continue; end if;   -- bỏ qua nhưng trả giá trị hiện tại
    isdel := coalesce(c->'d' = 'true'::jsonb, false);
    nv := case when isdel then null else c->'v' end;
    if nv = 'null'::jsonb then nv := null; isdel := true; end if;
    if cur is not distinct from (case when c->'b' = 'null'::jsonb then null else c->'b' end) then
      fin := nv;                                -- không xung đột
    elsif isdel then
      fin := cur;                               -- máy khác vừa sửa → giữ, không xoá
    else
      fin := public.nn_resolve(p, cur, nv);     -- cả hai cùng sửa → luật gộp
    end if;
    if fin is null then st := st - p; else st := st || jsonb_build_object(p, fin); end if;
    vals := vals || jsonb_build_object(p, fin);

    -- suy ra bảng thống kê (lỗi ở đây không được làm hỏng cả lô)
    seg := string_to_array(p, '|');
    begin
    if seg[1] = 'tdays' and seg[3] = 'done' and seg[4] ~ '^\d{1,4}$' then
      if fin is null then delete from user_days where user_id = uid and track = seg[2] and day = seg[4]::int;
      else insert into user_days (user_id, track, day) values (uid, left(seg[2], 32), seg[4]::int) on conflict do nothing; end if;
    elsif seg[1] = 'hist' and seg[2] ~ '^\d{4}-\d{2}-\d{2}$' and public.nn_num(fin) is not null then
      trk := left(coalesce(st->>'cfg|track', 'office'), 32);
      insert into daily_activity (user_id, day, track, tasks) values (uid, seg[2]::date, trk, least(public.nn_num(fin), 100000)::int)
        on conflict (user_id, day) do update set tasks = greatest(daily_activity.tasks, excluded.tasks), track = excluded.track;
    elsif seg[1] in ('srs', 'psrs') and fin is not null and fin is distinct from cur then
      if coalesce(public.nn_num(fin->'reps'), 0) > coalesce(public.nn_num(cur->'reps'), 0) then
        if seg[1] = 'srs' then ok_v := ok_v + 1; else ok_p := ok_p + 1; end if;
      elsif coalesce(public.nn_num(fin->'reps'), 0) = 0 and cur is not null then
        if seg[1] = 'srs' then fail_v := fail_v + 1; else fail_p := fail_p + 1; end if;
      end if;
    end if;
    exception when others then null;
    end;
  end loop;

  if pg_column_size(st) > 2000000 then raise exception 'state_too_large'; end if;   -- huỷ cả lô (kể cả bảng thống kê)
  if ok_v + fail_v > 0 then
    insert into attempts_daily (user_id, day, kind, ok, fail) values (uid, current_date, 'vocab', ok_v, fail_v)
      on conflict (user_id, day, kind) do update set ok = attempts_daily.ok + excluded.ok, fail = attempts_daily.fail + excluded.fail;
  end if;
  if ok_p + fail_p > 0 then
    insert into attempts_daily (user_id, day, kind, ok, fail) values (uid, current_date, 'phrase', ok_p, fail_p)
      on conflict (user_id, day, kind) do update set ok = attempts_daily.ok + excluded.ok, fail = attempts_daily.fail + excluded.fail;
  end if;

  r := r + 1;
  update user_state set state = st, rev = r, updated_at = now(), app_version = left(p_app_version, 20) where user_id = uid;
  insert into applied_changes (user_id, change_id) values (uid, p_id);
  update profiles set last_seen_at = now(),
         track = coalesce(left(st->>'cfg|track', 32), track),
         role = coalesce(left(st->>'cfg|role', 32), role),
         level = coalesce(left(st->>'cfg|level', 8), level)
   where id = uid;
  if random() < 0.05 then delete from applied_changes where user_id = uid and at < now() - interval '180 days'; end if;
  return jsonb_build_object('rev', r, 'prev', prev, 'vals', vals);
end $$;

create or replace function public.get_state()
returns jsonb
language sql stable security definer set search_path = public as $$
  select coalesce((select jsonb_build_object('rev', s.rev, 'state', s.state, 'updated_at', s.updated_at)
                     from user_state s where s.user_id = auth.uid()),
                  jsonb_build_object('rev', 0, 'state', '{}'::jsonb))
$$;

create or replace function public.get_rev()
returns bigint
language sql stable security definer set search_path = public as $$
  select coalesce((select rev from user_state where user_id = auth.uid()), 0)
$$;

revoke all on function public.apply_changes(text, jsonb, bigint, text) from public, anon;
revoke all on function public.get_state() from public, anon;
revoke all on function public.get_rev() from public, anon;
revoke all on function public.nn_resolve(text, jsonb, jsonb) from anon;
revoke all on function public.nn_ver(text) from anon;
revoke all on function public.nn_num(jsonb) from anon;
grant execute on function public.apply_changes(text, jsonb, bigint, text) to authenticated;
grant execute on function public.get_state() to authenticated;
grant execute on function public.get_rev() to authenticated;
