#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
#                      file directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files
    print('Removing header from ' + csvFilename + '...')

    # Read the CSV file (skip first row)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # skip first line
        csvRows.append(row)
    csvFileObj.close()

    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',  newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
