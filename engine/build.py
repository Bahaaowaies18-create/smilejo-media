import os, subprocess, sys
from playwright.sync_api import sync_playwright
import os as _os
ENG=_os.path.dirname(_os.path.abspath(__file__))+'/'
SP=ENG
A=ENG+'assets/'
F=ENG+'fonts/'
OUT=ENG+'out/'
os.makedirs(OUT,exist_ok=True)
LOGO=f"file://{ENG}assets/logo-crop.png"
MED="الخدمات العلاجية في الزرقاء والشميساني تحت إشراف أطباء متخصصين"
VMED="حل تجميلي متحرك، مش بديل دائم عن العلاج"

CSS=f"""
@font-face{{font-family:NA;src:url('file://{F}NotoSansArabic-Bold.ttf');font-weight:700}}
@font-face{{font-family:NA;src:url('file://{F}NotoSansArabic-SemiBold.ttf');font-weight:600}}
@font-face{{font-family:NA;src:url('file://{F}NotoSansArabic-Regular.ttf');font-weight:400}}
:root{{--blue:#014FC9;--yellow:#F9C03C;--dark:#23232A;--white:#F7F7F7;--muted:#B9BCC8;--night:#0B2F6E;--card:#2E2E36}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden}}
body{{background:var(--dark);color:var(--white);font-family:NA,Inter,'Noto Color Emoji',sans-serif;position:relative}}
.abs{{position:absolute}}
.lat{{font-family:Inter,NA;direction:ltr;unicode-bidi:isolate}}
.tag{{position:absolute;top:150px;left:72px;font-size:26px;color:var(--muted);background:#0006;padding:6px 18px;border-radius:999px;z-index:50}}
.end{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 90px 240px;background:radial-gradient(circle at 50% 38%,var(--night) 0%,var(--dark) 64%);z-index:40}}
.end img{{width:330px}}
.end .t{{font-weight:700;font-size:66px;line-height:1.35;margin-top:34px}}
.end .s{{font-size:40px;line-height:1.55;color:var(--white);opacity:.9;margin-top:22px}}
.pill{{margin-top:48px;background:var(--yellow);color:var(--dark);font-family:Inter;font-weight:800;font-size:54px;padding:20px 60px;border-radius:999px;direction:ltr}}
.fine{{position:absolute;bottom:300px;left:80px;right:80px;text-align:center;font-size:25px;color:var(--muted);line-height:1.5}}
@keyframes fin{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes fout{{from{{opacity:1}}to{{opacity:0}}}}
@keyframes up{{from{{opacity:0;transform:translateY(60px)}}to{{opacity:1;transform:none}}}}
@keyframes upout{{from{{opacity:1;transform:none}}to{{opacity:0;transform:translateY(-60px)}}}}
@keyframes pop{{0%{{opacity:0;transform:scale(.6)}}70%{{opacity:1;transform:scale(1.06)}}100%{{opacity:1;transform:scale(1)}}}}
@keyframes kb{{from{{transform:scale(1)}}to{{transform:scale(1.14)}}}}
@keyframes grow{{from{{max-height:0;opacity:0;margin-top:0;transform:scale(.85)}}to{{max-height:340px;opacity:1;margin-top:22px;transform:none}}}}
@keyframes shrink{{from{{max-height:200px;opacity:1;margin-top:22px}}to{{max-height:0;opacity:0;margin-top:0}}}}
@keyframes dot{{0%,100%{{opacity:.3;transform:translateY(0)}}50%{{opacity:1;transform:translateY(-8px)}}}}
@keyframes bar{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
@keyframes dim{{from{{filter:none;opacity:1}}to{{filter:grayscale(.7) brightness(.45);opacity:.8}}}}
@keyframes undim{{from{{filter:grayscale(.7) brightness(.45);opacity:.8}}to{{filter:none;opacity:1}}}}
"""
def an(*parts): return "animation:"+",".join(parts)
def html(body,extra=""):
    return f"<html dir='rtl'><head><meta charset='utf-8'><style>{CSS}{extra}</style></head><body>{body}</body></html>"
def endcard(t0,title,sub,fine,episode=""):
    ep=f"<div class='s' style='font-size:32px;color:var(--muted);margin-top:30px'>{episode}</div>" if episode else ""
    return f"""<div class='end' style='{an(f"fin .5s ease {t0}s both")}'>
<img src='{LOGO}' style='{an(f"pop .7s ease {t0+.2}s both")}'>
<div class='t' style='{an(f"up .6s ease {t0+.4}s both")}'>{title}</div>
<div class='s' style='{an(f"up .6s ease {t0+.7}s both")}'>{sub}</div>
<div class='pill' style='{an(f"pop .6s ease {t0+1.0}s both")}'>smilejo.shop</div>{ep}
<div class='fine' style='{an(f"fin .5s ease {t0+1.2}s both")}'>{fine}</div></div>"""

