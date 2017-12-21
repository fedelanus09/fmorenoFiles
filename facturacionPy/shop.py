import time
from os import system
from allDesignsMenu import shopMenu
from searchItem import *

def shop():
	while True:
		shopMenu()
		
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
