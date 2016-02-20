import os, openpyxl, csv

path = './excelTest/'
os.makedirs(path, exist_ok=True)
os.chdir(path)

for excelFile in os.listdir('.'):
    # skip non xlsx files
    if not excelFile.endswith('.xlsx'):
        continue

    wb = openpyxl.load_workbook(excelFile)
    
    for sheetName in wb.get_sheet_names():
        # Loop through every sheet in the workbook
        sheet = wb.get_sheet_by_name(sheetName)
        
        # Create CSV filename by combining excel filename and sheet name
        excelFileFixed = excelFile[:-5]
        csvFilename = excelFileFixed + sheetName + '.csv'
        
        # Create csv.writer for this CSV
        csvFileObj = open(csvFilename, 'w', newline='')
        writer = csv.writer(csvFileObj, delimiter=' ')
        
        # Loop through every row in the sheet
        for rowNum in range(1, sheet.max_row + 1):
            rowData = [] # append each cell to this list
            # Loop through each cell in the row
            for colNum in range(1, sheet.max_column + 1):
                # Append each cell's data to rowData
                rowData.append(sheet.cell(row=rowNum, column=colNum).value)
                
            # Write rowData list to csv file
            for row in rowData:
                print(row)
                writer.writerow([row])
                
        csvFileObj.close()

print('Done')
