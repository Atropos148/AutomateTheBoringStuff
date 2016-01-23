#! python3
# madLibs.py - Write your own lyrics, man!
# Instructions on screen!

import os, re

path = '.\\madLibs'
i = 1
if not os.path.exists(path):
    os.makedirs('.\\madLibs')

madLibsFile = open('.\\madLibs\\madLibs1.txt', 'r')
while True:
    if os.path.isfile('.\\madLibs\\madlibs%sUser.txt' % i):
        i += 1
    else:
        madLibsFileUser = open('.\\madLibs\\madLibs%sUser.txt' % i, 'w')
        break

adjective = 'ADJECTIVE'
noun = 'NOUN'
verb = 'VERB'
adverb = 'ADVERB'


madLibsFileRead = madLibsFile.readlines()
print(madLibsFileRead[0])

for word in madLibsFileRead[0].split(' '):
    removeDotsRX = re.sub(r'[\.]+?', '', word)

    if removeDotsRX == adjective:
        print('Enter an adjective:')
        adjectiveInput = input()
        madLibsFileUser.write(adjectiveInput + ' ')

    elif removeDotsRX == noun:
        print('Enter a noun:')
        nounInput = input()
        madLibsFileUser.write(nounInput + ' ')

    elif removeDotsRX == verb:
        print('Enter a verb:')
        verbInput = input()
        madLibsFileUser.write(verbInput + ' ')

    elif removeDotsRX == adverb:
        print('Enter an adverb:')
        adverbInput = input()
        madLibsFileUser.write(adverbInput + ' ')

    else:
        madLibsFileUser.write(word + ' ')

madLibsFile.close()
