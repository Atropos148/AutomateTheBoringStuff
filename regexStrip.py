#! python3
# regexStrip.py - takes one or two arguments
# if only one whitespaces if front and behind the string are removed
# else it second string will be removed from the first

import sys, re

while True:
    print('Give me a string to strip!(exit to stop)')
    first = input('')
    if first == 'exit':
        break
    print('')
    print('Your String:')
    print(first)
    print('Press Enter to remove whitespaces')
    print(' or type another string to remove')
    second = input('')

    if second != '':
        removeStringRX = re.sub(second, '', first)
        print(removeStringRX)
        input('')

    elif second == '':
            removeSpacesRX = re.sub(r'[\s]+?', '', first)
            print(removeSpacesRX + '.')
            input('')
