import sys; sys.argv=['x','none']; sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from build import *
from playwright.sync_api import sync_playwright

# ---------- A: قوانين سمايل جو ----------
AX="""
.hook{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 80px 160px;z-index:30;background:var(--dark)}
.hook .a{font-weight:700;font-size:118px;line-height:1.2}
.hook .b{font-weight:700;font-size:58px;color:var(--yellow);margin-top:24px}
.ttl{position:absolute;top:240px;left:0;right:0;text-align:center;font-weight:700;font-size:64px}
.paper{position:absolute;top:350px;left:60px;right:60px;height:1150px;background:var(--white);border-radius:34px;padding:50px 50px;color:var(--dark);box-shadow:0 40px 90px #000a;overflow:hidden}
.paper:before{content:'';position:absolute;top:0;left:0;right:0;height:16px;background:var(--blue)}
.r{display:flex;gap:28px;align-items:flex-start;margin-bottom:30px}
.r .n{flex:none;width:80px;height:80px;border-radius:50%;background:var(--blue);color:#fff;font-family:Inter;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center}
.r .x{font-weight:700;font-size:49px;line-height:1.36;padding-top:2px}
.stamp{position:absolute;left:60px;bottom:34px;border:8px solid var(--blue);color:var(--blue);font-weight:700;font-size:58px;padding:6px 34px;border-radius:20px;transform:rotate(-12deg)}
@keyframes stamp{0%{opacity:0;transform:rotate(-12deg) scale(2.4)}70%{opacity:1;transform:rotate(-12deg) scale(.92)}100%{opacity:1;transform:rotate(-12deg) scale(1)}}
"""
rules=["ممنوع تضحك وتمّك مسكّر 🤐","اللي بيقول «مش جوعان» بالعزومة، بنسأله ليش 🤨","سؤال «بيبيّن؟» مسموح… 100 مرة 😄","الاستشارة مجانية، والتفكير كمان ببلاش 🤍","ممنوع تطلع قبل ما تعرف كل خياراتك","الصورة الجماعية بالآخر إجبارية 📸"]
rows="".join(f"<div class='r' style='{an(f'pop .45s ease {1.9+i*1.65}s both')}'><div class='n'>{i+1}</div><div class='x'>{t}</div></div>" for i,t in enumerate(rules))
RA=html(f"""<div class='tag'>تمثيل… بس مش كثير 😄</div>
<div class='hook' style='{an("fout .4s ease 1.6s forwards")}'><div class='a'>قوانين فرع<br>سمايل جو 📜</div><div class='b'>اقرأها قبل ما تيجي 😂</div></div>
<div class='ttl' style='{an("fin .4s ease 1.6s both")}'>قوانين فرع سمايل جو 📜</div>
<div class='paper' style='{an("up .5s ease 1.5s both")}'>{rows}<div class='stamp' style='{an("stamp .5s ease 12.2s both")}'>معتمد ✔</div></div>
{endcard(14.0,"منشن حدا لازم يلتزم<br>بالقانون رقم 1 😂","فحص واستشارة مجانية بالزرقاء والشميساني",MED)}""",AX)

