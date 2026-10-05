import sys, os; sys.argv=['x','none']; sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from build import *
from playwright.sync_api import sync_playwright

HOOKX="""
.hook{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 80px 160px;z-index:30;background:var(--dark)}
.hook .a{font-weight:700;font-size:112px;line-height:1.2}
.hook .b{font-weight:700;font-size:58px;line-height:1.4;margin-top:24px}
.y{color:var(--yellow)}
"""
def hook(a,b,t=1.7): return f"<div class='hook' style='{an(f'fout .4s ease {t}s forwards')}'><div class='a'>{a}</div><div class='b'>{b}</div></div>"

# ---------- QA (image bg) ----------
def qa(img,pos,label,hk_a,hk_b,items,end_t,end_title,end_sub,fine):
    X=R2X.replace(f"service-veneer.webp') center 22%",f"{img}') {pos}")
    cards=""; prog=""; n=len(items)
    for i,(t,q,a) in enumerate(items):
        cards+=f"""<div class='card' style='{an(f"up .5s ease {t}s both")},upout .4s ease {t+3.85}s forwards'>
<span class='chip'>سؤال {i+1} من {n}</span><div class='q'>{q}</div>
<div class='al' style='{an(f"fin .3s ease {t+1.2}s both")}'>الجواب</div>
<div class='a' style='{an(f"up .45s ease {t+1.3}s both")}'>{a}</div></div>"""
        prog+=f"<div><span style='{an(f'bar 4.2s linear {t}s both')}'></span></div>"
    return html(f"""<div class='bg' style='{an("kb 19s linear 0s both")}'></div><div class='sh'></div>
<div class='tag'>{label}</div>
<div class='hk' style='{an("upout .45s ease 2.2s forwards")}'><div class='a'>{hk_a}</div><div class='b'>{hk_b}</div></div>
<div class='prog' style='{an("fin .4s ease 2.5s both")}'>{prog}</div>{cards}
{endcard(end_t,end_title,end_sub,fine)}""",X)

# ---------- chat ----------
def chat(title,members,hk_a,hk_b,msgs,typing_t,last,end_t,end_title,end_sub,fine,episode=""):
    b1="".join(bub(t,w,x,m,tm) for t,w,x,m,tm in msgs)
    typ=f"<div class='b ot typ' style='{an(f'grow .35s ease {typing_t}s both',f'shrink .25s ease {typing_t+1.2}s forwards')}'>"+"".join(f"<i style='{an(f'dot .9s ease {typing_t+k*.15}s infinite')}'></i>" for k in range(3))+"</div>"
    lt,lw,lx,ltm=last
    b1+=typ+bub(lt,lw,lx,False,ltm)
    return html(f"""<div class='tag'>قصة تمثيلية</div>
<div class='hook' style='{an("fout .45s ease 2.1s forwards")}'><div class='a' style='font-size:110px'>{hk_a}</div><div class='b'>{hk_b}</div></div>
<div class='chat' style='{an("up .6s ease 2.0s both")}'>
<div class='hd'><div class='av'>🏠</div><div><div class='n'>{title}</div><div class='m'>{members}</div></div></div>
<div class='msgs'>{b1}</div></div>
{endcard(end_t,end_title,end_sub,fine,episode)}""",R1X)

# ---------- documentary ----------
DOCX="""
.bars:before,.bars:after{content:'';position:absolute;left:0;right:0;height:250px;background:#000;z-index:20}
.bars:before{top:0}.bars:after{bottom:0}
.bg2{position:absolute;inset:0;background:radial-gradient(circle at 50% 45%,#2E2E36 0%,#121216 70%)}
.grain{position:absolute;inset:0;opacity:.07;background-image:repeating-radial-gradient(circle at 17% 32%,#fff 0 1px,transparent 1px 3px);z-index:15}
.yr{position:absolute;top:640px;left:0;right:0;text-align:center;font-family:Inter;font-weight:800;font-size:170px;color:var(--white);letter-spacing:6px}
.sub{position:absolute;top:900px;left:90px;right:90px;text-align:center;font-weight:600;font-size:56px;line-height:1.5}
.sub2{position:absolute;top:1090px;left:90px;right:90px;text-align:center;font-size:44px;line-height:1.5;color:var(--muted)}
.ttl{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;z-index:25;background:#000}
.ttl .s{font-family:Inter;font-weight:700;letter-spacing:10px;font-size:32px;color:var(--muted)}
.ttl .t{font-weight:700;font-size:84px;line-height:1.3;margin-top:24px;padding:0 80px}
"""
def doc(title,beats,end_t,end_title,end_sub,fine,episode=""):
    out=""
    for i,(t,yr,s1,s2) in enumerate(beats):
        nxt=beats[i+1][0] if i+1<len(beats) else end_t
        o=f"fout .35s ease {nxt-.35}s forwards"
        out+=f"<div class='yr' style='{an(f'fin .6s ease {t}s both',o)}'>{yr}</div>"
        out+=f"<div class='sub' style='{an(f'up .5s ease {t+.4}s both',o)}'>{s1}</div>"
        if s2: out+=f"<div class='sub2' style='{an(f'fin .5s ease {t+1.3}s both',o)}'>{s2}</div>"
    return html(f"""<div class='bg2'></div><div class='grain'></div><div class='bars'></div>
<div class='tag' style='z-index:30;top:270px'>تمثيل</div>
<div class='ttl' style='{an("fout .6s ease 2.4s forwards")}'><div class='s'>A SMILE JO DOCUMENTARY</div><div class='t'>{title}</div></div>
{out}{endcard(end_t,end_title,end_sub,fine,episode)}""",DOCX)

