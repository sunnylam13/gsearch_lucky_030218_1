try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'The program searches for a search term supplied through the command line and has the computer automatically open the browser with all the top search results in new tabs.',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/gsearch_lucky_030218_1',
	'download_url': 'https://github.com/sunnylam13/gsearch_lucky_030218_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['os,requests,webbrowser'],
	'scripts': [],
	'name': 'Lucky Google Search'
}

setup(**config)