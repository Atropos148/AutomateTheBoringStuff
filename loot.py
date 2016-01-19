dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'skull', 'dagger']
bag = {'gold coin': 1, 'rope': 1}


def displayInventory(bag):
    print("Inventory:")
    item_total = 0
    for k, v in bag.items():
        if v > 1:
            print(str(v) + ' ' + k + 's')
        else:
            print(str(v) + ' ' + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))


def addToInventory(bag, addedItems):
    x = 0
    addedItems = []
    for x in range(len(dragonLoot)):
        addedItems.append(dragonLoot[x])
        x += 1
        
    for x in range(len(addedItems)):
        if addedItems[x] not in bag:
            bag.setdefault(addedItems[x],1)
        elif addedItems[x] in bag:
            bag[addedItems[x]] += 1

    return bag

#BODY
bag = addToInventory(bag, dragonLoot)
displayInventory(bag)