# ---------- versus (two images, alternating highlight) ----------
VSX=R3X
def versus(right_img,right_pos,right_lb,left_img,left_pos,left_lb,hk_html,hk_sub,rh,rd,lh,ld,who_q,who_a,end_title,end_sub,fine,tag='صور توضيحية'):
    return html(f"""<div class='tag' style='top:150px'>{tag}</div>
<div class='ph z' style='{an("dim .4s ease 7.0s forwards","undim .4s ease 11.3s forwards")}'><img src='file://{A}{right_img}' style='object-position:{right_pos}'><span class='lb'>{right_lb}</span></div>
<div class='ph e' style='{an("dim .4s ease 2.6s both","undim .4s ease 7.0s forwards")}'><img src='file://{A}{left_img}' style='object-position:{left_pos}'><span class='lb'>{left_lb}</span></div>
<div class='hk' style='{an("upout .4s ease 2.2s forwards")}'><div class='a' style='font-size:84px'>{hk_html}</div><div class='b'>{hk_sub}</div></div>
<div class='tx' style='{an("up .5s ease 2.6s both","upout .4s ease 6.8s forwards")}'><span class='k'>{right_lb}</span><div class='h'>{rh}</div><div class='d'>{rd}</div></div>
<div class='tx' style='{an("up .5s ease 7.2s both","upout .4s ease 11.2s forwards")}'><span class='k'>{left_lb}</span><div class='h'>{lh}</div><div class='d'>{ld}</div></div>
<div class='who' style='{an("fin .45s ease 11.6s both")}'><div class='q' style='font-size:88px;{an("pop .6s ease 11.8s both")}'>{who_q}</div>
<div class='a' style='{an("up .5s ease 12.9s both")}'>{who_a}</div></div>
{endcard(15.4,end_title,end_sub,fine)}""",VSX)

# ---------- list (paper or dark rows with marks) ----------
LX="""
.ttl{position:absolute;top:240px;left:60px;right:60px;text-align:center;font-weight:700;font-size:62px;line-height:1.3}
.lst{position:absolute;top:430px;left:60px;right:60px}
.row{display:flex;gap:28px;align-items:center;background:var(--card);border-radius:32px;padding:40px 38px;margin-bottom:28px}
.row .m{flex:none;width:76px;height:76px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:Inter;font-weight:800;font-size:42px;color:#fff;background:var(--blue)}
.row.bad .m{background:#C9372C}
.row .x{font-weight:700;font-size:53px;line-height:1.36}
"""
def lst(tag,hk_a,hk_b,title,rows,t0,step,end_t,end_title,end_sub,fine):
    r=""
    for i,(mark,text,bad) in enumerate(rows):
        r+=f"<div class='row{' bad' if bad else ''}' style='{an(f'pop .45s ease {t0+i*step}s both')}'><div class='m'>{mark}</div><div class='x'>{text}</div></div>"
    return html(f"""<div class='tag'>{tag}</div>{hook(hk_a,hk_b,t0-.3)}
<div class='ttl' style='{an(f"fin .4s ease {t0-.3}s both")}'>{title}</div><div class='lst'>{r}</div>
{endcard(end_t,end_title,end_sub,fine)}""",HOOKX+LX)

