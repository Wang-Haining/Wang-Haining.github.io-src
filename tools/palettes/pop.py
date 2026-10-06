import json, colorsys
from roles import hex2rgb, rgb2hex, contrast, adjust_l, WHITE, hls
P=json.load(open('curated.json')); L=json.load(open('lisa_roles.json'))
def chroma(c): h,l,s=hls(c); return s*(1-abs(2*l-1))
def hd(a,b): d=abs(a-b); return min(d,1-d)
for p in P:
    src=next((x for x in L if x['work'][:14]==p['work'][:14] or (p['work'].startswith('The ') and x['work'][:14]==p['work'][4:18]) or x['work'][:10]==p['work'][:10]), None)
    cols=[hex2rgb(c) for c in (src['colors'] if src else p['src'])]
    side=hex2rgb(p['sidebar']); sh=hls(side)[0]
    cand=[c for c in cols if chroma(c)>0.10 and hd(hls(c)[0],sh)>=0.12]
    if not cand:
        h=(sh+0.5)%1; cand=[colorsys.hls_to_rgb(h,0.72,0.55)]; how='complement'
    else: how='painting'
    best=max(cand,key=lambda c: hd(hls(c)[0],sh)*1.0+chroma(c)*0.8)
    # light pop with sidebar-colored ink, or dark pop with white ink
    if hls(best)[1]>=0.5:
        pop=best
        ink=rgb2hex(adjust_l(side,lambda r: contrast(r,pop)>=4.8,-0.01))
    else:
        pop=adjust_l(best,lambda r: contrast(r,WHITE)>=4.6,-0.01); ink='#ffffff'
    p['pop']=rgb2hex(pop); p['popInk']=ink
    print(f"{p['work'][:28]:28} side {p['sidebar']} pop {p['pop']} ink {ink} ({how}) cr {contrast(pop,hex2rgb(ink)):.2f} vsWhite {contrast(pop,WHITE):.2f}")
json.dump(P,open('curated.json','w'),indent=1,ensure_ascii=False)
