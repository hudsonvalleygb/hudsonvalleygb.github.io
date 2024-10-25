#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'HVGB'
SITENAME = 'Hudson Valley Ghostbusters'
SITEURL = 'https://hudsonvalleyghostbusters.org'
# SITEURL = 'hudsonvalleygb.github.io'
#SITEURL = ''
SITE_SUMMARY = 'Hudson Valley Ghostbusters, a 501(c)(3) non-profit, dedicated to having fun while doing good'
SITE_LOGO = 'HVGB_logo_transparent.png'
#SITE_LOGO = 'HVGB_logo_pride_transparent.png'
THEME = 'theme'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Store', "https://www.redbubble.com/people/hudsonvalleygb/shop"), ('Linktree', "https://linktr.ee/HVGhostbusters"), ('Hudson Valley Slime Time', 'https://www.youtube.com/playlist?list=PLZfgEVgjj4cFUv3wtB3UbJ13rmXrS8tea'),)

STATIC_PATHS = [
    'images',
    'extra'
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/HV.Ghostbusters/'),
          ('instagram', 'https://www.instagram.com/hudsonvalley_ghostbusters/'),
          ('twitter', 'https://twitter.com/HVGhostbusters'),)

#PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['photos', 'sitemap', 'pelican_redirect']
#PHOTO_LIBRARY = "/home/peter/repos/hudsonvalleygb.github.io/Pelican/content/images"
#PHOTO_LIBRARY = "/home/pnatale/repos/hudsonvalleygb.github.io/Pelican/content/images"
PHOTO_LIBRARY = "/Users/pete.natale/repos/hudsonvalleygb.github.io/Pelican/content/images"
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.3,
        'indexes': 0.5,
        'pages': 0.7
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    },
    'exclude': ['tag/', 'category/', 'author/']
}

DEFAULT_PAGINATION = False
DISPLAY_CATEGORIES_ON_MENU = False
PAGE_ORDER_BY = "sort_order"
API_KEY = "3b974f3ccb23633eb1dd640aae473cd0"
PHOTO_RESIZE_JOBS = -1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
