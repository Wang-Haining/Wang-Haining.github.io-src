# Palette of the day

The site rotates one painting palette per day (inline script in `templates/base.html`).

- `lisa.json`: 133 palettes scraped from Color Lisa (https://colorlisa.com/).
- `roles.py`: color math (WCAG contrast, lightness adjustment).
- `curate.py`: the 28 hand-picked paintings and which painting color plays sidebar / link / highlight; computes contrast-safe values into `curated.json`.
- `pop.py`: adds the contrasting "pop" color (and its text color) used by the Ask Haining widget.

To change palettes: edit the list in `curate.py`, run `python3 curate.py && python3 pop.py`, then regenerate the `var P = [...]` array in `templates/base.html` from `curated.json`
(fields: work, artist, sidebar, chip, accent, hover, accentDark, selection, pop, popInk). Preview any palette with `?palette=N`.
