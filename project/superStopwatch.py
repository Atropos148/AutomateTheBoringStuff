#! python3
# superStopwatch.py - Simple stopwatch

import time

#Display instructions

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.\nPress Ctrl-C to quit.')
input() # press ENTER to begin
print('Started...')
startTime = time.time()
lastTime = startTime
lapNum = 1

# start tracking lap times

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print ('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() #reset the last lap time

except KeyboardInterrupt:
    #Handle the Ctrl-C exception to keep its error message from displaying
    print('\nDone.')
