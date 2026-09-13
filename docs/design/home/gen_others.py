import re, json, random
css=open('_shared.css').read();hdr=open('_header.html').read();tabs=open('_tabs.html').read()
FONT='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Hanken+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap">'
CHEV='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#9aa1ad" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"></path></svg>'
CHEVW=CHEV.replace('#9aa1ad','#fff')
PLAY='<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M7 4l13 8-13 8z"></path></svg>'
P12=PLAY.replace('18','12'); P14=PLAY.replace('18','14'); P15=PLAY.replace('18','15'); P26=PLAY.replace('18','26')
MIC='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="3" width="6" height="11" rx="3"></rect><path d="M5 11a7 7 0 0 0 14 0"></path><path d="M12 18v3"></path></svg>'
SEND='<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M3 20l18-8L3 4v6l12 2-12 2z"></path></svg>'
CHECK='<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 13l4 4 10-11"></path></svg>'
TICKSM="<span class='tick on' style='width:24px;height:24px'>"+CHECK+"</span>"
BACK='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 6l-6 6 6 6"></path></svg>'
def tabs_on(label):
    t=tabs.replace('class="tab on"','class="tab"')
    return re.sub(r'<div class="tab">(<span class="ic">(?:(?!<div).)*?</span><b>'+label+'</b>)', r'<div class="tab on">\1', t, count=1, flags=re.S)
def sticky(inner,bottom=66):
    return f'<div style="position:absolute;left:0;right:0;bottom:{bottom}px;padding:12px 18px 10px;background:linear-gradient(180deg,rgba(245,246,248,0) 0%,#f5f6f8 30%)">{inner}</div>'
def subhdr(title,right=''):
    return f'<div class="top" style="padding:16px 18px 8px"><div style="display:flex;align-items:center;gap:10px"><div class="icobtn" style="width:36px;height:36px;border-radius:10px;color:#14161a">{BACK}</div><div class="disp" style="font-size:18px">{title}</div></div>{right}</div>'
def page(name,body,tab,header=None,extra_css='',stick=''):
    html=f'''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  {FONT}
  <style>
{css}
.phone{{height:844px;overflow:hidden}}
.main{{gap:14px}}
{extra_css}
  </style>
</helmet>
<div class="phone">
{header if header is not None else hdr}
<div class="main">
{body}
</div>
{stick}
{tab}
</div>
</x-dc>
</body>
</html>
'''
    open(name+'.dc.html','w').write(html)
def seg(items,on):
    out='<div style="display:flex;border:1px solid #e6e8ec;border-radius:11px;overflow:hidden;background:#fff">'
    for i,x in enumerate(items):
        st='background:#1b4dff;color:#fff' if i==on else 'color:#6b7280'
        br='' if i==len(items)-1 else ';border-right:1px solid #e6e8ec'
        out+=f'<div style="flex:1;height:40px;display:flex;align-items:center;justify-content:center;font-size:13.5px;font-weight:600;{st}{br}">{x}</div>'
    return out+'</div>'
def chips(items,on=0):
    inner=''.join(f'<span class="chip" style="height:36px;{"background:#1b4dff;color:#fff;border-color:#1b4dff" if i==on else ""}">{x}</span>' for i,x in enumerate(items))
    return f'<div style="position:relative;margin:0 -18px"><div style="display:flex;gap:8px;overflow-x:auto;padding:0 18px">{inner}</div><div style="position:absolute;right:0;top:0;bottom:0;width:40px;background:linear-gradient(90deg,rgba(245,246,248,0),#f5f6f8);pointer-events:none"></div></div>'
def prog(label,pct,right=''):
    return f'<div style="display:flex;flex-direction:column;gap:6px"><div style="display:flex;justify-content:space-between"><span class="muted" style="font-size:13.5px">{label}</span><span class="mono" style="font-size:12.5px;color:#6b7280">{right}</span></div><div class="bar" style="height:6px"><i style="width:{pct}%"></i></div></div>'
BIGPLAY=f'<div style="width:56px;height:56px;border-radius:16px;background:#1b4dff;color:#fff;display:flex;align-items:center;justify-content:center;margin:0 auto;box-shadow:0 10px 22px rgba(27,77,255,.3)">{PLAY}</div>'

