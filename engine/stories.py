STX=f"""
.st{{position:absolute;inset:0;padding:260px 80px 260px;display:flex;flex-direction:column;align-items:center;text-align:center}}
.lg{{height:160px}}
.k{{display:inline-block;background:var(--blue);color:#fff;font-weight:700;font-size:38px;padding:10px 32px;border-radius:999px;margin-top:50px}}
.h{{font-weight:700;font-size:84px;line-height:1.3;margin-top:36px}}
.y{{color:var(--yellow)}}
.d{{font-size:46px;line-height:1.55;margin-top:26px;opacity:.92}}
.sp{{flex:1}}
.im{{width:100%;border-radius:40px;overflow:hidden;box-shadow:0 30px 70px #0009;position:relative}}
.im img{{width:100%;height:100%;object-fit:cover;display:block}}
.im .lb{{position:absolute;top:18px;left:18px;background:#000a;font-size:24px;padding:4px 16px;border-radius:999px;color:var(--muted)}}
.fn{{font-size:26px;color:var(--muted);line-height:1.5}}
.bub{{background:#3A3A44;border-radius:40px 40px 40px 12px;padding:26px 40px;font-size:60px;font-weight:700;align-self:flex-start;margin-top:60px}}
.cols{{display:flex;gap:24px;width:100%;margin-top:50px;text-align:right}}
.col{{flex:1;background:var(--card);border-radius:36px;overflow:hidden}}
.col img{{width:100%;height:420px;object-fit:cover;display:block}}
.col div{{padding:28px 30px 34px}}
.col b{{display:block;font-size:52px}}
.col p{{font-size:36px;line-height:1.5;margin-top:10px;opacity:.9}}
"""
def S(body,bg=""): return html(f"<div class='st' style='{bg}'>{body}</div>",STX)
LG=f"<img class='lg' src='{LOGO}'>"
NIGHT="background:radial-gradient(circle at 50% 30%,var(--night) 0%,var(--dark) 62%)"
STORIES=[
# set A — with reel 1
("story-A1",S(f"""{LG}<div class='bub'>مش جوعان 🙂</div>
<div class='h' style='margin-top:70px'>مين بالعيلة بيحكيها<br><span class='y'>بكل عزومة؟</span> 😅</div><div class='sp'></div>""")),
("story-A2",S(f"""{LG}<div class='h' style='margin-top:90px'>إذا حدا بعيلتك صار<br>يمضغ على جهة وحدة…</div>
<div class='d'>خلّيه يعمل فحص واستشارة.<br>مجانية بالزرقاء والشميساني.</div><div class='sp'></div>
<div class='fn'>{MED}</div>""",NIGHT)),
("story-A3",S(f"""{LG}<span class='k'>اسألنا 👇</span><div class='h'>عندك سؤال عن<br>التركيبات الثابتة؟</div>
<div class='d'>إلك أو لأهلك.<br>بنجاوب عليه بستوري.</div><div class='sp'></div>""")),
# set B — with reel 2
("story-B1",S(f"""{LG}<span class='k'>اختبار سريع 🤔</span><div class='h'>الفنير المتحرك<br>بيحتاج <span class='y'>برد</span> للأسنان؟</div>
<div class='sp'></div><div class='im' style='height:560px'><img src='file://{A}service-veneer.webp' style='object-position:center 30%'><span class='lb'>صورة تمثيلية</span></div>""")),
("story-B2",S(f"""{LG}<span class='k'>الجواب ✅</span><div class='h'><span class='y'>غالباً لا.</span></div>
<div class='d'>والقرار النهائي بيكون<br>بعد فحص الحالة بالفرع.</div><div class='sp'></div>
<div class='fn'>{VMED}</div>""",NIGHT)),
("story-B3",S(f"""{LG}<div class='h' style='margin-top:90px'>قديش بتخجلي<br>تضحكي بالصور؟</div>
<div class='sp'></div><div class='d'>الاستشارة مجانية،<br>واحجزيها من موبايلك 👇</div><div style='height:260px'></div>""")),
# set C — with reel 3
("story-C1",S(f"""{LG}<div class='h' style='margin-top:80px'>سمعت عن <span class='lat y'>E.max</span><br>قبل هيك؟</div>
<div class='sp'></div><div class='im' style='height:620px'><img src='file://{A}service-emax.webp' style='object-position:center 55%'><span class='lb'>صورة توضيحية</span></div>""")),
("story-C2",S(f"""{LG}<div class='h' style='font-size:72px;margin-top:60px'>الفرق بسطرين</div>
<div class='cols'><div class='col'><img src='file://{A}service-zirconia.webp' style='object-position:30% center'><div><b>زيركون</b><p>تركيبة ثابتة بتجمع بين المتانة والمظهر الطبيعي.</p></div></div>
<div class='col'><img src='file://{A}service-emax.webp' style='object-position:center 55%'><div><b class='lat' style='text-align:right'>E.max</b><p>شفافية عالية، للقشور والتيجان حسب الحالة.</p></div></div></div>
<div class='d' style='font-size:42px;margin-top:44px'>والقرار للطبيب بعد الفحص.</div><div class='sp'></div>
<div class='fn'>{MED}</div>""")),
("story-C3",S(f"""{LG}<div class='h' style='margin-top:90px'>محتار بين<br>خيارين؟</div>
<div class='d'>احجز فحص واستشارة <span class='y' style='font-weight:700'>مجانية</span><br>وبنوضحلك الخيارات حسب حالتك.</div><div class='sp'></div>
<div class='d' style='font-size:40px'>📍 الزرقاء | الشميساني</div><div style='height:200px'></div>""",NIGHT)),
]
CVX="""
.cv{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 80px}
.cv .a{font-weight:700;font-size:150px;color:var(--yellow);line-height:1.15}
.cv .b{font-weight:700;font-size:74px;line-height:1.35;margin-top:24px}
"""
COVERS=[
("cover-1",html(f"""<div class='cv' style='{NIGHT}'><div class='a' style='font-size:124px;white-space:nowrap'>«مش جوعان»</div><div class='b'>أكثر جملة بنسمعها<br>بعزايم العيلة 😅</div></div>""",CVX)),
("cover-2",html(f"""<div class='abs' style='inset:0;background:url("file://{A}service-veneer.webp") center 22%/cover'></div>
<div class='abs' style='inset:0;background:linear-gradient(180deg,#23232A00 20%,#23232ACC 50%,#23232AEE 70%,#23232A99 100%)'></div>
<div class='cv' style='padding-top:300px'><div class='a lat'>3</div><div class='b'>أسئلة بتخجلي تسأليها<br>عن الفنير المتحرك</div></div>""",CVX)),
("cover-3",html(f"""<div class='abs' style='top:0;right:0;width:540px;height:1920px;background:url("file://{A}service-zirconia.webp") 30% center/cover'></div>
<div class='abs' style='top:0;left:0;width:540px;height:1920px;background:url("file://{A}service-emax.webp") center 55%/cover'></div>
<div class='abs' style='inset:0;background:linear-gradient(180deg,#23232A33 0%,#23232AC8 38%,#23232AC8 64%,#23232A33 100%)'></div>
<div class='cv'><div class='b' style='font-size:110px;margin:0'>زيركون</div><div class='b' style='font-size:60px;color:var(--muted);margin:6px 0'>ولا</div><div class='a lat' style='font-size:130px'>E.max</div><div class='b' style='font-size:52px;font-weight:600'>الفرق بأقل من دقيقة</div></div>""",CVX)),
]
