import time
from os import system
from allDesignsMenu import createMenu
from persistence import saveData

inventory = []
stock = {}

def createItem():	
	while True:
		createMenu()
		
		registerOption = int(input("Seleccione una opcion: "))

		if registerOption == 1:
			time.sleep(1)
			print()
			system("clear")
		
			item = input(" Nombre de producto: ")
		
			if item in stock:
				print(" El producto ya existe.")
				quantity = int(input(" Agregar cantidad: "))
				stock[item] = stock[item] + quantity
				
			else:
				quantity = int(input(" Cantidad: "))
				stock[item] = quantity
				price = int(input(" Precio unit. $: "))
				stock[item][price] = price
				
			inventory.append(stock)
		
			print()
			input("Presione ENTER para volver al menu...")
			time.sleep(1)
		
		elif registerOption == 2:
			break
	
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			time.sleep(1)
