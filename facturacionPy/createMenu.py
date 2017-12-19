#!/usr/bin/env python3

import time
from os import system
from json import loads
from json import dump

stock = {}

system("cls")
	
print(" Registro de mercaderia")
print("="*40)
print()
print(" 1) INGRESAR PRODUCTO")
print(" 2) VOLVER AL MENU ANTERIOR")
print()
print("="*40)

while True:
    menuOption = int(input(" Seleccione una opcion: "))

    if menuOption == 1:
        system("cls")
        item = input(" Nombre de producto: ")

        if item in stock:
            print(" Este producto ya existe.")
            quantity = int(input(" Agregar cantidad: "))
            stock[item] = stock[item] + quantity
        else:
            quantity = int(input(" Cantidad: "))
            stock[item] = quantity
            price = int(input(" Precio unit. $: "))
            stock[price] = price

        with open("database.json", "w") as fout:
            dump(stock, fout)

    elif menuOption == 2:
        quit()
    else:
        print(" ERROR! OPCION INCORRECTA.")

stock = loads(open("database.json").read())

print(" LISTA DE PRODUCTOS ")
print("="*40)

for i in stock:
    print(" Cantidad: " + stock[item] + " Producto: " + item + " Precio unit. $: "\
          + stock[price])