#!/usr/bin/env python3

import time
from os import system
from shopMenus import *

system("clear")

print("Bienvenido a FIS Shop")
print("="*40)
print()
print(" 1) Ingreso de mercaderia")
print(" 2) Lista de productos")
print(" 3) Venta")
print(" 4) Salir")
print("="*40)
print()

while True:
	mainOption = input("Seleccione una opcion: ")

	if mainOption == "1":
		time.sleep(1)
		create()
	elif mainOption == "2":
		time.sleep(1)
		search()
	elif mainOption == "3":
		time.sleep(1)
		sell()
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