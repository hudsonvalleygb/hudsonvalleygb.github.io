#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'HVGB'
SITENAME = 'Hudson Valley Ghostbusters'
SITEURL = 'hudsonvalleygb.github.io'

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
LINKS = (('Store', "https://www.storefrontier.com/hudsonvalleyghostbusters?type&fbclid=IwAR2SpHuv9f6i3nAT1836XsrwDYacWV8ptv6n2F5K93TdygCDdr0bqHdhM8w"),)

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

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['photos']
PHOTO_LIBRARY = "/Users/pnatale/repos/hudsonvalleygb.github.io/Pelican/content/images"

DEFAULT_PAGINATION = False
DISPLAY_CATEGORIES_ON_MENU = False
PAGE_ORDER_BY = "sort_order"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
