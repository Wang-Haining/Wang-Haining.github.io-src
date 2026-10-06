"""Pre-publish SEO check over built HTML. Usage: .venv/bin/python tools/check_seo.py output"""
import sys, json, glob, os
from html.parser import HTMLParser

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.tags = []; s.text = {}; s.stack = []
    def handle_starttag(s, t, a):
        s.tags.append((t, dict(a)))
        if t not in ("meta", "link", "img", "br", "input", "hr"): s.stack.append(len(s.tags) - 1)
    def handle_endtag(s, t):
        if s.stack: s.stack.pop()
    def handle_data(s, d):
        if s.stack: s.text[s.stack[-1]] = s.text.get(s.stack[-1], "") + d

bad = 0
for f in sorted(glob.glob(os.path.join(sys.argv[1], "*.html"))):
    if os.path.basename(f).startswith("google"): continue  # Search Console verification file
    p = P(); p.feed(open(f).read()); T = p.tags
    meta = lambda k, v: [a for t, a in T if t == "meta" and a.get(k) == v]
    titles = [p.text.get(i, "").strip() for i, (t, a) in enumerate(T) if t == "title"]
    h1 = [i for i, (t, a) in enumerate(T) if t == "h1"]
    h1_text = ["".join(p.text.get(j, "") for j in range(i, min(i + 3, len(T)))).strip() for i in h1]
    ld = [p.text.get(i, "") for i, (t, a) in enumerate(T) if t == "script" and a.get("type") == "application/ld+json"]
    try: [json.loads(x) for x in ld]; ld_ok = len(ld) == 1
    except ValueError: ld_ok = False
    canon = [a["href"] for t, a in T if t == "link" and a.get("rel") == "canonical"]
    checks = {
        "title": len(titles) == 1 and titles[0] != "",
        "description": len(meta("name", "description")) == 1,
        "canonical": len(canon) == 1 and canon[0].startswith("https://"),
        "og:url": len(meta("property", "og:url")) == 1,
        "og:type": len(meta("property", "og:type")) == 1,
        "og:image": len(meta("property", "og:image")) == 1 and meta("property", "og:image")[0]["content"].startswith("https://"),
        "robots": any(a.get("content", "").startswith("index, follow") for a in meta("name", "robots")),
        "one h1": len(h1) == 1 and all(h1_text),
        "img alt": all(a.get("alt") for t, a in T if t == "img"),
        "json-ld": ld_ok,
    }
    fails = [k for k, v in checks.items() if not v]; bad += len(fails)
    print(f"{os.path.basename(f):15} {titles[0][:60] if titles else '-':60} {canon[0] if canon else '-':34} {'FAIL ' + ', '.join(fails) if fails else 'ok'}")
print("failures:", bad); sys.exit(1 if bad else 0)
