# inventory.py
#enumerate的说明
#https://blog.csdn.net/churximi/article/details/51648388
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonloot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuffnew = {'gold coin':142, 'rope':1, 'health':3}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))
#display_inventory(stuff)

def addtoinventory(inventory, addeditems):
	for i in addeditems:
		if i in inventory.keys():
			inventory[i] = inventory[i] + 1
		else:
			inventory[i] = 1

addtoinventory(stuff, dragonloot)
#display_inventory(stuff)

def mergestuff(stuff,stuffadd):
	## add which allraedy known
	for k1 in stuff.keys():
		for k2 in stuffadd.keys():
			if k2 == k1:
				stuff[k1] = stuff[k1] + stuffadd[k2]
			else:
				pass
	for k2 in stuffadd.keys():
		if k2 not in stuff.keys():
			stuff[k2] = stuffadd[k2]
		else:
			pass

mergestuff(stuff, stuffnew)
display_inventory(stuff)

#lack enumerate methord