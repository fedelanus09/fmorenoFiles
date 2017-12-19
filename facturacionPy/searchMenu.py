import time
from os import system
from persistence import loadData

def searchMenu():
	system('clear')
	
	print("Lista de mercaderia")
	print("===== == ==========")
	print()
	print(" 1) Mostrar todos los productos")
	print(" 2) Volver al menu anterior")
	print()

def search():
	while True:
		searchMenu()

		searchOption = input("Elija una opcion: ")
		
		if searchOption == "1":
			time.sleep(1)
			showAll()
			print()
			input("Presione ENTER para volver al menu...")
			time.sleep(1)
		elif searchOption == "2":
			break
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			time.sleep(1)

def showAll():
	system('clear')
	
	print(" Lista de Productos")
	print(" ===== == =========")
	print()
	print(" Cantidad | Producto  | Precio unit. |")
	
	loadData()
