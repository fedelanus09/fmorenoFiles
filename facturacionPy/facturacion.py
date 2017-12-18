#!/usr/bin/env python3

import time
from createMenu import *
from searchMenu import *
from sellMenu import *

while True:
	print("Menu Principal")
	print("==== =========")
	print()
	print(" 1) Ingreso de mercaderia")
	print(" 2) Lista de productos")
	print(" 3) Venta")
	print(" 4) Salir")
	print()
	
	mainOption = input("Seleccione una opcion: ")
	
	if mainOption == "1":
		time.sleep(1)
		register()
	elif mainOption == "2":
		time.sleep(1)
		search()
	elif mainOption == "3":
		time.sleep(1)
		shop()
	elif mainOption == "4":
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
