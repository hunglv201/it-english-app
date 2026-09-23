# -*- coding: utf-8 -*-
"""v3.0 — sinh gói ngành: packs_src/<id>.py  ->  packs/<id>.gen.js (+ bản sao game/packs/).

Chạy:  python3 packs_src/build.py            # tất cả gói
       python3 packs_src/build.py hotel      # một gói
Mỗi file gói định nghĩa PACK (xem SCHEMA ở README trong thư mục này). Gói IT KHÔNG nằm ở đây:
IT vẫn là data.gen.js + phrases.gen.js + roles.gen.js (gen_data.py / phrases_data.py / roles_data.py).
Script kiểm tra chặt: sai cấu trúc -> dừng với thông báo rõ.
"""
import json, os, re, sys, shutil, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ORDER = ["office", "hotel", "sales", "factory", "logistics", "finance", "marketing", "health", "construction", "aviation"]

# nhóm "Câu thường dùng" chung cho mọi gói (lấy từ phrases_data.py, bỏ câu mang chất IT)
GENERIC_GROUPS = {
 "Chào hỏi & mở đầu ngày": None, "Hỏi xin giúp đỡ": None, "Đề nghị giúp & phản hồi": None,
 "Hỏi lại cho rõ (clarify)": None, "Đồng ý & không đồng ý": None, "Hỏi & báo trạng thái": None,
 "Báo blocker & trễ hạn": "Báo vướng mắc & trễ hạn", "Ước lượng & kế hoạch": "Kế hoạch & thời gian",
 "Họp — sắp xếp & điều phối": None, "Họp — trong cuộc họp": None, "Đề xuất ý tưởng": None,
 "Xin lỗi & nhận trách nhiệm": None, "Cảm ơn & ghi nhận": None, "Email & chat — mở & kết": None,
 "Xã giao & kết thúc ngày": None, "Học hỏi & phản hồi cá nhân": None,
}
IT_WORDS = re.compile(r"\b(code|coding|bug|bugs|deploy\w*|PR|PRs|merge\w*|API|APIs|server|staging|repo|repos|repositor\w*|commit\w*|test|tests|testing|build|builds|ticket|tickets|sprint|branch\w*|log|logs|database|DB|release|feature|features|prod|production|git|standup|stand-up|backend|frontend|blocker|blockers|blocked|Jira|debug\w*|refactor\w*|module|script|pipeline|QA|dev|devs|developer\w*|tech|technical|stack|endpoint|query|story points?|PM|pair|pairing|backlog|over-engineer\w*)\b", re.I)

def load_generic():
    spec = importlib.util.spec_from_file_location("phrases_data_src", os.path.join(ROOT, "phrases_data.py"))
    src = open(os.path.join(ROOT, "phrases_data.py"), encoding="utf-8").read()
    # chỉ lấy GROUPS, không chạy phần ghi file
    ns = {}
    code = src.split("\nimport json")[0] if "\nimport json" in src else src
    code = re.sub(r"\nopen\(.*$", "", code, flags=re.S)
    exec(compile(code, "phrases_data.py", "exec"), ns)
    out = []
    for name, pairs in ns["GROUPS"]:
        if name not in GENERIC_GROUPS: continue
        items = [{"en": en, "vi": vi} for en, vi in pairs if not IT_WORDS.search(en) and not IT_WORDS.search(vi)]
        out.append({"name": GENERIC_GROUPS[name] or name, "items": items})
    return out

def die(pid, msg):
    raise SystemExit("[%s] %s" % (pid, msg))

def norm(w):
    return re.sub(r"[^\w]", "", w.lower().replace("’", "'"))

