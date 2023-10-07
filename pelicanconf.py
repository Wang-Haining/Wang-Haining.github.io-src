#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
import os

AUTHOR = 'Haining Wang 王海宁'
SITENAME = "Home"
SITESUBTITLE = """<br>
                  <br>
                  <br><font size="5">Haining Wang 王海宁</font><br> <br>   
                  <br> <font size="4">Information Science</font>
                  <br> <font size="4">Data Science</font>
                  <br>
                  <br>
                  <br> <font size="4">PhD student, ILS@IUB</font>
                  <br>
                  <br> Bloomington, IN
                  <br> USA"""
SITEDESCRIPTION = "I'm a doctoral student in the Department of Information & Library Science at Indiana University Bloomington."
SITEURL = 'https://Wang-Haining.github.io'
SITELOGO = "/images/profile.png"
FAVICON = "/images/favicon.ico"
BROWSER_COLOR = '#333'

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
COPYRIGHT_NAME = 'ISC'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

# PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = ['post_stats']

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

# CUSTOM_CSS = "static/custom.css"
# CUSTOM_CSS = "../pelican-themes/Flex/static/stylesheet"
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    # "extra/custom.css": {"path": "static/custom.css"},
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

SOCIAL = (
    ('envelope', 'mailto:hw56 (AT) indiana.edu'),
    ('github', 'https://codeberg.org/haining/'),
    ('facebook', 'https://www.facebook.com/haining.wang.56/'),
    ('twitter', 'https://twitter.com/Haining_Wang_'),
)

LINKS = ()


# SEO
SITE_DESCRIPTION = (
    "Haining Wang, Indiana University Bloomington, IUB, information science, computational linguistics, NLP"
)

AUTHORS = {
    "Haining Wang": {
        "url": "https://www.hainingwang.com/",
        "blurb": "is a learner in information and computational sciences.",
        "avatar": "/images/avatar.png",
    },
}
# DISQUS_FILTER = True
# UTTERANCES_FILTER = True
# COMMENTBOX_FILTER = True

# Static files
STATIC_PATHS = [
    'images',
    'pages',
    'extra/CNAME'
]

# settings.py
SEO_REPORT = True  # To enable this feature
SEO_ENHANCER = True  # To disable this feature
SEO_ENHANCER_OPEN_GRAPH = True # The default value for this feature
SEO_ENHANCER_TWITTER_CARDS = True # The default value for this feature

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MENUITEMS = (('Research', "/research"),
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
INDEX_SAVE_AS = 'index.html'
