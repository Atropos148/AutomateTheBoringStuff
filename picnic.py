def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwitch':4, 'apple': 12, 'cup': 4}

printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
