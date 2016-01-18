dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addedItems = {}

bag = {'gold coin': 1, 'rope': 1}

def displayInventory(bag):
    print("Inventory:")
    item_total = 0
    for k, v in bag.items():
        print(k + ' ' + str(v))
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

def addToInventory(bag, addedItems):
	x = 0
	for dragonLoot[x] in dragonLoot:
		if dragonLoot[x] in bag:
			print(dragonLoot[x])
			x += 1
		else:
			print('is not')
			addedItems.append(dragonLoot[x])
			x += 1

bag = addToInventory(bag, dragonLoot)
displayInventory(bag)
input()