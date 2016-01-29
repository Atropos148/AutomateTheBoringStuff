#! python3
# coinToss - debugging challenge

import random, logging

logging.basicConfig(level=logging.DEBUG, format= ' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

guess = ''

while guess not in('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()


toss = random.randint(0, 1) #0 is heads, 1 is tails

logging.debug('toss is ' + str(toss))

if toss == 1:
    toss = 'tails'
if toss == 0:
    toss = 'heads'

logging.debug('toss is ' + str(toss))

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = ''
    while guess not in('heads', 'tails'):
        print('Enter heads or tails:')
        guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('No. You are bad at this game.')
