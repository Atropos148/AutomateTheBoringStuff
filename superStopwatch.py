#! python3
# superStopwatch.py 

import time

print('Press Enter to start counting, then Enter for each lap. \nLap times will show current lap time and overall time. Press Ctrl-C to quit.')

input() # enter to begin
print('Started.')
startTime = time.time() # first lap time
lastTime = startTime
lapNum = 1

# tracking the lap times

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: Lap: %s Time: %s' % (lapNum, lapTime, totalTime), end='')
        lapNum += 1
        lastTime = time.time() # reset
except KeyboardInterrupt:
    # Handle the Ctrl-C
    print('\nDone.')
