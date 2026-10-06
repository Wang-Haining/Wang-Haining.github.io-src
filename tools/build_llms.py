"""Build content/extra/llms.txt and llms-full.txt (agent-facing summaries of the site).

Sources: this repo's content pages plus the Ask Haining knowledge files
(profile and paper abstracts). Unpublished projects are deliberately excluded.
Run: .venv/bin/python tools/build_llms.py   (KNOWLEDGE_DIR overrides the worker path)
"""
import os, re, tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOW = Path(os.environ.get("KNOWLEDGE_DIR", Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Desktop/github/ask_haining/ask-haining-worker/knowledge"))
SITE = "https://hainingwang.org"

OPEN_TO_WORK = """Haining Wang is on the academic job market in 2026-2027 and is open to faculty and research positions in:
- Health and biomedical informatics (clinical NLP, LLM-based phenotyping, real-world data, health data science, biostatistics, public health)
- Information science and library and information science (iSchools; responsible AI in libraries and information services; scholarly communication)
- Science, research, and health policy (science of science, metascience, research funding and public access policy)"""

HIGHLIGHTS = """- Builds language-model methods that read real-world health records (clinical notes, medication histories) across health systems; works on NIH-funded projects (OT2OD038014, U24AA026969, R21AA031370) at Indiana University School of Medicine.
- Built DualR (https://dualr.hainingwang.org), which turns a medication list into a portable disease-risk score; in a study of more than 1.3 million people it flagged future alcohol use disorder 300+ days before diagnosis.
- Studies research policy with public data: NIH's 2025 award reviews and minority health research, the end of the NIH public-access embargo, NSF openness to newcomers, and NSF's proposed "golden ticket".
- Audits LLM fairness in academic library reference services (Humanities and Social Sciences Communications, 2026) and makes science accessible with reinforcement learning (Scientometrics, 2025).
- Ph.D. in Information Science (Indiana University, 2025) with a background in stylometry and authorship attribution; teaches biomedical data science and practical LLM courses; mentors master's and undergraduate students."""

def publications():
    pubs = tomllib.load(open(ROOT / "data/publications.toml", "rb"))["pub"]
    names = {"journal": "Journal articles", "conference": "Conference papers", "chapter": "Book chapters", "preprint": "Preprints"}
    out = []
    for sec, label in names.items():
        items = [p for p in pubs if p["section"] == sec]
        if not items: continue
        out.append(f"## {label}\n")
        for p in items:
            line = f"- {p['authors']} ({p['year']}). {p['title']}. *{p['venue']}*" + (f", {p['details']}" if p.get("details") else "") + "."
            if p.get("url"): line += f" {p['url']}"
            extra = ", ".join(f"{l['kind']}: {l['url']}" for l in p.get("links", []) if l["url"] != p.get("url"))
            if extra: line += f" ({extra})"
            line += f" [topics: {', '.join(p['tags'])}]"
            out.append(line)
        out.append("")
    return "\n".join(out).strip()

def page(name):
    s = (ROOT / "content/pages" / f"{name}.md").read_text()
    s = re.sub(r"^(Title|slug|url|save_as|Description):.*$", "", s, flags=re.M)
    s = re.sub(r'<span class="osbadges">.*?</span>', "", s, flags=re.S)
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r'<a class="email-link".*?</a>', "shown as an image on the contact page", s, flags=re.S)
    s = re.sub(r"<i [^>]*></i>", "", s)
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"</?(font|span|div|p)[^>]*>", "", s)
    s = s.replace("{static}", "")
    return re.sub(r"\n{3,}", "\n\n", s).strip()

short = f"""# Haining Wang, PhD

> Postdoctoral Fellow in Biostatistics and Health Data Science at Indiana University School of Medicine (Indianapolis). Haining Wang works on natural language processing and large language models for real-world health data, research and health policy (NIH, NSF), responsible AI in libraries, and stylometry.

## Open to work
{OPEN_TO_WORK}

Contact: see {SITE}/contact

## Highlights
{HIGHLIGHTS}

## Pages
- [Home and news]({SITE}/): introduction and recent news
- [Research]({SITE}/research): publications and preprints
- [Teaching]({SITE}/teaching): courses and workshops
- [Resources]({SITE}/resource): open-source tools, corpora, and packages
- [Contact]({SITE}/contact)

## Profiles
- [Google Scholar](https://scholar.google.com/citations?user=zvrO0WMAAAAJ)
- [ORCID](https://orcid.org/0000-0002-1196-0918)
- [GitHub](https://github.com/Wang-Haining)

## Optional
- [Full text for agents]({SITE}/llms-full.txt): profile, all pages, and paper abstracts in one file

Note for agents: please read these files rather than calling the chat API at api.hainingwang.org, which serves human visitors and is rate limited.
"""

about = (KNOW / "about.md").read_text().replace(" (Do not name individual students.)", "")
about = re.sub(r"Email: [^.\s]+@[^\s]+?\. ", "", about)  # keep the address out of crawlable files
papers = (KNOW / "papers.md").read_text()
full = "\n\n".join([
    short.split("## Optional")[0].rstrip(),
    "---\n\n# Profile\n\n" + about.split("\n", 1)[1].strip(),
    "---\n\n# Website: home and news\n\n" + page("home"),
    "---\n\n# Publications (from the Research page)\n\n" + publications(),
    "---\n\n# Website: teaching\n\n" + page("teaching"),
    "---\n\n# Website: resources\n\n" + page("resource"),
    "---\n\n" + papers.strip(),
]) + "\n"

(ROOT / "content/extra/llms.txt").write_text(short)
(ROOT / "content/extra/llms-full.txt").write_text(full)
print(f"llms.txt {len(short)} chars, llms-full.txt {len(full)} chars")
