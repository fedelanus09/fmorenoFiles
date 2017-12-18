import time
from os import system
from persistence import saveData

def register():
	system("clear")
	
	print(" Registro de mercaderia ")
	print(" ======== == ========== ")
	print()
	print(" 1) Ingresar nuevo producto")
	print(" 2) Volver al menu anterior")
	print()

	while True:
		registerOption = input("Seleccione una opcion: ")
	
		if registerOption == "1":
			time.sleep(1)
			system("clear")
			addProduct()
			print()
			input("Presione ENTER para volver al menu...")
			time.sleep(1)
			register()
		elif registerOption == "2":
			break
		else:
			print()
			print("ERROR! OPCION INCORRECTA")
			time.sleep(1)

def addProduct():	
	print(" INGRESO DE NUEVO PRODUCTO ")
	print(" ======= == ===== ======== ")
	print()
	
	saveData()
