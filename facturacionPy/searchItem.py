import time
from allDesignsMenu import searchMenu
from persistence import loadData

def searchItem(loadData):	
	while True:
		searchMenu()
		
		searchOption = input("Elija una opcion: ")

		if searchOption == "1":
			time.sleep(1)
			loadData()
		
			for price, item in stock:
				print(" Cantidad: ",stock[item]," Producto: ",item," Precio unit. $: ",shop[price])
			
			print()
			input("Presione ENTER para volver al menu...")
			time.sleep(1)
		
		elif searchOption == "2":
			break
	
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			time.sleep(1)
