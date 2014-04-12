#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"tBunnyMan"
SITENAME = u"Hui Song's Homepage"
SITEURL = ''

TIMEZONE = 'CET'

DEFAULT_LANG = 'en'

THEME = 'theme/notmymod'

# Blogroll
LINKS = (
		('SINTEF ICT', 'http://www.sintef.no/home/Information-and-Communication-Technology-ICT/'),
		('SINTEF', 'http://www.sintef.no/home'),
		('MOD research group', 'http://modelbased.net'),
        ('Pelican', 'http://blog.getpelican.com')
    )

# Social widget
SOCIAL = (('LinkedIn', 'http://no.linkedin.com/pub/hui-song/24/2b0/413'),
		  ('GooglePlus','https://plus.google.com/104535812896658559609/posts')
          )

DEFAULT_PAGINATION = 5

# Put pages in root
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'

# And sort my articles
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
