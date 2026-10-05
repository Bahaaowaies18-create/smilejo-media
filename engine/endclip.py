import sys; sys.argv=['x','none']; sys.path.insert(0,'.')
from build import *
from playwright.sync_api import sync_playwright
doc=html(f"""<div class='end' style='{an("fin .35s ease 0s both")}'>
<img src='{LOGO}' style='width:380px;{an("pop .7s ease .15s both")}'>
<div class='t' style='font-size:76px;{an("up .55s ease .5s both")}'>شكراً إلكم 🤍</div>
<div class='lat' style='margin-top:30px;font-weight:700;font-size:58px;color:var(--white);{an("up .55s ease .8s both")}'>@smile._.jo</div>
<div class='pill' style='{an("pop .55s ease 1.1s both")}'>smilejo.shop</div></div>""")
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    render_reel(pg,'endcard-50k',doc,3.0)
    still(pg,'endcard-50k',doc,2.9)
    b.close()
