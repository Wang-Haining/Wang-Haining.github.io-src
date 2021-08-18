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
                  <br> <font size="4">information science</font>
                  <br> <font size="4">computational linguistics</font>
                  <br>
                  <br>
                  <br> <font size="4">PhD student, ILS@IUB</font>
                  <br>
                  <br> Bloomington, IN, USA"""
SITEDESCRIPTION = "I'm a doctoral student in the Department of Information & Library Science at Indiana University Bloomington."
SITEURL = 'https://Wang-Haining.github.io'
SITELOGO = "/images/profile.png"
FAVICON = "/images/favicon.ico"
BROWSER_COLOR = '#333333'

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
TYPOGRIFY = True

# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# ROBOTS = "index, follow"

CUSTOM_CSS = "static/custom.css"
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    "extra/custom.css": {"path": "static/custom.css"},
}

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True

LINKS_IN_NEW_TAB = 'external'

SOCIAL = (
    ('envelope', 'mailto:hw56 (AT) indiana.edu'),
    ('github', 'https://github.com/Wang-Haining'),
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
]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MENUITEMS = (('Research', "/research"),
            ('Resource', "/resource"),
             ('Contact', "/contact")
            # ('Blog', '/blog/')
             )
# code hilighting
PYGMENTS_STYLE = "monokai"

GITHUB_URL = 'https://github.com/Wang-Haining/Wang-Haining.github.io-src'


ARTICLE_HIDE_TRANSLATION = False

DISPLAY_CATEGORIES_ON_MENU = False
# USE_FOLDER_AS_CATEGORY = True

LOAD_CONTENT_CACHE = False
FILENAME_METADATA = '(?P<title>.*)'
DELETE_OUTPUT_DIRECTORY = False

OUTPUT_RETENTION = [".gitignore", ".git"]
OUTPUT_PATH = 'output/blog'
INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'

# OUTPUT_PATH = 'output'
# INDEX_SAVE_AS = 'index.html'
# INDEX_URL = '/'

# STATIC_PATHS = ["extra/custom.css"]
# CUSTOM_CSS = "static/custom.css"
# # Enable i18n plugin.
# PLUGINS = ["i18n_subsites"]
# # Enable Jinja2 i18n extension used to parse translations.
# JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}