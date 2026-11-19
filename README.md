# Wang-Haining.github.io-src

My personal website.
Built with [Pelican](https://getpelican.com/); the rendered site lives in the `output` submodule.

Build: `pelican content -o output -s publishconf.py`, then `python tools/check_seo.py output`.
If `content/pages/home.md` or `about.md` changes, regenerate `llms-full.txt` with `python tools/build_llms.py`.
