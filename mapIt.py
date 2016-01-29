#! python3
# mapIt - take Google maps link from clipboard and  open it in browser

import webbrowser,logging, sys, pyperclip

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

print('It lives!')
if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
    if sys.argv[1].lower() == 'good':
        print('And moves!')
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