# ---------------- REEL 1: chat story ----------------
R1X="""
.hook{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 80px 160px;z-index:30;background:var(--dark)}
.hook .a{font-weight:700;font-size:132px;color:var(--yellow);line-height:1.2}
.hook .b{font-weight:700;font-size:62px;line-height:1.4;margin-top:26px}
.chat{position:absolute;top:250px;left:56px;right:56px;height:1280px;background:#1B1B21;border-radius:52px;overflow:hidden;box-shadow:0 40px 90px #0009;display:flex;flex-direction:column}
.hd{height:150px;background:var(--card);display:flex;align-items:center;gap:26px;padding:0 40px;flex:none}
.av{width:92px;height:92px;border-radius:50%;background:var(--blue);display:flex;align-items:center;justify-content:center;font-size:48px}
.hd .n{font-weight:700;font-size:44px}.hd .m{font-size:27px;color:var(--muted);margin-top:2px}
.msgs{flex:1;display:flex;flex-direction:column;justify-content:flex-end;padding:0 34px 44px;overflow:hidden}
.b{max-width:780px;padding:20px 30px 16px;border-radius:34px;font-size:42px;line-height:1.45;overflow:hidden}
.me{align-self:flex-end;background:var(--blue);border-bottom-left-radius:10px}
.ot{align-self:flex-start;background:#3A3A44;border-bottom-right-radius:10px}
.nm{font-size:27px;font-weight:700;color:#8FB6FF;margin-bottom:2px}
.tm{font-family:Inter;font-size:22px;color:#ffffffa0;text-align:left;margin-top:4px;direction:ltr}
.typ{display:flex;gap:12px;padding:30px 34px}
.typ i{width:18px;height:18px;border-radius:50%;background:var(--muted);display:block}
"""
def bub(t,who,text,me=False,tm="9:41 PM"):
    nm="" if me else f"<div class='nm'>{who}</div>"
    return f"<div class='b {'me' if me else 'ot'}' style='{an(f'grow .45s cubic-bezier(.2,.9,.3,1.2) {t}s both')}'>{nm}{text}<div class='tm'>{tm}</div></div>"
msgs=[(2.7,"أحمد","يابا ليش ما أكلت من المنسف؟ 😅",True),
(4.0,"أبو أحمد","مش جوعان",False),
(5.3,"أم أحمد","كل عزومة نفس الحكي… صار يمضغ على جهة وحدة",False),
(7.2,"أحمد","يابا خليني أحجزلك فحص واستشارة، ببلاش",True),
(8.9,"أبو أحمد","بلاش غلبة يابا",False),
(10.3,"أحمد","حجزتلك 📅 الخميس، فرع الزرقاء",True)]
TMS=["9:41 PM","9:41 PM","9:42 PM","9:43 PM","9:43 PM","9:45 PM"]
b1="".join(bub(t,w,x,m,TMS[i]) for i,(t,w,x,m) in enumerate(msgs))
typ=f"<div class='b ot typ' style='{an('grow .35s ease 11.7s both','shrink .25s ease 12.9s forwards')}'>"+"".join(f"<i style='{an(f'dot .9s ease {11.7+k*.15}s infinite')}'></i>" for k in range(3))+"</div>"
b1+=typ+bub(13.1,"أبو أحمد","ماشي… عشان خاطرك بس 🙂",False,"9:47 PM")
R1=html(f"""<div class='tag'>قصة تمثيلية</div>
<div class='hook' style='{an("fout .45s ease 2.1s forwards")}'><div class='a'>«مش جوعان»</div><div class='b'>أكثر جملة بنسمعها<br>بعزايم العيلة 😅</div></div>
<div class='chat' style='{an("up .6s ease 2.0s both")}'>
<div class='hd'><div class='av'>🏠</div><div><div class='n'>العيلة</div><div class='m'>أبو أحمد، أم أحمد، أحمد</div></div></div>
<div class='msgs'>{b1}</div></div>
{endcard(15.0,"في ناس بنحبهم بيخبّوا إشي<br>ورا «مش جوعان»","ابعتها لحدا بالعيلة لازم يشوفها 🤍",MED+"<br>فحص واستشارة مجانية · الزرقاء | الشميساني","الحلقة الجاية: شو صار مع أبو أحمد بالاستشارة")}
""",R1X)

