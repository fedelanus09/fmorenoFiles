import time
import random
from os import system
from searchMenu import *

def shop():
	system("clear")
	
	print(" Menu de Ventas ")
	print(" ==== == ====== ")
	print()
	print(" 1) Realizar venta")
	print(" 2) Volver al menu anterior")
	print()

	while True:
		sellOption = input("Seleccione una opcion: ")
	
		if sellOption == "1":
			time.sleep(1)
			runShop()
			print()
			input("Presione ENTER para volver al menu...")
			time.sleep(1)
		elif sellOption == "2":
			break
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			time.sleep(1)

def runShop():
	system("clear")
	
	loadData()
	
	shopCurrency = random.randint(150, 600)
	sellerCurrency = random.randint(100, 350)

	displayInventory(message, inventory, values, count=0)
	
	itemValueKeys = sorted(itemValueKeys.keys())
	answer = raw_input("Que producto te gustaria comprar? ")
	
	if answer.isdigit() and int(answer) < itemCount:
		answer = int(answer)
		itemName = itemValueKeys[answer]
		itemValue = itemValues[itemName]
		if shopInventory[itemName] <= 0:
			print("{} no esta disponible. ".formar(itemName))
		else:
			shopCurrency = shopCurrency + itemValue
			sellerCurrency = sellerCurrency - itemValue
			shopInventory[itemName] = shopInventory[itemName] - 1
			sellerInventory[itemName] = sellerInventory[itemName] + 1

	elif answer.isdigit() and int(answer) >= itemCount:
		answer = int(answer)
		itemName = itemValueKeys[answer - itemCount]
		itemValue = itemValues[itemName]
		if sellerInventory[itemName] <= 0:
			print("{} no esta disponible.".format(itemName))
		else:
			playerCurrency = playerCurrency + itemValue
			shopCurrency = shopCurrency - itemValue
			playerInventory[itemName] = playerInventory[itemName] - 1
			shopInventory[itemName] = shopInventory[itemName] + 1

	else:
		if answer.lower().startswith(("n", "s")):
			continueShopping = False
		elif answer.lower():
			continueShopping = True
		else:
			print("Could not find {}".format(answer))
			continueShopping = True
