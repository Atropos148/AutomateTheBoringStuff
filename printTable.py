#! python3
# printTable.py

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData)
wideColumn = 0

def longestWordLenght(table, list):
    y = 0
    long = ''
    x = 0
    for x in range(len(tableData)):
        for y in range(len(tableData[x])):
            if len(tableData[x][y]) > len(long):
                long = tableData[x][y]
                colWidths[x] = len(long)
            else:
                long = long  # please don't judge me
            y += 1
        long = ''
        x += 1
    return colWidths

def tablePrint(table ,list):
    x = 0
    y = 0

    for y in range(len(tableData[y])):
        for x in range(len(tableData)):
            print(tableData[x][y].rjust(colWidths[x] + 1), end = ' ')
        print()


longestWordLenght(tableData, colWidths)
tablePrint(tableData, colWidths)
