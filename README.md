# Lucky Google Search

The program searches for a search term supplied through the command line and has the computer automatically open the browser with all the top search results in new tabs.

## What It Does

* gets search keywords from command line arguments

* gets the search results page

* opens a browser tab for each result

## What the Code Does

* read the command line from `sys.argv`

* grab the search result page with the `requests` module

* find the links to each search result

* call the `webbrowser.open()` function to open the web browser

## Resources and References

ABSP:  413

