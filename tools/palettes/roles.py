import json, colorsys
def hex2rgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16)/255 for i in (0,2,4))
def rgb2hex(c): return '#%02x%02x%02x'%tuple(round(max(0,min(1,x))*255) for x in c)
def lin(c): return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def lum(rgb): r,g,b=map(lin,rgb); return 0.2126*r+0.7152*g+0.0722*b
def contrast(a,b):
    la,lb=lum(a),lum(b); hi,lo=max(la,lb),min(la,lb); return (hi+0.05)/(lo+0.05)
WHITE=(1,1,1); DARKBG=hex2rgb('#333333')
def hls(c): return colorsys.rgb_to_hls(*c)
def adjust_l(c, target_fn, step):
    h,l,s=hls(c)
    for _ in range(100):
        rgb=colorsys.hls_to_rgb(h,l,s)
        if target_fn(rgb): return rgb
        l=max(0,min(1,l+step))
    return colorsys.hls_to_rgb(h,l,s)
def mix(c,w,t): return tuple(c[i]*(1-t)+w[i]*t for i in range(3))
def roles(colors):
    cs=[hex2rgb(c) for c in dict.fromkeys(c.lower() for c in colors)]
    sat=lambda c: hls(c)[2]*(1-abs(2*hls(c)[1]-1))  # chroma-ish
    # sidebar: prefer chromatic colors; darken until white text >= 4.6, but not too dark
    def side_score(c):
        cr=contrast(c,WHITE); ch=sat(c); l=lum(c)
        return (cr>=3.0)*1 + ch*2 - abs(l-0.12)*3
    side=max(cs,key=side_score)
    side=adjust_l(side, lambda r: contrast(r,WHITE)>=4.6, -0.01)
    sh=hls(side)[0]
    # accent: most chromatic color with hue distinct from sidebar
    def hue_d(c): d=abs(hls(c)[0]-sh); return min(d,1-d)
    acc_src=max(cs,key=lambda c: sat(c)*1.5+hue_d(c))
    acc=adjust_l(acc_src, lambda r: contrast(r,WHITE)>=4.6, -0.01)
    hover=adjust_l(acc, lambda r: contrast(r,WHITE)<5.5 and contrast(r,WHITE)>=3.2, +0.01) if contrast(acc,WHITE)>6 else adjust_l(acc, lambda r: contrast(r,WHITE)>=6.5, -0.01)
    acc_dark=adjust_l(acc_src, lambda r: contrast(r,DARKBG)>=4.6, +0.01)
    tint_src=max(cs,key=lambda c: lum(c))
    sel=mix(acc_src,WHITE,0.72)
    chip=mix(side,WHITE,0.22)
    return dict(sidebar=rgb2hex(side), accent=rgb2hex(acc), hover=rgb2hex(hover), accentDark=rgb2hex(acc_dark), selection=rgb2hex(sel), chip=rgb2hex(chip),
                cr_side=round(contrast(side,WHITE),2), cr_acc=round(contrast(acc,WHITE),2), cr_dark=round(contrast(acc_dark,DARKBG),2), hue_gap=round(hue_d(acc_src),3),
                shift=round(abs(hls(acc)[1]-hls(acc_src)[1]),2))
if __name__=='__main__':
    P=json.load(open('lisa.json'))
    for p in P:
        p['colors']=list(dict.fromkeys(c.lower() for c in p['colors']))
        p['roles']=roles(p['colors'])
    json.dump(P,open('lisa_roles.json','w'),indent=1)
    for i,p in enumerate(P):
        r=p['roles']; print(f"{i:3} {p['artist'][:22]:22} {p['work'][:34]:34} side {r['sidebar']} acc {r['accent']} gap {r['hue_gap']} shift {r['shift']}")
