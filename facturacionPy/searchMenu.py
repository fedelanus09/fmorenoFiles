import time
from os import system
from persistence import loadData

def search():
	system("clear")
	
	print("Lista de mercaderia")
	print("===== == ==========")
	print()
	print(" 1) Mostrar todos los productos")
	print(" 2) Volver al menu anterior")
	print()

	while True:
		searchOption = input("Elija una opcion: ")
	
		if searchOption == "1":
			time.sleep(1)
			displayInventory()
			print()
			input("Presione ENTER para volver al menu...")
			time.sleep(1)
		elif searchOption == "2":
			break
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			time.sleep(1)

def displayInventory():
	system("clear")
	
	loadData()