# ---------- B: POV حجز 2026 ----------
BX="""
.hook{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 80px 160px;z-index:30;background:var(--dark)}
.hook .a{font-family:Inter;font-weight:800;font-size:110px;color:var(--yellow)}
.hook .b{font-weight:700;font-size:72px;line-height:1.35;margin-top:10px}
.cap{position:absolute;top:240px;left:60px;right:60px;text-align:center;font-weight:700;font-size:62px;line-height:1.3}
.ph{position:absolute;top:430px;left:280px;width:520px;height:1040px;border-radius:70px;background:#0E0E12;border:14px solid #3A3A44;box-shadow:0 40px 90px #000c;overflow:hidden}
.nt{position:absolute;top:14px;left:50%;width:150px;height:36px;margin-left:-75px;background:#000;border-radius:20px;z-index:5}
.scr{position:absolute;inset:0;padding:90px 34px 30px;background:var(--dark)}
.url{font-family:Inter;font-weight:700;font-size:24px;color:var(--muted);text-align:center;background:#2E2E36;border-radius:999px;padding:8px}
.sh{font-weight:700;font-size:42px;margin:40px 0 24px}
.gr{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.c{background:#2E2E36;border-radius:22px;padding:24px 12px;text-align:center;font-weight:600;font-size:28px;position:relative}
.c.on{background:var(--blue)}
.big .c{padding:44px 12px;font-size:34px}
.ok{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;height:100%}
.ok .i{width:150px;height:150px;border-radius:50%;background:var(--blue);display:flex;align-items:center;justify-content:center;font-size:84px}
.ok .t{font-weight:700;font-size:44px;margin-top:34px}
.ok .s{font-size:28px;line-height:1.5;color:var(--muted);margin-top:16px}
.tap{position:absolute;width:90px;height:90px;border-radius:50%;background:#ffffff55;border:4px solid #fff;z-index:9;opacity:0}
@keyframes tap{0%{opacity:0;transform:scale(1.6)}40%{opacity:1;transform:scale(.8)}100%{opacity:0;transform:scale(1.2)}}
@keyframes slin{from{transform:translateX(-100%)}to{transform:none}}
@keyframes slout{from{transform:none}to{transform:translateX(100%)}}
@keyframes on{from{background:#2E2E36}to{background:var(--blue)}}
.cnt{position:absolute;top:1490px;left:0;right:0;text-align:center;font-family:Inter;font-weight:800;font-size:46px;color:var(--white)}
"""
def scr(t_in,t_out,body):
    a=[f"slin .35s ease {t_in}s both"] if t_in>0 else []
    if t_out: a.append(f"slout .35s ease {t_out}s forwards")
    return f"<div class='scr' style='{an(*a) if a else ''}'>{body}</div>"
svcs=["الفنير المتحرك","زيركون","E.max","FlexCer","تركيبات زرعات","فحص واستشارة"]
s1="<div class='url'>smilejo.shop</div><div class='sh'>شو الخدمة؟</div><div class='gr'>"+"".join(f"<div class='c' style='{an('on .2s ease 3.1s both') if s=='فحص واستشارة' else ''}' dir='auto'>{s}</div>" for s in svcs)+"</div>"
s2=f"<div class='url'>smilejo.shop</div><div class='sh'>أي فرع؟</div><div class='gr big' style='grid-template-columns:1fr'><div class='c' style='{an('on .2s ease 5.6s both')}'>📍 الزرقاء</div><div class='c'>📍 الشميساني</div></div>"
s3=f"<div class='url'>smilejo.shop</div><div class='sh'>إيمتى بناسبك؟</div><div class='gr'><div class='c'>السبت</div><div class='c' style='{an('on .2s ease 8.1s both')}'>الأحد</div><div class='c'>الاثنين</div><div class='c'>الثلاثاء</div></div>"
s4="<div class='ok'><div class='i'>✓</div><div class='t'>انبعت طلبك</div><div class='s'>الفريق رح يتواصل معك<br>لتأكيد الموعد</div></div>"
def tap(t,x,y): return f"<div class='tap' style='left:{x}px;top:{y}px;{an(f'tap .6s ease {t}s both')}'></div>"
caps=[(1.6,4.2,"وإنت بالبيجاما 😴"),(4.2,6.7,"وما قمت عن الكنباية 🛋️"),(6.7,9.3,"والقهوة لسا سخنة ☕"),(9.3,12.6,"3 لمسات… وخلصنا ✅")]
capd="".join(f"<div class='cap' style='{an(f'up .35s ease {a}s both',f'fout .25s ease {b-.25}s forwards')}'>{t}</div>" for a,b,t in caps)
cnt="".join(f"<div class='cnt' style='{an(f'pop .3s ease {t}s both',f'fout .2s ease {t2}s forwards')}'>لمسة {n}</div>" for n,t,t2 in [(1,3.0,5.4),(2,5.5,7.9),(3,8.0,12.4)])
RB=html(f"""<div class='hook' style='{an("fout .4s ease 1.4s forwards")}'><div class='a lat'>POV:</div><div class='b'>حجزت موعد سنانك<br>بـ <span class='lat'>2026</span></div></div>
{capd}
<div class='ph' style='{an("up .5s ease 1.4s both")}'><div class='nt'></div>
{scr(0,3.5,s1)}{scr(3.5,6.0,s2)}{scr(6.0,8.5,s3)}{scr(8.5,0,s4)}
{tap(2.9,95,560)}{tap(5.4,200,330)}{tap(7.9,40,330)}</div>
{cnt}
{endcard(12.8,"احجز من موبايلك<br>وإنت محلك 🛋️","فحص واستشارة مجانية بالزرقاء والشميساني",MED)}""",BX)

