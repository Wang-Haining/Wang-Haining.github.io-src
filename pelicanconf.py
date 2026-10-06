#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
import os

AUTHOR = 'Haining Wang'
SITENAME = "Haining Wang"
SITETITLE = "Haining Wang, Ph.D."
SIDEBAR_GROUPS = [
    ["Postdoctoral Fellow"],
    ["Biostatistics & Health Data Science"],
    ["School of Medicine", "Richard M. Fairbanks School of Public Health", "Indiana University"],
]
HOME_TITLE = "Haining Wang, PhD | NLP and Health Data Science | Indiana University"
SITEDESCRIPTION = ("Haining Wang, PhD, is a postdoctoral fellow in Biostatistics and Health Data Science at "
                   "Indiana University School of Medicine (IU). Haining builds NLP and large language model methods for "
                   "real-world health data, and studies research policy, AI fairness in libraries, and stylometry.")
SITEURL = 'https://hainingwang.org'
SITELOGO = "/images/profile.png"
FAVICON = "/images/favicon.ico"
BROWSER_COLOR = '#5c8374'

USE_GOOGLE_FONTS = True
HOME_HIDE_TAGS = True
DISABLE_URL_HASH = True

MAIN_MENU = True

PATH = 'content'

# Regional Settings
TIMEZONE = 'America/Indiana/Indianapolis'
DATE_FORMATS = {"en": "%b %d, %Y"}

# License
COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = '0BSD'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

# No plugins: explicit [] stops Pelican from auto-loading installed namespace plugins
# (pelican-seo was silently injecting duplicate canonical/OG/JSON-LD tags).
PLUGINS = []

DISPLAY_PAGES_ON_MENU = False
DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 175

# Appearance
THEME = "../pelican-themes/Flex"
# TYPOGRIFY = True

# Feeds
FEED_ALL_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None



# ROBOTS = "index, follow"

CUSTOM_CSS = "static/custom.css?v=3"
# CUSTOM_CSS = "../pelican-themes/Flex/static/stylesheet/dark-theme.min.css"
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/chat-widget.js": {"path": "static/chat-widget.js"},
    "extra/site.js": {"path": "static/site.js"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/google6a4ae6271ad574af.html": {"path": "google6a4ae6271ad574af.html"},  # Google Search Console ownership; keep
    "extra/llms.txt": {"path": "llms.txt"},
    "extra/llms-full.txt": {"path": "llms-full.txt"},
    "extra/custom.css": {"path": "static/custom.css"},
}

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True

LINKS_IN_NEW_TAB = 'external'

# Social widget
# SOCIAL = (
#         ('GitHub', 'https://github.com/Wang-Haining'),
#         # ('Facebook', 'https://www.facebook.com/haining.wang.56/'),
#         # ('Twitter', 'https://twitter.com/Haining_Wang_'),
#         # ('Email', 'hw56@indiana.edu')
# )

SOCIAL = ()
SIDEBAR_LINKS = [  # (icon classes, url, label)
    ("fa-solid fa-envelope", "mailto:hw56@iu.edu", "Email"),
    ("fa-solid fa-graduation-cap", "https://scholar.google.com/citations?user=zvrO0WMAAAAJ", "Google Scholar"),
    ("fa-brands fa-github-alt", "https://github.com/Wang-Haining", "GitHub"),
]
SAME_AS = [
    "https://scholar.google.com/citations?user=zvrO0WMAAAAJ",
    "https://orcid.org/0000-0002-1196-0918",
    "https://github.com/Wang-Haining",
    "https://twitter.com/Haining_Wang_",
]
KNOWS_ABOUT = [
    "Natural language processing", "Large language models", "Clinical NLP", "Computational phenotyping",
    "Electronic health records", "Real-world data", "Health data science", "Medical informatics",
    "Health disparities", "Social determinants of health", "Metascience", "Science of science", "Research policy",
    "NIH and NSF funding", "Open access and public access policy", "AI fairness", "Library reference services",
    "Accessible science communication", "Stylometry", "Authorship attribution", "Adversarial stylometry",
]
BUILD_DATE = datetime.now().strftime("%Y-%m-%d")
ROBOTS = "index, follow, max-image-preview:large"

LINKS = ()


# SEO
SITE_DESCRIPTION = (
    "Haining Wang, Indiana University, IU School of Medicine, information science, natural language processing, language modeling, data science, machine learning, deep learning, biomedical informatics, computational humanities, computational social sciences, artificial intelligence, AI, data science, health data science"
)

# DISQUS_FILTER = True
# UTTERANCES_FILTER = True
# COMMENTBOX_FILTER = True

# Static files
STATIC_PATHS = [
    'images',
    'pages',
    'extra/CNAME',
    "extra/robots.txt",
    "extra/google6a4ae6271ad574af.html",
    "extra/llms.txt",
    "extra/llms-full.txt",
    "extra/site.js",
    "extra/chat-widget.js",
    "extra/custom.css"
]


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MENUITEMS = (('Research', "/research"),
             ('Teaching', "/teaching"),
             ('Resource', "/resource"),
             ('Contact', "/contact")
            # ('Blog', '/blog/')
             )
# code highlighting
PYGMENTS_STYLE = "monokai"

GITHUB_URL = 'https://github.com/Wang-Haining/Wang-Haining.github.io-src'


ARTICLE_HIDE_TRANSLATION = False

DISPLAY_CATEGORIES_ON_MENU = False
# USE_FOLDER_AS_CATEGORY = True

LOAD_CONTENT_CACHE = False
FILENAME_METADATA = '(?P<title>.*)'
DELETE_OUTPUT_DIRECTORY = False

OUTPUT_RETENTION = [".gitignore", ".git"]

# OUTPUT_PATH = 'output/blog'
# INDEX_SAVE_AS = 'blog/index.html'
# INDEX_URL = 'blog/'

OUTPUT_PATH = 'output'
# Pages only: no blog index, tag, category, author, or archive pages.
DIRECT_TEMPLATES = []
INDEX_SAVE_AS = ''
TEMPLATE_PAGES = {'sitemap.xml': 'sitemap.xml'}

# Template overrides (chat widget injection)
THEME_TEMPLATES_OVERRIDES = ['templates']
# Treat .html files under content/ as static files (e.g., the Search Console verification file), not pages.
READERS = {"html": None}
