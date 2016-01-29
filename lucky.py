#! python3
# lucky - googles command line argument and opens all results on separate tabs

import webbrowser,logging, sys, bs4, requests

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

print('Googling...') # display text while downloading the google page
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

# top search results
soup = bs4.BeautifulSoup(res.text)

# open the browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
