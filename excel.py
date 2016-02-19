#! python3
# readConsensusExcel

import os, openpyxl, logging, pprint

from openpyxl.cell import get_column_letter, column_index_from_string

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

path = '.\\excel\\'
if not os.path.exists(path):
    os.makedirs(path)
os.chdir(path)

print('Opening workbook...')
wb = openpyxl.load_workbook('census.xlsx')
print('Workbook opened...')
sheet = wb.get_sheet_by_name('Population by Census Tract')
print('Sheet found...')

countyData = {}

print('Reading rows...')
for row in range(2, sheet.get_highest_row() + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    # key for state exists
    countyData.setdefault(state, {})
    # key for this country in this state exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    # row == consensus tract, iterate
    countyData[state][county]['tracts'] += 1
    # add pop
    countyData[state][county]['pop'] += pop

# open txt file and write results
print('Writing results...')
resultsFile = open('census2010.py', 'w')
resultsFile.write('allData = ' + pprint.pformat(countyData))
resultsFile.close()
print('Done.')