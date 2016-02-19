#! python3

import os, openpyxl

path = '.\\excel\\'
if not os.path.exists(path):
    os.makedirs(path)
os.chdir(path)

wb = openpyxl.load_workbook('cellInverter.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

wbNew = openpyxl.Workbook()
sheetNew = wbNew.get_sheet_by_name('Sheet')

soldList = {}

for row in range(1, sheet.max_row + 1):
    for col in range(1, 50):

        x = row
        y = col
        value = sheet.cell(row=x, column=y).value

        soldList.setdefault(x, {})
        soldList[x].setdefault(y, {value})

        sheetNew.cell(row=y, column=x).value = value

wbNew.save('cellInverterUpdate.xlsx')
