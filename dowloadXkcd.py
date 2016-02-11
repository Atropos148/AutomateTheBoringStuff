#! python3
# downloadXkcd - downloads every XKCD comic

import logging, os, bs4, requests

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

url = 'http://www.xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # download page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # find url of comic image
    comicElem = soup.select('#comic img')
    if comicElem is []:
        print('Could not find the image.')

    else:
        logging.debug(url)
        try:
            comicUrl = comicElem[0].get('src')
            comicUrl="http:"+comicUrl
            if 'xkcd' not in comicUrl:
                comicUrl=comicUrl[:7]+'xkcd.com/'+comicUrl[7:]
            # download image
            print('Downloading image %s...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()

        except requests.exceptions.MissingSchema:
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue

        # save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # get the prev button url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