def _mod(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def load(pid):
    P = _mod(os.path.join(HERE, pid + ".py"), "pack_" + pid).PACK
    # v4.1: nội dung làm giàu ở packs_src/extra/<id>.py (EXTRA). Chỉ NỐI THÊM vào cuối để không
    # xê dịch chỉ số ngày/từ/hội thoại cũ (tiến độ người học lưu theo số ngày).
    xp = os.path.join(HERE, "extra", pid + ".py")
    P["phases2"] = []
    if os.path.exists(xp):
        X = _mod(xp, "extra_" + pid).EXTRA
        P["phases2"] = list(X.get("phases", []))
        for k in ("rev", "reading", "ai", "quips"):
            P[k] = list(P[k]) + list(X.get(k, []))
        if X.get("events"):
            ev = list(P["events"]); tail = [e for e in ev if e[0] == "other"]
            P["events"] = [e for e in ev if e[0] != "other"] + list(X["events"]) + tail
        for rk, rx in (X.get("roles") or {}).items():
            if rk not in P["roles"]: die(pid, "extra.roles: vai %r không có trong gói" % rk)
            r = P["roles"][rk]
            r["scenarios"] = list(r["scenarios"]) + list(rx.get("scenarios", []))
            r["dialogues"] = list(r["dialogues"]) + list(rx.get("dialogues", []))
    return P

VI_DIACRITIC = re.compile(r"[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]", re.I)

def check_phase(pid, i, p):
    t = p.get("title") or die(pid, "phase %d thiếu title" % i)
    where = "%s (chặng %d)" % (t, i)
    if len(p["vocab"]) != 10: die(pid, where + ": cần đúng 10 từ, có %d" % len(p["vocab"]))
    for v in p["vocab"]:
        if len(v) not in (6, 8): die(pid, where + ": từ %r cần 6 hoặc 8 phần tử" % (v[0],))
        if not (v[1].startswith("/") and v[1].endswith("/")): die(pid, where + ": IPA của %r phải dạng /.../" % v[0])
        if "<b>" not in v[4]: die(pid, where + ": ví dụ của %r phải bọc từ bằng <b>…</b>" % v[0])
        if not VI_DIACRITIC.search(v[3] + v[5]): die(pid, where + ": nghĩa/ví dụ tiếng Việt của %r thiếu dấu?" % v[0])
    if len(p["phrases"]) < 8: die(pid, where + ": cần ≥ 8 câu (phrases), có %d" % len(p["phrases"]))
    if len(p["dialogues"]) != 5: die(pid, where + ": cần đúng 5 hội thoại, có %d" % len(p["dialogues"]))
    for them, opts in p["dialogues"]:
        if len(opts) != 3 or sum(1 for o in opts if o[1]) != 1: die(pid, where + ": hội thoại %r cần 3 lựa chọn, đúng 1 câu True" % them)
    if len(p["listen"]) != 6: die(pid, where + ": cần 6 bài nghe (4 câu + 2 đoạn), có %d" % len(p["listen"]))
    npass = 0
    for sent, blanks, hint in p["listen"]:
        words = sent.split()
        is_p = sum(1 for w in words if w[-1:] in ".?!") >= 2 or len(words) >= 15
        npass += is_p
        if is_p and len(blanks) != 3: die(pid, where + ": đoạn nghe cần đúng 3 ô trống: %r" % sent)
        if not is_p and not (1 <= len(blanks) <= 2): die(pid, where + ": câu nghe cần 1–2 ô trống: %r" % sent)
    if npass != 2: die(pid, where + ": cần đúng 2 đoạn nghe dài (2–3 câu), có %d" % npass)

def build_phase_pools(pid, phases, POOL):
    V, PH, DI, LI = POOL["vocab"], POOL["phrases"], POOL["dialogues"], POOL["listen"]
    idx = []
    for p in phases:
        vi = []
        for v in p["vocab"]:
            w = {"t": v[0], "ipa": v[1], "pos": v[2], "vi": v[3], "ex": v[4], "exVi": v[5]}
            if len(v) == 8 and v[6]: w["ja"] = v[6] + "|" + v[7]
            vi.append(len(V)); V.append(w)
        pi = []
        for ph in p["phrases"]:
            en, vn = ph[0], ph[1]; note = ph[2] if len(ph) > 2 else ""
            pi.append(len(PH)); PH.append({"en": en, "vi": vn, "note": note})
        di = []
        for them, opts in p["dialogues"]:
            o = [{"t": t, "good": g, "fb": f} for t, g, f in opts]
            gi = next(k for k, x in enumerate(o) if x["good"]); g = o.pop(gi); o.insert(len(DI) % 3, g)
            di.append(len(DI)); DI.append({"them": them, "opts": o})
        li = []
        for sent, blanks, hint in p["listen"]:
            words = sent.split(); bidx = []; used = set()
            for bw in blanks:
                for k, w in enumerate(words):
                    if k in used: continue
                    if norm(w) == norm(bw): bidx.append(k); used.add(k); break
                else:
                    die(pid, "không thấy từ trống %r trong câu nghe %r" % (bw, sent))
            it = {"s": words, "blank": bidx, "hint": hint}
            if sum(1 for w in words if w[-1:] in ".?!") >= 2 or len(words) >= 15: it["p"] = 1
            li.append(len(LI)); LI.append(it)
        idx.append((p["title"], vi, pi, di, li))
    return idx

def check_meta(pid, P):
    for k in ("id", "label", "short", "emoji", "desc", "persona", "counterpart", "context", "report", "podcast", "ai", "rev", "reading", "roles", "events", "quips", "phases", "jd_placeholder", "rw_placeholder", "reverse_tag", "game_tag"):
        if k not in P: die(pid, "PACK thiếu khoá %r" % k)
    r = P["report"]
    for k in ("title", "short", "sub", "steps", "kind", "structure", "sample"):
        if k not in r: die(pid, "report thiếu %r" % k)
    if len(r["steps"]) != 3: die(pid, "report.steps cần 3 bước")
    if len(P["ai"]) < 6: die(pid, "ai cần ≥ 6 tình huống")
    for k in ("ai", "rev", "quips"):
        keys = [x if isinstance(x, str) else x[0] for x in P[k]]
        d = sorted(set(x for x in keys if keys.count(x) > 1))
        if d: die(pid, "%s trùng: %r" % (k, d[:5]))
    ks = [x[0] for x in P["ai"]]
    for rv in P["roles"].values(): ks += ["r_" + x[0] for x in rv["scenarios"]]
    ek = [e[0] for e in P["events"]]
    for arr in (ks, ek):
        d = sorted(set(x for x in arr if arr.count(x) > 1))
        if d: die(pid, "khoá tình huống trùng: %r" % d[:5])
    if len(P["rev"]) < 10: die(pid, "rev cần ≥ 10 câu")
    if len(P["reading"]) < 4: die(pid, "reading cần ≥ 4 bài")
    for rd in P["reading"]:
        for q in rd["q"]:
            if len(q["o"]) != 3 or q["a"] not in (0, 1, 2): die(pid, "reading %r: mỗi câu hỏi 3 lựa chọn, a∈0..2" % rd["t"])
    if len(P["events"]) < 4: die(pid, "events cần ≥ 4 loại")
    if not (3 <= len(P["roles"]) <= 5): die(pid, "roles cần 3–5 vai")
    for rk, rv in P["roles"].items():
        if len(rv["scenarios"]) < 4: die(pid, "vai %s cần ≥ 4 tình huống" % rk)
        if len(rv["dialogues"]) < 6: die(pid, "vai %s cần ≥ 6 hội thoại" % rk)
        for them, opts in rv["dialogues"]:
            if len(opts) != 3 or sum(1 for o in opts if o[1]) != 1: die(pid, "vai %s: hội thoại %r cần 3 lựa chọn, 1 đúng" % (rk, them))

def build(pid, office=None):
    P = load(pid)
    if P["id"] != pid: die(pid, "PACK.id phải là %r" % pid)
    check_meta(pid, P)
    for i, p in enumerate(P["phases"] + P["phases2"]): check_phase(pid, i, p)
    own = P["phases"] + P["phases2"]
    seen = {}
    for p in own:
        for v in p["vocab"]:
            k = v[0].lower()
            if k in seen: die(pid, "từ vựng trùng %r (chặng %r và %r)" % (v[0], seen[k], p["title"]))
            seen[k] = p["title"]
    tt = [p["title"] for p in own]
    if len(set(tt)) != len(tt): die(pid, "tên chặng trùng")
    phases = list(P["phases"])
    core = P.get("core", [])
    if core and not os.path.exists(os.path.join(HERE, "office.py")):
        print("[%s] cảnh báo: chưa có office.py — tạm bỏ qua chặng lõi %r" % (pid, core)); core = []
    if core:
        if office is None: office = load("office")
        n = len(phases); half = (n + 1) // 2
        ins = [office["phases"][c] for c in core]
        # xen chặng lõi: một chặng giữa lộ trình, còn lại ở cuối
        phases = phases[:half] + ins[:1] + phases[half:] + ins[1:]
    phases += P["phases2"]   # chặng làm giàu: luôn ở cuối lộ trình
    POOL = {"vocab": [], "phrases": [], "dialogues": [], "listen": []}
    idx = build_phase_pools(pid, phases, POOL)
    DAYS = []
    for pi_, (title, vi, pi, di, li) in enumerate(idx):
        for dp in range(10):
            DAYS.append({"n": len(DAYS) + 1, "phase": pi_, "title": title,
                         "v": [vi[(dp * 3) % 10], vi[(dp * 3 + 1) % 10], vi[(dp * 3 + 2) % 10]],
                         "ph": pi[dp % len(pi)], "di": di[dp % len(di)], "li": li[dp % len(li)]})
    DATA = dict(POOL, days=DAYS, phaseTitles=[x[0] for x in idx])
    # Câu thường dùng: nhóm theo chặng của gói + nhóm chung
    groups = [{"name": p["title"], "items": [{"en": x[0], "vi": x[1]} for x in p["phrases"]]} for p in phases]
    groups += load_generic()
    ROLES = {}
    for n_, (rk, rv) in enumerate(P["roles"].items()):
        dl = []
        for j, (them, opts) in enumerate(rv["dialogues"]):
            o = [{"t": t, "good": g, "fb": f} for t, g, f in opts]
            gi = next(k for k, x in enumerate(o) if x["good"]); g = o.pop(gi); o.insert((j + n_) % 3, g)
            dl.append({"them": them, "opts": o})
        ROLES[rk] = {"label": rv["label"], "emoji": rv["emoji"],
                     "scenarios": [{"k": "r_" + k, "l": l, "s": s} for k, l, s in rv["scenarios"]], "dialogues": dl}
    META = {k: P[k] for k in ("id", "label", "short", "emoji", "desc", "persona", "counterpart", "context", "report", "podcast",
                              "rev", "reading", "quips", "jd_placeholder", "rw_placeholder", "reverse_tag", "game_tag")}
    META["ai"] = [{"k": k, "l": l, "s": s} for k, l, s in P["ai"]]
    META["events"] = [list(e) for e in P["events"]]
    js = ("/* gói " + pid + " — sinh bởi packs_src/build.py, KHÔNG sửa tay */\n"
          "window.PACK=" + json.dumps(META, ensure_ascii=False, separators=(",", ":")) + ";\n"
          "window.DATA=" + json.dumps(DATA, ensure_ascii=False, separators=(",", ":")) + ";\n"
          "window.PHRASES=" + json.dumps(groups, ensure_ascii=False, separators=(",", ":")) + ";\n"
          "window.ROLES=" + json.dumps(ROLES, ensure_ascii=False, separators=(",", ":")) + ";\n")
    os.makedirs(os.path.join(ROOT, "packs"), exist_ok=True)
    out = os.path.join(ROOT, "packs", pid + ".gen.js")
    open(out, "w", encoding="utf-8").write(js)
    if os.path.isdir(os.path.join(ROOT, "game")):
        os.makedirs(os.path.join(ROOT, "game", "packs"), exist_ok=True)
        shutil.copyfile(out, os.path.join(ROOT, "game", "packs", pid + ".gen.js"))
    print("%-8s phases %2d  days %3d  vocab %3d  dialogues %3d  listen %3d  phrases %4d  roles %d  %d KB"
          % (pid, len(idx), len(DAYS), len(POOL["vocab"]), len(POOL["dialogues"]), len(POOL["listen"]),
             sum(len(g["items"]) for g in groups), len(ROLES), len(js) // 1024))

if __name__ == "__main__":
    ids = sys.argv[1:] or [p for p in ORDER if os.path.exists(os.path.join(HERE, p + ".py"))]
    for pid in ids: build(pid)
    # packs/custom.js (viết tay) cũng cần ở game/packs/
    cj = os.path.join(ROOT, "packs", "custom.js")
    if os.path.exists(cj) and os.path.isdir(os.path.join(ROOT, "game")):
        shutil.copyfile(cj, os.path.join(ROOT, "game", "packs", "custom.js"))