# ---------------- REEL 2: veneer FAQ ----------------
R2X=f"""
.bg{{position:absolute;inset:0;background:url('file://{A}service-veneer.webp') center 22%/cover}}
.sh{{position:absolute;inset:0;background:linear-gradient(180deg,#23232A66 0%,#23232A33 30%,#23232AEE 58%,#23232A 100%)}}
.hk{{position:absolute;left:80px;right:80px;top:820px;text-align:center}}
.hk .a{{font-weight:700;font-size:150px;color:var(--yellow);line-height:1}}
.hk .b{{font-weight:700;font-size:70px;line-height:1.35;margin-top:20px}}
.card{{position:absolute;left:64px;right:64px;top:930px;background:#1B1B21E8;border-radius:44px;padding:50px 56px 56px;box-shadow:0 30px 80px #000a}}
.chip{{display:inline-block;background:var(--blue);color:#fff;font-weight:700;font-size:32px;padding:8px 28px;border-radius:999px}}
.q{{font-weight:700;font-size:72px;line-height:1.3;margin-top:26px}}
.al{{font-weight:700;font-size:32px;color:var(--yellow);margin-top:36px}}
.a{{font-size:46px;line-height:1.55;margin-top:6px}}
.prog{{position:absolute;top:880px;left:64px;right:64px;display:flex;gap:14px}}
.prog div{{flex:1;height:8px;border-radius:8px;background:#ffffff30;overflow:hidden}}
.prog span{{display:block;height:100%;background:var(--white);transform-origin:right;transform:scaleX(0)}}
"""
qa=[(2.6,"بيحتاج برد لسناني؟","غالباً لا. والقرار النهائي بيكون بعد فحص الحالة."),
(6.8,"بقدر آكل وأنا لابسته؟","بيعتمد على التصميم وحالتك. وبتاخذي تعليمات الاستخدام والعناية وقت الاستلام."),
(11.0,"هو حل دائم؟","لأ، هو حل تجميلي متحرك.<br>ولما تكوني جاهزة، في خيارات ثابتة.")]
cards=""; prog=""
for i,(t,q,a) in enumerate(qa):
    out=f",upout .4s ease {t+3.85}s forwards"
    cards+=f"""<div class='card' style='{an(f"up .5s ease {t}s both")}{out}'>
<span class='chip'>سؤال {i+1} من 3</span><div class='q'>{q}</div>
<div class='al' style='{an(f"fin .3s ease {t+1.2}s both")}'>الجواب</div>
<div class='a' style='{an(f"up .45s ease {t+1.3}s both")}'>{a}</div></div>"""
    prog+=f"<div><span style='{an(f'bar 4.2s linear {t}s both')}'></span></div>"
R2=html(f"""<div class='bg' style='{an("kb 19s linear 0s both")}'></div><div class='sh'></div>
<div class='tag'>صورة تمثيلية</div>
<div class='hk' style='{an("upout .45s ease 2.2s forwards")}'><div class='a lat'>3</div><div class='b'>أسئلة بتخجلي تسأليها<br>عن الفنير المتحرك</div></div>
<div class='prog' style='{an("fin .4s ease 2.5s both")}'>{prog}</div>
{cards}
{endcard(15.2,"احفظي الفيديو<br>لوقت ما تحتاجيه 🔖","وأي سؤال ثاني، اسألينا بالكومنتات",VMED+"<br>📍 الزرقاء | الشميساني")}
""",R2X)

