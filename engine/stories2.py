import sys, os
sys.argv=['x','none']
SPD=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+'/'
sys.path.insert(0,SPD)
import build
from build import *
exec(open(SPD+'stories.py').read())
X2="""
.mini{font-size:28px;color:var(--muted);margin-top:18px}
.or{display:flex;flex-direction:column;gap:0;width:100%;margin-top:60px;align-items:center}
.opt{width:100%;background:var(--card);border-radius:40px;padding:56px 40px;font-weight:700;font-size:64px}
.vs{font-weight:700;font-size:44px;color:var(--yellow);margin:22px 0}
.st2 .h{font-size:78px}
.list{width:100%;margin-top:46px;display:flex;flex-direction:column;gap:20px;text-align:right}
.list div{background:var(--card);border-radius:30px;padding:30px 36px;font-size:46px;font-weight:600}
.list small{display:block;font-size:32px;font-weight:400;color:var(--muted);margin-top:6px}
"""
def S2(body,bg=""): return html(f"<div class='st' style='{bg}'>{body}</div>",STX+X2)
EP=lambda n:f"<span class='k'>حكاية تفاعلية · {n}</span>"
TAG="<div class='fn' style='margin-top:24px'>قصة تمثيلية</div>"
IMG=lambda f,pos,h,lb='صورة توضيحية':f"<div class='im' style='height:{h}px'><img src='file://{A}{f}' style='object-position:{pos}'><span class='lb'>{lb}</span></div>"
TF=lambda i:f"<span class='k'>صح ولا غلط؟ · {i}/4</span>"
NEW=[
# --- سلمى: حكاية تفاعلية 3 أيام ---
("salma-1a",S2(f"""{LG}{EP('الحلقة 1')}<div class='h'>سلمى عندها عرس<br>أختها بعد أسبوعين 💍</div>
<div class='d'>وكل ما حدا يصوّرها،<br>بتضحك وتمها مسكّر 🤐</div><div class='sp'></div>{TAG}""")),
("salma-1b",S2(f"""{LG}<div class='h' style='margin-top:90px'>شو لازم تعمل <span class='y'>سلمى</span>؟ 🤔</div>
<div class='d'>إنتو بتقرروا…<br>وبكرا بنكمّل الحكاية حسب تصويتكم.</div><div class='sp'></div>{TAG}""",NIGHT)),
("salma-2a-consult",S2(f"""{LG}{EP('الحلقة 2')}<div class='h'>أغلبكم قال:<br><span class='y'>تحجز استشارة</span> 📅</div>
<div class='d'>سلمى حجزت من موبايلها.<br>وبالاستشارة عرفت إنه في خيار<br>مؤقت سريع، وخيارات ثابتة لبعدين.</div><div class='sp'></div>{TAG}""")),
("salma-2a-hide",S2(f"""{LG}{EP('الحلقة 2')}<div class='h'>أغلبكم قال:<br><span class='y'>تضل تخبّي</span> 🤐</div>
<div class='d'>يعني كل صور العرس بتمّ مسكّر؟ 😅<br>سلمى قررت تسأل بس، وحجزت استشارة.<br>وهناك عرفت إنه في خيار مؤقت سريع،<br>وخيارات ثابتة لبعدين.</div><div class='sp'></div>{TAG}""")),
("salma-2b",S2(f"""{LG}<div class='h' style='margin-top:90px'>شو برأيكم<br>اختارت سلمى؟</div>
<div class='d'>بكرا بنحكيلكم 👀</div><div class='sp'></div>
<div class='fn'>{VMED}</div>{TAG}""",NIGHT)),
("salma-3a",S2(f"""{LG}{EP('الحلقة الأخيرة')}<div class='h'>سلمى بالعرس 📸</div>
<div class='d'>اختارت الفنير المتحرك لأنه العرس قريب،<br>وقالت: «بعد العرس بفكر بخيار ثابت».</div>
<div class='h' style='font-size:64px;margin-top:60px'>وأحلى صورة؟<br><span class='y'>كانت وهي بتضحك</span> 🤍</div><div class='sp'></div>{TAG}""")),
("salma-3b",S2(f"""{LG}<div class='h' style='margin-top:90px'>إذا إنتِ<br>زي سلمى…</div>
<div class='d'>بلّشي باستشارة مجانية،<br>والقرار إلك.</div><div class='sp'></div>
<div class='d' style='font-size:40px'>📍 الزرقاء | الشميساني</div><div style='height:170px'></div>
<div class='fn'>{VMED} · قصة تمثيلية</div>""",NIGHT)),
# --- هاد ولا هاد ---
("this-or-that-1",S2(f"""{LG}<span class='k'>هاد ولا هاد؟ 😄</span><div class='h' style='font-size:66px'>بصور العرس…</div>
<div class='or'><div class='opt'>ضحكة كبيرة 😁</div><div class='vs'>ولا</div><div class='opt'>ابتسامة خفيفة 🙂</div></div><div class='sp'></div>""")),
("this-or-that-2",S2(f"""{LG}<span class='k'>هاد ولا هاد؟ 😄</span><div class='h' style='font-size:66px'>لون الفنير المتحرك…</div>
<div class='or'><div class='opt'>طبيعي 🤍</div><div class='vs'>ولا</div><div class='opt'>لؤلؤي ✨</div></div><div class='sp'></div>""")),
("this-or-that-3",S2(f"""{LG}<span class='k'>هاد ولا هاد؟ 😄</span><div class='h' style='font-size:66px'>بتحجز موعدك…</div>
<div class='or'><div class='opt'>من الموبايل 📱</div><div class='vs'>ولا</div><div class='opt'>بتتصل ☎️</div></div><div class='sp'></div><div style='height:120px'></div>""")),
# --- صح ولا غلط ---
("true-false-1",S2(f"""{LG}{TF(1)}<div class='h' style='margin-top:70px'>الفنير المتحرك بتقدري<br>تلبسيه وتشيليه لحالك</div><div class='sp'></div>""")),
("true-false-2",S2(f"""{LG}{TF(2)}<div class='h' style='margin-top:70px'>الماي السخنة كثير<br>بتنظف الفنير المتحرك أحسن</div><div class='sp'></div>""")),
("true-false-3",S2(f"""{LG}{TF(3)}<div class='h' style='margin-top:70px'>النتيجة التجميلية<br>بتطلع نفسها عند كل الناس</div><div class='sp'></div>""")),
("true-false-4",S2(f"""{LG}{TF(4)}<div class='h' style='margin-top:70px'>الزرعة بدها تقييم<br>للحالة قبل أي إشي</div><div class='sp'></div>""")),
("true-false-5",S2(f"""{LG}<div class='h' style='margin-top:90px'>جاوبت صح<br>على الكل؟ 🏆</div>
<div class='d'>جرّب <span class='y' style='font-weight:700'>«تحدّي الابتسامة»</span> على موقعنا،<br>أسئلة أكثر وبدقيقتين.</div><div class='sp'></div><div style='height:220px'></div>""",NIGHT)),
# --- خمّن شو هاد ---
("guess-1",S2(f"""{LG}<span class='k'>خمّن شو هاد؟ 🤔</span><div class='sp'></div>{IMG('service-implants.webp','center',760)}<div style='height:330px'></div>""")),
("guess-1-answer",S2(f"""{LG}<span class='k'>الجواب ✅</span><div class='h'>تركيبات زرعات</div>
<div class='d'>دعامات وبراغي، وفوقهم تيجان زيركون<br>بتصميم رقمي دقيق.</div><div class='sp'></div>{IMG('service-implants.webp','center',620)}
<div class='fn' style='margin-top:30px'>{MED}</div>""")),
("guess-2",S2(f"""{LG}<span class='k'>وهاد؟ 👀</span><div class='sp'></div>{IMG('service-porcelain.webp','center',760)}<div style='height:330px'></div>""")),
("guess-2-answer",S2(f"""{LG}<span class='k'>الجواب ✅</span><div class='h'>تركيبات البورسلان</div>
<div class='d'>خيارات عملية بتناسب<br>الاحتياج والميزانية.</div><div class='sp'></div>{IMG('service-porcelain.webp','center',620)}
<div class='fn' style='margin-top:30px'>{MED}</div>""")),
# --- شو بدك من ابتسامتك ---
("guide-1",S2(f"""{LG}<div class='h' style='margin-top:90px'>شو أكثر إشي بدك<br><span class='y'>تحسّنه</span> بابتسامتك؟</div><div class='sp'></div>""",NIGHT)),
("guide-2",S2(f"""{LG}<span class='k'>إذا اخترت الشكل ✨</span><div class='h' style='font-size:64px'>خيارات بتنحكى<br>بالاستشارة:</div>
<div class='list'><div>الفنير المتحرك<small>بداية سهلة، بتلبسه وبتشيله</small></div><div class='lat' style='text-align:right'>E.max<small style='font-family:NA'>شفافية عالية للقشور والتيجان</small></div><div class='lat' style='text-align:right'>FlexCer<small style='font-family:NA'>قشور مطبوعة رقمياً</small></div></div>
<div class='sp'></div><div class='fn'>القرار بعد الفحص · {MED}</div>""")),
("guide-3",S2(f"""{LG}<span class='k'>إذا اخترت المضغ 🍽️</span><div class='h' style='font-size:64px'>خيارات بتنحكى<br>بالاستشارة:</div>
<div class='list'><div>تركيبات الزيركون<small>ثابتة، بتجمع بين المتانة والمظهر الطبيعي</small></div><div>تركيبات الزرعات<small>تيجان زيركون بتصميم رقمي دقيق</small></div><div>البورسلان<small>خيارات عملية بتناسب الاحتياج والميزانية</small></div></div>
<div class='sp'></div><div class='fn'>القرار بعد الفحص · {MED}</div>""")),
("guide-4",S2(f"""{LG}<div class='h' style='margin-top:90px'>لسا مش متأكد؟<br>هاد طبيعي 🤍</div>
<div class='d'>جاوب على سؤالين بالموقع،<br>وبعدها احجز استشارتك المجانية.</div><div class='sp'></div><div style='height:220px'></div>
<div class='fn'>{MED}</div>""",NIGHT)),
]
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for name,doc in NEW: still(pg,name,doc)
    b.close()
from PIL import Image
sh=Image.new('RGB',(8*216,3*384),(0,0,0))
for i,(n,_) in enumerate(NEW):
    im=Image.open(OUT+n+'.jpg'); im.thumbnail((216,384)); sh.paste(im,((i%8)*216,(i//8)*384))
sh.save(OUT+'sheet-new.jpg'); print(len(NEW))