# ---------- C: الهدية ----------
CX="""
.hk{position:absolute;top:250px;left:70px;right:70px;text-align:center;font-weight:700;font-size:78px;line-height:1.3}
.box{position:absolute;left:290px;top:820px;width:500px;height:500px}
.bx{position:absolute;left:0;right:0;bottom:0;height:380px;background:var(--blue);border-radius:24px}
.bx:after{content:'';position:absolute;left:50%;margin-left:-35px;top:0;bottom:0;width:70px;background:var(--yellow)}
.lid{position:absolute;left:-30px;right:-30px;top:60px;height:110px;background:#0B5DE0;border-radius:22px;z-index:3}
.lid:after{content:'';position:absolute;left:50%;margin-left:-35px;top:0;bottom:0;width:70px;background:var(--yellow)}
.bow{position:absolute;left:50%;top:-56px;margin-left:-90px;width:180px;height:80px}
.bow i{position:absolute;top:0;width:90px;height:70px;border:18px solid var(--yellow);border-radius:50% 50% 50% 50%}
.card{position:absolute;left:170px;right:170px;top:820px;background:var(--white);color:var(--dark);border-radius:30px;padding:46px 40px;text-align:center;box-shadow:0 30px 80px #000a;z-index:2}
.card .e{font-size:80px}.card .t{font-weight:700;font-size:56px;line-height:1.35;margin-top:10px}
.card .s{font-size:34px;color:#555;margin-top:12px}
.ln{position:absolute;left:70px;right:70px;top:1380px;text-align:center;font-weight:700;font-size:56px;line-height:1.4}
@keyframes shake{0%,100%{transform:rotate(0)}20%{transform:rotate(-5deg)}40%{transform:rotate(5deg)}60%{transform:rotate(-4deg)}80%{transform:rotate(3deg)}}
@keyframes lidoff{from{transform:none;opacity:1}to{transform:translate(-260px,-520px) rotate(-38deg);opacity:0}}
@keyframes rise{from{opacity:0;transform:translateY(360px) scale(.6)}to{opacity:1;transform:translateY(-250px) scale(1)}}
@keyframes boxdown{from{transform:none;opacity:1}to{transform:translateY(260px);opacity:.0}}
"""
RC=html(f"""<div class='hk' style='{an("upout .4s ease 5.0s forwards")}'>أغلى هدية ممكن<br>تعطيها <span style='color:var(--yellow)'>لأمك</span>…</div>
<div class='box' style='{an("shake .8s ease 2.0s both","boxdown .6s ease 4.6s forwards")}'><div class='bx'></div><div class='lid' style='{an("lidoff .6s ease 3.0s forwards")}'><div class='bow'><i style='left:0;transform:rotate(-20deg)'></i><i style='right:0;transform:rotate(20deg)'></i></div></div></div>
<div class='card' style='{an("rise .8s cubic-bezier(.2,.9,.3,1.15) 3.3s both")}'><div class='e'>🎁</div><div class='t'>فحص واستشارة<br>مجانية لماما</div><div class='s'>سمايل جو · الزرقاء | الشميساني</div></div>
<div class='hk' style='{an("up .45s ease 5.3s both","upout .35s ease 8.0s forwards")}'>ببلاش 😄<br>بس بتفرق معها كثير</div>
<div class='hk' style='{an("up .45s ease 8.3s both","upout .35s ease 11.4s forwards")}'>لأنها دايماً بتأجّل حالها<br>عشانكم 🤍</div>
<div class='ln' style='{an("up .45s ease 9.2s both","fout .3s ease 11.4s forwards")}'>احجزلها من الموبايل،<br>والفريق بيرتب الباقي</div>
{endcard(11.8,"منشن أخوك أو أختك…<br>ونحجزلها سوا 🤍","الاستشارة مجانية بالزرقاء والشميساني",MED)}""",CX)

R=[("reel-rules",RA,17.5),("reel-pov-2026",RB,16.5),("reel-gift-mama",RC,15.5)]
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    import os
    if os.environ.get('MODE')=='preview':
        for name,doc,d in R:
            for t in [0,2.5,4.5,6.5,9,11.5,13.5,16]: still(pg,f'{name}-t{t}',doc,t)
    else:
        for name,doc,d in [x for x in R if x[0]==os.environ.get("ONLY",x[0])]: render_reel(pg,name,doc,d); print('done',name,flush=True)
    b.close()