REELS3=[
("2026-10-08","reel-qa-fixed",qa('service-zirconia.webp','30% center','صور توضيحية',"3","أسئلة بتخجل تسألها<br>عن التركيبات الثابتة",
 [(2.6,"التركيبة الثابتة بتنشال؟","لأ، هي ثابتة.<br>وهاد الفرق بينها وبين الفنير المتحرك."),
  (6.8,"مين بيحدد زيركون<br>ولا <span class='lat'>E.max</span>؟","الطبيب بعد الفحص، حسب حالتك."),
  (11.0,"قديش بتاخذ وقت؟","المدة بتختلف حسب الخدمة والحالة،<br>وبتعرفها بعد الاستشارة.")],
 15.2,"احفظ الفيديو<br>لوقت ما تحتاجه 🔖","وأي سؤال ثاني، اسألنا بالكومنتات",MED),19.0),
("2026-10-09","reel-abu-ahmad-2",chat("العيلة","أبو أحمد، أم أحمد، أحمد","الحلقة 2","أبو أحمد<br>بعد الاستشارة 👀",
 [(2.7,"أحمد","يابا طمني، كيف كانت الاستشارة؟",True,"6:10 PM"),
  (4.0,"أبو أحمد","والله شرحولي كل إشي على رواق",False,"6:12 PM"),
  (5.4,"أم أحمد","وأخيراً سأل كل الأسئلة اللي كان يخبيها 😅",False,"6:12 PM"),
  (7.2,"أحمد","طيب شو قررت؟",True,"6:13 PM"),
  (8.6,"أبو أحمد","قالولي في كذا خيار، وأنا رح أفكر بالزيركون",False,"6:15 PM"),
  (10.3,"أحمد","المهم ارتحت؟ 🤍",True,"6:15 PM")],
 11.7,(13.1,"أبو أحمد","ارتحت… وعزومة الجمعة عليّ 😄","6:17 PM"),
 15.0,"أحياناً كل اللي بنحتاجه<br>حدا يسألنا «كيف حالك؟» 🤍","ابعتها لحدا بالعيلة لازم يشوفها",MED+"<br>فحص واستشارة مجانية · الزرقاء | الشميساني","الحلقة الجاية: عزومة الجمعة"),19.0),
("2026-10-11","reel-documentary",doc("الرجل اللي<br>ما ضحك بالصور",
 [(2.6,"2011","صورة التخرج.","غطّى تمّه بإيده."),(5.4,"2016","عرس أخوه.","وقف ورا الكل."),(8.2,"2024","صورة العيلة.","ابتسم… بدون سنان."),(11.0,"2026","حجز استشارة مجانية.","وأخيراً، سأل.")],
 14.2,"الحلقة الجاية:<br>يوم الاستشارة 🎬","إذا بتعرف حدا زيه، ابعتله الفيديو",MED),18.0),
("2026-10-13","reel-removable-vs-fixed",versus('service-zirconia.webp','30% center','تركيبة ثابتة','service-veneer.webp','center 25%','الفنير المتحرك',
 "متحرك<br>ولا <span class='y'>ثابت</span>؟","الفرق بأقل من دقيقة",
 "حسب تقييم الطبيب","زيركون أو <span class='lat'>E.max</span> أو غيرهم،<br>والخيار بيتحدد بعد الفحص.",
 "بداية سهلة","بتلبسه وبتشيله.<br>حل تجميلي متحرك، مش بديل دائم.",
 "طب بأيهم أبلّش؟","بلّش بالمتحرك إذا بدك حل سريع،<br><span class='y'>ولما تكون جاهز، في خيارات ثابتة.</span>",
 "ابعتها لحدا<br>محتار بين الاثنين","فحص واستشارة مجانية بالزرقاء والشميساني",VMED+"<br>"+MED,tag='صور توضيحية · صورة تمثيلية'),19.0),
("2026-10-15","reel-pov-first-visit",lst("📍 فروعنا: الزرقاء | الشميساني","<span class='lat'>POV:</span>","أول مرة بتدخل<br>فرع سمايل جو","أول زيارة إلك لفرعنا 👀",
 [("1","بتحكي «بس بدي أسأل» 😅",False),("2","بتسأل 100 سؤال… وكلهم إلهم جواب",False),("3","بتعرف كل خياراتك، المتحرك والثابت",False),("4","وبتطلع لسا ما قررت… وعادي 🤍",False)],
 1.9,2.2,12.0,"الاستشارة مجانية،<br>والقرار إلك","احجز من الموبايل وتعال اسأل",MED),16.0),
("2026-10-16","reel-before-consult",lst("احفظه 🔖","5 أشياء","اعملها قبل<br>استشارتك المجانية","قبل استشارتك المجانية ✍️",
 [("1","صوّر ابتسامتك من قدام 📸",False),("2","اكتب كل أسئلتك على الموبايل",False),("3","فكّر شو بزعجك أكثر: الشكل ولا المضغ؟",False),("4","جيب معك حدا بتثق برأيه",False),("5","واحجز من smilejo.shop ☕",False)],
 1.9,2.0,13.4,"احفظ الفيديو<br>وابعته لحدا محتار","الاستشارة مجانية بالزرقاء والشميساني",MED),17.5),
("2026-10-18","reel-follow-or-unfollow",lst("بخفة دم 😄","تابعنا إذا…","وأنفولو إذا… 😅","تابعنا إذا… 👀",
 [("✓","بتحب تضحك بالصور وإنت واثق",False),("✓","بدك تعرف كل خياراتك قبل ما تقرر",False),("✓","بتحب تحجز وإنت عالكنباية",False),("✗","وأنفولو إذا بتحب تستنى حدا يرد عليك 😅",True)],
 1.9,2.2,12.0,"تابعنا 😄<br>والباقي علينا","@smile._.jo · smilejo.shop",MED),16.0),
]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    only=os.environ.get('ONLY')
    for day,name,docu,d in REELS3:
        if only and only!=name: continue
        if os.environ.get('MODE')=='preview':
            for t in [0,3.5,7.5,10,13,15.5]: still(pg,f'{name}-t{t}',docu,t)
        else:
            render_reel(pg,name,docu,d); print('done',name,flush=True)
    b.close()
