#!/usr/bin/env python3

import time
from allDesignsMenu import mainMenu
from createItem import *
from shop import *
from persistence import saveData

while True:
	mainMenu()
	
	mainOption = int(input("Seleccione una opcion: "))
	
	if mainOption == 1:
		time.sleep(1)
		createItem()
		
	elif mainOption == 2:
		time.sleep(1)
		searchItem()
		
	elif mainOption == 3:
		time.sleep(1)
		shop()
		
	elif mainOption == 4:
		time.sleep(1)
		print()
		print("Gracias!")
		print()
		time.sleep(1)
		break
	
	else:
		print()
		print("ERROR! OPCION INCORRECTA")
		time.sleep(1)

saveData(inventory)
