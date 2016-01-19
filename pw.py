#! python3
# pw.py Insecure password locker program.

import sys
import pyperclip

PASSWORDS = {'email': 'dbhjsadasdjSBBJKDFb', 'blog': 'BHBvhbdsvjdsvjsdshbv', 'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [accout] - copy account password')
    sys.exit()

account = sys.argv[1]  # acc name is first command line argument

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)