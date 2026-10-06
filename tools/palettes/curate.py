import json
from roles import hex2rgb, rgb2hex, contrast, adjust_l, mix, WHITE, DARKBG, hls
TEXT=hex2rgb('#242121')
# (work, artist, sidebar, accent, light)  -- all colors are Color Lisa palette colors
C=[
 ("The Starry Night","Vincent van Gogh","#1a3431","#2b41a7","#ccc776"),
 ("The Great Wave off Kanagawa","Katsushika Hokusai","#1f284c","#2d4472","#d9ccac"),
 ("Water Lilies","Claude Monet","#395a92","#9f4640","#7ea860"),
 ("Woman with a Parasol","Claude Monet","#4c7899","#2f5136","#b1b94c"),
 ("Girl with a Pearl Earring","Johannes Vermeer","#707da6","#b08e4a","#ccad9d"),
 ("The Kiss","Gustav Klimt","#4a5fab","#a27cba","#e3c454"),
 ("Night Windows","Edward Hopper","#3f6148","#67161c","#dbd3a4"),
 ("Bedroom in Arles","Vincent van Gogh","#374d8d","#82a866","#c4b743"),
 ("A Sunday on La Grande Jatte","Georges Seurat","#465946","#3f3f63","#8c9355"),
 ("The Birth of Venus","Sandro Botticelli","#7a989a","#cf9546","#c1ae8d"),
 ("The Arnolfini Portrait","Jan van Eyck","#3b5b71","#3c490c","#7c6c4e"),
 ("The Swan","Hilma af Klint","#466ca6","#87240e","#d1ae45"),
 ("The Persistence of Memory","Salvador Dalí","#40798c","#805730","#bfb37f"),
 ("The Son of Man","René Magritte","#3a282f","#b60614","#e3bfa1"),
 ("Dance (I)","Henri Matisse","#165f8c","#03735e","#078c66"),
 ("Landscape at Collioure","Henri Matisse","#375c8c","#bf7821","#bfaa8f"),
 ("A Bigger Splash","David Hockney","#126599","#497e58","#79bed9"),
 ("Abstraction Blue","Georgia O'Keeffe","#182044","#51628e","#91a1ba"),
 ("The Night Watch","Rembrandt","#5b5224","#8a350c","#dbc99a"),
 ("Broadway Boogie Woogie","Piet Mondrian","#314290","#4a71c0","#f0d32d"),
 ("Villa di Marlia, Lucca","John Singer Sargent","#4e6a3d","#778bd0","#e2d76b"),
 ("American Gothic","Grant Wood","#41240b","#9c4823","#a6bdb0"),
 ("White Zig Zags","Wassily Kandinsky","#4052bd","#c13c53","#efe96d"),
 ("Les Demoiselles d'Avignon","Pablo Picasso","#566c7d","#a1544b","#dd9d91"),
 ("Large Green Vase with Mixed Flowers","Odilon Redon","#4d5e30","#695b8f","#c2af46"),
 ("George Lawson and Wayne Sleep","David Hockney","#3e797a","#a63f5a","#f2e7ae"),
 ("Hommage à Blériot","Robert Delaunay","#4368b6","#e4930a","#dec23b"),
 ("The Creation of Adam","Michelangelo","#42819f","#86aa7d","#cbb396"),
]
def until(c,cond,step): return adjust_l(hex2rgb(c) if isinstance(c,str) else c,cond,step)
out=[]
for work,artist,side,acc,light in C:
    s=until(side,lambda r: contrast(r,WHITE)>=4.6,-0.01)
    a=until(acc,lambda r: contrast(r,WHITE)>=4.6,-0.01)
    # if accent is very dark, lift it so it still reads as a link (target ~ 7:1)
    if contrast(a,WHITE)>8: a=until(a,lambda r: contrast(r,WHITE)<=7.2,+0.01)
    hov=until(a,lambda r: contrast(r,WHITE)<=3.4,+0.01)
    ad=until(acc,lambda r: contrast(r,DARKBG)>=4.6,+0.01)
    sel=hex2rgb(light); t=0.0
    while contrast(mix(sel,WHITE,t),TEXT)<10 and t<1: t+=0.02
    sel=mix(sel,WHITE,t)
    chip=mix(s,WHITE,0.16)
    out.append(dict(work=work,artist=artist,src=[side,acc,light],
        sidebar=rgb2hex(s),accent=rgb2hex(a),hover=rgb2hex(hov),accentDark=rgb2hex(ad),selection=rgb2hex(sel),chip=rgb2hex(chip),
        check=dict(side=round(contrast(s,WHITE),2),acc=round(contrast(a,WHITE),2),hover=round(contrast(hov,WHITE),2),dark=round(contrast(ad,DARKBG),2),sel=round(contrast(sel,TEXT),2))))
json.dump(out,open('curated.json','w'),indent=1,ensure_ascii=False)
for o in out: print(f"{o['work'][:28]:28} side {o['sidebar']}({o['check']['side']}) acc {o['accent']}({o['check']['acc']}) hov {o['hover']} dark {o['accentDark']}({o['check']['dark']}) sel {o['selection']}")
