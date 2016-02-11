#! python3
# FAILED PROJECT

import os, re, logging, shutil

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

folder = '.'

numbersRx = re.compile(r'(\D+)(\d+)')

fileList = []
print(fileList)

for foldername, subfolders, filenames in os.walk(folder):
    if foldername == '.\gapFolder':
        for filename in filenames:
            fileList.append(filename)

#logging.debug(fileList)

number = 1
testFileNameBase = numbersRx.search(fileList[0]).group(1)

for x in range(5):
    testFileNames = []
    number = 1
    for x in range(len(fileList)):
        testFileName = testFileNameBase + '00' + '%s' % number + '.txt'
        testFileNames.append(testFileName)
        number += 1

    enumFileList = enumerate(fileList)
    for pos, filename in enumerate(testFileNames):
        if filename in fileList:
            print(str(pos) + ' ' + filename + ' found...')
        else:
            print(str(pos) + ' ' + filename + ' not found...')

            lowerFilenameBase = (numbersRx.search(filename).group(2))
            lowerFilename = testFileNameBase + str(lowerFilenameBase) + '.txt'

            print('Renaming ' + fileList[pos] + ' to ' + lowerFilename)

            posOfFileListFile = '.\gapFolder' + '\\' + fileList[pos]
            openThisToRenameFile = os.path.abspath(posOfFileListFile)

            lowerFilenameAbsPath = '.\gapFolder' + '\\' + lowerFilename
            renameToThis = os.path.abspath(lowerFilenameAbsPath)

            open(openThisToRenameFile)
            shutil.move(openThisToRenameFile, renameToThis)
