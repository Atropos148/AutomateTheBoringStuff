#! python3

import os, openpyxl

pathTxt = '.\\excel\\txt\\'
if not os.path.exists(pathTxt):
    os.makedirs(pathTxt)
os.chdir(pathTxt)

fileList = os.listdir('.')

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')
fileNum = 1

for file in fileList:
    if file.endswith('.txt'):
        fileTxt = open(file)
        lines = fileTxt.read().splitlines()
        for lineNumber in range(len(lines)):
            sheet.cell(row=(lineNumber+1), column=fileNum).value = lines[lineNumber]
        fileTxt.close()
    fileNum += 1

wb.save('textOutput.xlsx')
