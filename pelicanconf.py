#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"songhui"
SITENAME = u"Hui Song's Homepage"
SITEURL = ''

TIMEZONE = 'CET'

DEFAULT_LANG = 'en'

THEME = 'theme/notmymod'

# Blogroll
LINKS = (
		('MOD research group', 'http://modelbased.net'),
		('SINTEF ICT', 'http://www.sintef.no/home/Information-and-Communication-Technology-ICT/'),
		('PKU SEI', 'http://www.sei.pku.edu.cn/'),
		('TCD DSG', 'http://www.dsg.cs.tcd.ie/'),
		('NII', 'http://www.nii.ac.jp/en/')
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
