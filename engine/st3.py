import sys; sys.argv=['x','none']; sys.path.insert(0,'.')
from build import *
exec(open('stories.py').read())
from playwright.sync_api import sync_playwright
X=[("q-answers-1",S(f"""{LG}<span class='k'>أسئلتكم 💬</span><div class='h'>جاوبنا على<br>أسئلتكم 👇</div><div class='d'>اسحب للستوري الجاية</div><div class='sp'></div>""",NIGHT)),
("q-answers-2",S(f"""{LG}<div class='sp'></div><div style='height:700px'></div><div class='d' style='font-size:40px'>أي سؤال عن حالتك بالذات،<br>جوابه بالاستشارة المجانية 🤍</div><div class='sp'></div><div class='fn'>{MED}</div>""")),
("follow-1",S(f"""{LG}<div class='h' style='margin-top:90px'>شفت ريل اليوم؟ 😄</div><div class='d'>تابعتنا ولا لسا؟</div><div class='sp'></div>""",NIGHT)),
("follow-2",S(f"""{LG}<div class='h' style='margin-top:90px'>منشن حدا<br><span class='y'>لازم يتابعنا</span> 👇</div><div class='sp'></div><div class='d' style='font-size:40px'>📍 الزرقاء | الشميساني</div><div style='height:120px'></div>"""))]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for n,d in X: still(pg,n,d)
    b.close()