# ---------------- REEL 3: zirconia vs E.max ----------------
R3X=f"""
.ph{{position:absolute;top:250px;width:462px;height:760px;border-radius:40px;overflow:hidden;box-shadow:0 30px 70px #0009}}
.ph img{{width:100%;height:100%;object-fit:cover}}
.ph .lb{{position:absolute;bottom:22px;right:22px;background:#000b;padding:6px 24px;border-radius:999px;font-weight:700;font-size:36px}}
.z{{right:64px}} .e{{left:64px}}
.hk{{position:absolute;left:70px;right:70px;top:1080px;text-align:center}}
.hk .a{{font-weight:700;font-size:96px;line-height:1.25}}
.hk .b{{font-size:44px;color:var(--muted);margin-top:16px}}
.tx{{position:absolute;left:72px;right:72px;top:1080px}}
.tx .k{{display:inline-block;background:var(--blue);color:#fff;font-weight:700;font-size:34px;padding:8px 28px;border-radius:999px}}
.tx .h{{font-weight:700;font-size:76px;line-height:1.3;margin-top:22px}}
.tx .d{{font-size:44px;line-height:1.55;margin-top:14px;opacity:.92}}
.who{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 90px 220px;background:var(--dark);z-index:20}}
.who .q{{font-weight:700;font-size:100px}}
.who .a{{font-weight:700;font-size:64px;line-height:1.45;margin-top:40px}}
.who .y{{color:var(--yellow)}}
"""
R3=html(f"""<div class='tag' style='top:150px'>صور توضيحية</div>
<div class='ph z' style='{an("dim .4s ease 7.0s forwards","undim .4s ease 11.3s forwards")}'><img src='file://{A}service-zirconia.webp' style='object-position:30% center'><span class='lb'>زيركون</span></div>
<div class='ph e' style='{an("dim .4s ease 2.6s both","undim .4s ease 7.0s forwards")}'><img src='file://{A}service-emax.webp' style='object-position:center 55%'><span class='lb lat'>E.max</span></div>
<div class='hk' style='{an("upout .4s ease 2.2s forwards")}'><div class='a'>زيركون ولا <span class='lat' style='color:var(--yellow)'>E.max</span>؟</div><div class='b'>الفرق بينهم بأقل من دقيقة</div></div>
<div class='tx' style='{an("up .5s ease 2.6s both","upout .4s ease 6.8s forwards")}'><span class='k'>زيركون</span>
<div class='h'>تركيبة ثابتة</div><div class='d'>بتجمع بين المتانة والمظهر الطبيعي.</div></div>
<div class='tx' style='{an("up .5s ease 7.2s both","upout .4s ease 11.2s forwards")}'><span class='k lat'>E.max</span>
<div class='h'>شفافية عالية</div><div class='d'>خيار تجميلي للقشور والتيجان حسب الحالة.</div></div>
<div class='who' style='{an("fin .45s ease 11.6s both")}'><div class='q' style='{an("pop .6s ease 11.8s both")}'>طيب مين بيقرر؟</div>
<div class='a' style='{an("up .5s ease 12.9s both")}'>الطبيب، بعد الفحص.<br><span class='y'>والاستشارة مجانية.</span></div></div>
{endcard(15.4,"ابعتها لحدا<br>محتار بين الاثنين","فحص واستشارة مجانية بالزرقاء والشميساني",MED)}
""",R3X)

REELS=[("reel-1-abu-ahmad",R1,19.0),("reel-2-veneer-faq",R2,19.0),("reel-3-zircon-emax",R3,19.0)]
FPS=30
def render_reel(pg,name,doc,dur):
    p=OUT+name+'.html'; open(p,'w').write(doc)
    pg.goto('file://'+p); pg.wait_for_timeout(800)
    ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate',str(FPS),'-c:v','mjpeg','-i','-',
        '-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest','-map','0:v','-map','1:a',
        '-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r',str(FPS),'-c:a','aac','-b:a','64k','-movflags','+faststart',OUT+name+'.mp4'],stdin=subprocess.PIPE)
    n=int(dur*FPS)
    for i in range(n):
        pg.evaluate("t=>{document.getAnimations().forEach(a=>{a.pause();a.currentTime=t})}",i*1000/FPS)
        ff.stdin.write(pg.screenshot(type='jpeg',quality=93))
    ff.stdin.close(); ff.wait()

def still(pg,name,doc,t=None):
    p=OUT+name+'.html'; open(p,'w').write(doc)
    pg.goto('file://'+p); pg.wait_for_timeout(800)
    if t is not None: pg.evaluate("t=>{document.getAnimations().forEach(a=>{a.pause();a.currentTime=t})}",t*1000)
    pg.screenshot(path=OUT+name+'.jpg',type='jpeg',quality=93)

if __name__=='__main__':
    which=sys.argv[1:] or ['reels','stories']
    exec(open(ENG+'stories.py').read())
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
        if 'preview' in which:
            for name,doc,dur in REELS:
                for t in [0,3.5,7.5,10,12.5,14,17.5]: still(pg,f'{name}-t{t}',doc,t)
        if 'reels' in which:
            for name,doc,dur in REELS: render_reel(pg,name,doc,dur); print('done',name,flush=True)
        if 'stories' in which or 'preview' in which:
            for name,doc in STORIES: still(pg,name,doc)
            for name,doc in COVERS: still(pg,name,doc)
        b.close()
