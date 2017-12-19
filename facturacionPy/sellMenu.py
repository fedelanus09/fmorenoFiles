import time
from os import system
from searchMenu import *

def sellMenu():
	system('clear')
	
	print("Menu de Ventas")
	print("==== == ======")
	print()
	print(" 1) Realizar venta")
	print(" 2) Volver al menu anterior")
	print()

def sell():
	while True:
		sellMenu()
		
		sellOption = int(input("Seleccione una opcion: "))
		
		if sellOption == "1":
			time.sleep(1)
			sale()
			print()
			input("Presione ENTER para volver al menu...")
			time.sleep(1)
		elif sellOption == "2":
			break
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			time.sleep(1)

def sale():
	system('clear')
	
	showAll()
	
	while True:
		saleOption = input("Nombre de producto: ")
		
		if saleOption == "Remera":
			tShirtSale()
		elif saleOption == "Jean":
			jeanSale()
		elif saleOption == "Musculosa":
			topSale()
		elif saleOption == "Short":
			shortSale()
		elif saleOption == "Camisa":
			shirtSale()
		else:
			print()
			print("ERROR! NOMBRE DE PRODUCTO INCORRECTO")
			time.sleep(1)

def tShirtSale():
	while True:
		tShirtOption = int(input("Cantidad: "))
		
		
