#! python3
# renameDates.py - change US dates to EU dates

import re, os, shutil

usFilesFolder = '.\\usFiles'

# regex for US dates

datePattern = re.compile(r"""^(.*?)
                         ((0|1)?\d)-
                         ((0|1|2|3)?\d)-
                         ((19|20)\d\d)
                         (.*?)$
                        """, re.VERBOSE)

# loop over files
for usFilename in os.listdir(usFilesFolder):
    dateRX = datePattern.search(usFilename)

# skip files without a date
    if dateRX is None:
        continue

# get the different parts of filename
    beforePart = dateRX.group(1)
    monthPart = dateRX.group(2)
    dayPart = dateRX.group(4)
    yearPart = dateRX.group(6)
    afterPart = dateRX.group(8)

# make EU date format
    euFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# get full absolute path
    absWorkingDir = os.path.abspath(usFilesFolder)
    usFilename = os.path.join(absWorkingDir, usFilename)
    euFilename = os.path.join(absWorkingDir, euFilename)

# rename the files
    print('Renaming "%s" to "%s"...' % (usFilename, euFilename))
    shutil.move(usFilename, euFilename)