# -*- coding: utf-8 -*-

#! python3
# ! /usr/local/Cellar/python3/3.6.1

import requests, sys, webbrowser, bs4, logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")

print('Google searching...') # show some text while downloading

logging.debug('Accessing Google results...')
res = requests.get('https://www.google.ca/search?q=' + ' '.join(sys.argv[1:]))

logging.debug('Confirming successful web page access...')
res.raise_for_status()

logging.debug('The response code is...')
logging.debug(res)

# retrieve top search result links

logging.debug('Retrieving top search results from data object...')
soup = bs4.BeautifulSoup(res.text,"html.parser")

# open a browser tab for each result

logging.debug('Select all link elements...')
linkElems = soup.select('.r a') # select all <a> link elements with a CSS class of `r`

numOpen = min(5,len(linkElems))

logging.debug('Opening all chosen links in the web browser...')
for i in range(numOpen): # might have fewer results, opens whichever is smaller, using the min() function
	webbrowser.open('https://google.com' + linkElems[i].get('href'))