# 1 Thẻ lật
grade=''
for t,d,s in [('Ôn lại','&lt;1 phút','background:#fbeeec;color:#c0392b'),('Khó','1 ngày','background:#fff;border:1px solid #e6e8ec;color:#14161a'),('Nhớ','3 ngày','background:#1b4dff;color:#fff'),('Dễ','7 ngày','background:#e9eeff;color:#1740d6')]:
    grade+=f'<div style="height:54px;border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;font-weight:700;font-size:14px;{s}"><span>{t}</span><small style="font-size:10.5px;font-weight:500;opacity:.75">{d}</small></div>'
body=f'''
{seg(['Thẻ lật','Kiểm tra','Danh sách'],0)}
{chips(['Tất cả','Của tôi','Hay sai','Git &amp; quản lý mã','Code review'])}
{prog('Thẻ 7 / 15',47,'Đã thuộc 128/370')}
<div class="card" style="text-align:center;gap:12px;padding:22px 18px 18px;flex-grow:1;justify-content:center">
  <div class="eyebrow">Thuật ngữ IT · v</div>
  <div class="disp" style="font-size:34px;line-height:1.05">rollback</div>
  <div class="mono" style="color:#6b7280;font-size:15px">/ˈrəʊlbæk/</div>
  {BIGPLAY}
  <div style="height:1px;background:#e6e8ec;margin:6px 0"></div>
  <div style="text-align:left;display:flex;flex-direction:column;gap:8px">
    <div class="disp" style="font-size:20px;line-height:1.25">quay lại bản trước</div>
    <div style="font-size:15px">If the deploy fails, we <span style="color:#1b4dff;font-weight:700">roll back</span>.</div>
    <div class="muted" style="font-size:13.5px">Nếu deploy lỗi thì mình quay lại bản cũ.</div>
  </div>
</div>
'''
page('TheLat',body,tabs_on('Từ vựng'),extra_css='.main{padding-bottom:150px}',stick=sticky(f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px">{grade}</div>'))

# 2 Kiểm tra
opts=''
for i,x in enumerate(['access','provision','storage','request']):
    sel=i==1
    opts+=f'<div style="min-height:56px;padding:14px 16px;border-radius:12px;border:1px solid {"#1b4dff" if sel else "#e6e8ec"};background:{"#e9eeff" if sel else "#fff"};font-size:16px;display:flex;align-items:center;justify-content:space-between"><span>{x}</span>{TICKSM if sel else ""}</div>'
body=f'''
{seg(['Thẻ lật','Kiểm tra','Danh sách'],1)}
{chips(['Tất cả','Của tôi','Hay sai','Git &amp; quản lý mã','Code review'])}
{prog('Câu 4 / 10',40,'Đúng 3')}
<div class="card" style="gap:6px;padding:18px"><div class="eyebrow">Từ tiếng Anh?</div><div class="disp" style="font-size:24px;line-height:1.2">cấp quyền / cung cấp</div><div class="muted" style="font-size:13.5px">Ví dụ: We need to ___ a new server.</div></div>
<div style="display:flex;flex-direction:column;gap:10px">{opts}</div>
<div style="display:flex;align-items:center;gap:8px;color:#1740d6;font-size:14px;font-weight:600">{CHECK} Đúng rồi · provision = cấp, cung cấp</div>
'''
page('KiemTra',body,tabs_on('Từ vựng'),extra_css='.main{padding-bottom:140px}',stick=sticky(f'<div class="btn">Câu tiếp {CHEVW}</div>'))

# 3 Câu
body=f'''
{prog('Câu 3 / 10',30,'Ngẫu nhiên · Deploy &amp; release')}
<div class="card" style="text-align:center;gap:12px;padding:24px 18px;flex-grow:1;justify-content:center">
  <div class="eyebrow">Deploy &amp; release</div>
  <div class="disp" style="font-size:24px;line-height:1.25">The deploy is delayed until Monday.</div>
  {BIGPLAY}
  <div style="height:1px;background:#e6e8ec"></div>
  <div class="disp" style="font-size:19px">Deploy bị hoãn tới thứ Hai.</div>
  <div style="display:flex;gap:8px;justify-content:center"><span class="chip" style="height:36px">Lưu câu</span><span class="chip" style="height:36px">Chép lại</span></div>
</div>
<div class="card" style="padding:12px 14px;gap:8px;background:#e9eeff;border-color:transparent;flex-direction:row;align-items:center">
  <div style="width:44px;height:44px;border-radius:12px;background:#1b4dff;color:#fff;display:flex;align-items:center;justify-content:center;flex:0 0 auto">{MIC}</div><div><b style="font-size:14.5px">Đọc theo để chấm</b><br><small class="muted" style="font-size:12.5px">Giữ để nói · chấm % giống câu mẫu</small></div>
</div>
'''
page('Cau',body,tabs_on('Câu'),header=subhdr('Câu thường dùng','<span class="chip" style="height:32px">Tự động</span>'),extra_css='.main{padding-bottom:140px}',stick=sticky(f'<div style="display:flex;gap:10px"><div class="btn ghost" style="flex:0 0 96px">Nghe lại</div><div class="btn">Câu tiếp {CHEVW}</div></div>'))

# 4 Giao tiếp
def bub(who,text,you=False):
    if you: return f'<div style="align-self:flex-end;max-width:85%"><div style="background:#1b4dff;color:#fff;padding:12px 15px;border-radius:14px;border-bottom-right-radius:4px;font-size:15px;line-height:1.45">{text}</div></div>'
    return f'<div style="align-self:flex-start;max-width:88%;display:flex;flex-direction:column;gap:4px"><span class="mono" style="font-size:11px;color:#9aa1ad;margin-left:6px">{who}</span><div style="display:flex;gap:8px;align-items:flex-end"><div style="background:#f0f2f5;border:1px solid #e6e8ec;padding:12px 15px;border-radius:14px;border-bottom-left-radius:4px;font-size:15px;line-height:1.45">{text}</div><div style="width:36px;height:36px;border-radius:10px;border:1px solid #e6e8ec;background:#fff;color:#1b4dff;display:flex;align-items:center;justify-content:center;flex:0 0 auto">{P14}</div></div></div>'
fix=f'<div style="background:#f7efdd;border-radius:12px;padding:12px 14px;display:flex;flex-direction:column;gap:6px"><div style="display:flex;justify-content:space-between;align-items:center"><span class="eyebrow" style="color:#a66a00">Sửa lỗi · 2</span><span class="chip" style="height:28px;font-size:12px;background:#fff">Lưu vào Của tôi</span></div><div style="font-size:14.5px"><span style="color:#c0392b;text-decoration:line-through">I fix</span> → <b>I fixed</b> <span class="muted" style="font-size:13px">(việc hôm qua, quá khứ)</span></div><div style="font-size:14.5px"><span style="color:#c0392b;text-decoration:line-through">will working</span> → <b>will work</b></div><div style="display:flex;align-items:center;gap:8px;font-size:13.5px;color:#1740d6;font-weight:600">{P14} Nghe câu đúng</div></div>'
body=f'''
<div style="display:flex;flex-direction:column;gap:12px;flex-grow:1">
{bub('Đồng nghiệp','Hi! What did you do yesterday, and what is your plan for today?')}
{bub('','Yesterday I fix the login bug and today I will working on payment API',True)}
{fix}
{bub('Đồng nghiệp','Nice, the payment API sounds interesting. Do you have any blockers right now?')}
</div>
<div class="muted" style="font-size:12.5px;text-align:center">Còn 2 lượt nữa để được chấm điểm cả buổi</div>
'''
inp=f'<div style="display:flex;flex-direction:column;gap:8px"><div style="display:flex;gap:8px;overflow-x:auto;margin:0 -18px;padding:0 18px"><span class="chip" style="height:34px">Gợi ý trả lời</span><span class="chip" style="height:34px">Đổi tình huống</span><span class="chip" style="height:34px">Lưu hội thoại</span></div><div style="display:flex;gap:8px;align-items:center"><div style="flex-grow:1;height:52px;border-radius:14px;border:1px solid #e6e8ec;background:#fff;display:flex;align-items:center;padding:0 15px;color:#9aa1ad;font-size:15px">Trả lời bằng tiếng Anh…</div><div style="width:52px;height:52px;border-radius:14px;border:1px solid #e6e8ec;background:#fff;color:#1b4dff;display:flex;align-items:center;justify-content:center">{MIC}</div><div style="width:52px;height:52px;border-radius:14px;background:#1b4dff;color:#fff;display:flex;align-items:center;justify-content:center">{SEND}</div></div></div>'
page('GiaoTiep',body,tabs_on('Giao tiếp'),header=subhdr('Standup','<span class="chip ok" style="height:32px">AI · Claude</span>'),extra_css='.main{padding-bottom:190px}',stick=sticky(inp))

# 5 Nghe
toks=''.join(f'<span class="mono" style="padding:7px 11px;border-radius:7px;font-size:13.5px;font-weight:500;{"background:#e9eeff;color:#1740d6" if ok else "background:#fbeeec;color:#c0392b"}">{w}</span>' for w,ok in [('Today',0),('I',0),('will',0),('work',0),('on',1),('the',0),('payment',0),('module',0)])
body=f'''
{seg(['Chép chính tả','Nhại theo'],0)}
{prog('Câu 1 / 148',1,'Nghe &amp; chép')}
<div class="card" style="align-items:center;gap:12px;padding:22px 18px">
  <div style="width:72px;height:72px;border-radius:20px;background:#1b4dff;color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 22px rgba(27,77,255,.3)">{P26}</div>
  <div style="display:flex;gap:8px"><span class="chip" style="height:34px">0.6× chậm</span><span class="chip ok" style="height:34px">1× thường</span><span class="chip" style="height:34px">Nghe 2 lần</span></div>
</div>
<div class="card" style="gap:10px">
  <div style="display:flex;justify-content:space-between;align-items:center"><span class="eyebrow">Đối chiếu · đúng 1/8 từ</span><span class="chip" style="height:28px;font-size:12px">Nghe lại</span></div>
  <div style="display:flex;flex-wrap:wrap;gap:8px">{toks}</div>
  <div class="muted" style="font-size:13px">Chữ đỏ là từ bạn nghe sót hoặc gõ sai. Thử lại lần 2 rồi hãy sang câu tiếp.</div>
</div>
'''
inp2=f'<div style="display:flex;flex-direction:column;gap:10px"><div style="display:flex;gap:8px;align-items:center"><div style="flex-grow:1;height:52px;border-radius:14px;border:1px solid #1b4dff;background:#fff;display:flex;align-items:center;padding:0 15px;font-size:15px">we deploy on friday</div><div style="width:52px;height:52px;border-radius:14px;border:1px solid #e6e8ec;background:#fff;color:#1b4dff;display:flex;align-items:center;justify-content:center">{MIC}</div></div><div style="display:flex;gap:10px"><div class="btn ghost" style="flex:0 0 110px">Thử lại</div><div class="btn">Câu tiếp {CHEVW}</div></div></div>'
page('Nghe',body,tabs_on('Nghe'),extra_css='.main{padding-bottom:190px}',stick=sticky(inp2))

# 6 Ngày
def step(n,title,sub,state):
    if state=='done': ic=f'<span class="tick on">{CHECK}</span>'; st=''
    elif state=='next': ic=f'<span class="tick next">{P12}</span>'; st='background:#e9eeff;margin:0 -8px;padding:14px 12px;border-radius:12px;border-bottom:none;'
    else: ic=f'<span class="tick mono" style="font-size:12px;font-weight:600">{n}</span>'; st=''
    col=';color:#9aa1ad' if state=='done' else ''
    return f'<div class="si" style="min-height:60px;{st}"><div style="display:flex;align-items:center;gap:12px">{ic}<span><b style="font-size:15px{col}">{title}</b><br><small class="muted" style="font-size:12.5px">{sub}</small></span></div>{CHEV}</div>'
body=f'''
<div style="padding:2px 2px 0"><div class="eyebrow">Chặng 2 · Git &amp; quản lý mã · ngày 2/10</div><div class="disp" style="font-size:24px;line-height:1.15;margin-top:3px">Ngày 12 · Merge &amp; conflict</div></div>
{prog('2/4 phần đã học',50,'khoảng 4 phút nữa')}
<div class="card" style="gap:0;padding:8px 18px">
{step(1,'Từ vựng · 3 từ','merge · conflict · resolve · đã nghe cả 3','done')}
{step(2,'Mẫu câu','"I got a merge conflict in main."','done')}
{step(3,'Hội thoại · chọn cách đáp','Any blockers today?','next')}
{step(4,'Nghe · điền từ trống','1 câu · 2 chỗ trống','todo')}
</div>
<div class="card" style="padding:12px 14px;flex-direction:row;align-items:center;justify-content:space-between"><div><b style="font-size:14.5px">Luyện thêm với AI</b><br><small class="muted" style="font-size:12.5px">Sinh ví dụ mới cho 3 từ hôm nay</small></div><span class="chip" style="height:34px">Sinh ví dụ</span></div>
'''
page('Ngay',body,tabs_on('Hôm nay'),header=subhdr('Lộ trình','<span class="mono" style="font-size:12px;color:#6b7280">12/370</span>'),extra_css='.main{padding-bottom:150px}',stick=sticky('<div class="btn" style="background:#e6e8ec;color:#9aa1ad;box-shadow:none">Hoàn thành ngày 12 · còn 2 phần</div><div class="muted" style="text-align:center;font-size:12px;margin-top:6px">Nút sáng lên khi học đủ 4 phần</div>'))

# 7 Thống kê
random.seed(3)
cells=''.join(f'<i style="aspect-ratio:1;border-radius:5px;background:{c};border:1px solid #eef0f3"></i>' for c in [random.choice(['#f0f2f5','#f0f2f5','#d2dbff','#a9b9ff','#6f8cff','#1b4dff']) for _ in range(28)])
wk=''.join(f'<span class="mono" style="font-size:10.5px;color:#9aa1ad;text-align:center">{d}</span>' for d in ['T2','T3','T4','T5','T6','T7','CN'])
weak=''.join(f'<div class="si" style="min-height:56px;padding:10px 4px"><div><b style="font-size:15px">{w}</b> <span class="mono" style="font-size:13px;color:#6b7280">{p}</span><br><small class="muted" style="font-size:12.5px">{v}</small></div><div style="width:40px;height:40px;border-radius:11px;border:1px solid #e6e8ec;background:#fff;color:#1b4dff;display:flex;align-items:center;justify-content:center">{P15}</div></div>' for w,p,v in [('rollback','/ˈrəʊlbæk/','quay lại bản trước'),('merge','/mɜːdʒ/','gộp nhánh'),('staging','/ˈsteɪdʒɪŋ/','môi trường thử')])
sw=lambda c:f'<i style="display:inline-block;width:9px;height:9px;border-radius:2px;background:{c};border:1px solid #eef0f3"></i>'
body=f'''
<div class="tiles" style="grid-template-columns:repeat(2,minmax(0,1fr))">
  <div class="tile"><div class="n" style="color:#1b4dff">5</div><div class="l">ngày liên tiếp</div></div>
  <div class="tile"><div class="n">128<span style="font-size:13px;color:#6b7280;font-weight:600">/370</span></div><div class="l">từ đã thuộc</div></div>
  <div class="tile"><div class="n">12<span style="font-size:13px;color:#6b7280;font-weight:600">/370</span></div><div class="l">ngày lộ trình</div></div>
  <div class="tile"><div class="n">412</div><div class="l">tổng lượt học</div></div>
</div>
<div class="card" style="gap:8px;padding:14px 18px">
  <div style="display:flex;justify-content:space-between;align-items:center"><span class="eyebrow">4 tuần gần đây</span><span class="muted" style="font-size:12px;display:flex;align-items:center;gap:3px">Ít {sw('#f0f2f5')}{sw('#a9b9ff')}{sw('#1b4dff')} Nhiều</span></div>
  <div style="display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:5px">{wk}{cells}</div>
</div>
<div class="card" style="gap:0;padding:12px 18px">
  <div style="display:flex;justify-content:space-between;align-items:center;padding-bottom:6px"><span class="eyebrow">Từ hay sai · 6</span><span class="chip ok" style="height:32px">Ôn ngay</span></div>
{weak}
</div>
'''
page('ThongKe',body,tabs_on('Hôm nay'),header=subhdr('Thống kê'),extra_css='.main{padding-bottom:120px}')

# 8 Cấu hình
def srow(label,val,chev=True):
    return f'<div class="si" style="min-height:52px;padding:11px 4px"><span style="font-size:15px">{label}</span><span style="display:flex;align-items:center;gap:6px;color:#6b7280;font-size:14px">{val}{CHEV if chev else ""}</span></div>'
def toggle(on):
    return f'<span style="width:46px;height:28px;border-radius:999px;background:{"#1b4dff" if on else "#e6e8ec"};position:relative;display:inline-block"><i style="position:absolute;top:3px;{"right:3px" if on else "left:3px"};width:22px;height:22px;border-radius:50%;background:#fff"></i></span>'
def group(title,rows):
    return f'<div class="card" style="gap:0;padding:6px 18px"><div class="eyebrow" style="padding:8px 0 4px">{title}</div>{rows}</div>'
body=f'''
{group('Đọc &amp; tự động',srow('Tự động đọc tiếng Anh',toggle(True),False)+srow('Tốc độ · giọng đọc','Vừa · Anh-Mỹ')+srow('Thời gian mỗi thẻ / câu','5s · 6s · 5s'))}
{group('Học tập',srow('Mục tiêu mỗi ngày','4 việc')+srow('Nhắc học hằng ngày','20:00')+srow('Giao diện','Theo hệ thống'))}
{group('AI &amp; dữ liệu',srow('Nhà cung cấp AI','Claude (trong app)')+srow('Sao lưu','JSON')+srow('Khôi phục','Từ file'))}
<div class="muted mono" style="text-align:center;font-size:11.5px">IT English · v1.5.0 · 2026-09-13</div>
'''
page('CauHinh',body,tabs_on('Hôm nay'),header=subhdr('Cấu hình'),extra_css='.main{padding-bottom:90px}')

c=json.load(open('canvas.json'))
c['pages']=[{"id":"page-1","name":"Hôm nay"},{"id":"page-2","name":"Các màn khác"}]
c['artboards']=[a for a in c['artboards'] if a.get('page')!='page-2']
c['annotations']=[n for n in c['annotations'] if n['id']!='note-others']
for a in c['artboards']: a['page']='page-1'
for n in c['annotations']: n['page']='page-1'
others=[('TheLat','Từ vựng · Thẻ lật'),('KiemTra','Từ vựng · Kiểm tra'),('Cau','Câu · phiên luyện'),('GiaoTiep','Giao tiếp · chat AI'),('Nghe','Nghe · chép chính tả'),('Ngay','Lộ trình · một ngày'),('ThongKe','Thống kê'),('CauHinh','Cấu hình')]
for i,(f,t) in enumerate(others):
    c['artboards'].append({"file":f+".dc.html","x":(i%4)*480,"y":(i//4)*1000,"w":390,"h":844,"title":t,"page":"page-2"})
c['annotations'].append({"id":"note-others","x":0,"y":-170,"w":900,"page":"page-2","text":"CÁC MÀN KHÁC · cùng nguyên tắc mobile-first:\n• Hành động chính ghim trên tab bar (chấm thẻ, câu tiếp, gửi, hoàn thành ngày).\n• Nội dung chính vừa 1 màn 390×844, không phải cuộn để thấy nút.\n• Chip chủ đề có fade mép phải; hàng chạm ≥52px; ô nhập 52px.\n• Chat: thẻ sửa lỗi nổi, nhiều lỗi, nút nghe câu đúng, báo còn mấy lượt được chấm.\n• Ngày lộ trình: 4 phần dạng bước, nút hoàn thành chỉ sáng khi đủ 4/4."})
c['launch']={"view":"canvas","page":"page-2"}
json.dump(c,open('canvas.json','w'),ensure_ascii=False,indent=1)
print('done')
