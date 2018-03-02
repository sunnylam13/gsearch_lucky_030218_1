# -*- coding: utf-8 -*-

#! python3
# ! /usr/local/Cellar/python3/3.6.1

import requests, sys, webbrowser, bs4, logging

logging.debug('Start of the factorial( %)' % (n))

print('Google searching...') # show some text while downloading

res = requests.get('https://www.google.ca/search?q=' + ' '.join(sys.argv[1:]))

res.raise_for_status()

# TODO:  retrieve top search result links

# TODO:  open a browser tab for each result

