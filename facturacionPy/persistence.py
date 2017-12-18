import random
from json import loads
from json import dump

def loadData(count=0):
	depot = loads(open("outfile.json").read())
	
	continueShopping = True
	
	print("Bienvenido a FIS Shop!")
	print("-"*40)
	
	while continueShopping is True:
		loadData(message="Shop Inventory",
						 inventory=shopInventory,
						 values=itemValues)
		loadData(message="Seller Inventory",
						 inventory=sellerInventory,
						 values=itemValues,
						 count=itemCount)
	
	print("-"*40)
	print(message)
	print("-"*40)
	
	for itemIndex, itemData in enumerate(sorted(inventory.items())):
		itemIndex = itemIndex + count
		itemName, itemQuantity = itemData
		itemValue = Values.get(itemName, "SIN STOCK")
		if itemValue == "SIN STOCK":
			print("{}: {} es {} y no esta disponible.".format(itemIndex, itemName, \
				itemValue))
		else:
			print("{}: {} vale ${} y nos quedan {}.".format(itemIndex, itemName, \
				itemValue))
			
		print("-"*40)
		
def saveData():
	depot = []
	itemNames = {}
	
	itemNames[0] = input("Primer producto: ")
	itemNames[1] = input("Segundo producto: ")
	itemNames[2] = input("Tercer producto: ")
	itemNames[3] = input("Cuarto producto: ")
	itemNames[4] = input("Quinto producto: ")

	itemCount = len(itemNames)
	
	itemValues = {}
	shopInventory = {}
	sellerInventory = {}
	
	for itemName in itemNames:
		itemValue = random.randint(10, 100)
		shopQuantity = random.randint(1, 4)
		sellerQuantity = random.randint(0, 1)
		itemValues[itemName] = itemValue
		shopInventory[itemName] = shopQuantity
		sellerInventory[itemName] = sellerQuantity
		depot.append(itemNames)
	
	with open("outfile.json", "w") as fout:
		dump(depot, fout)
