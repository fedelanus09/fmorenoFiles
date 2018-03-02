#!/usr/bin/env python3

import tkinter as tk
from tkinter import simpledialog as sd

def loadData(dictionary, columnas):
	for nombreColumna in columnas: 
		dictionary[nombreColumna] = sd.askstring("Datos Personales", "Ingrese " + nombreColumna)

def showData(dictionary):
	yValue = 90
	
	for clave, valor in dictionary.items():
		label = tk.Label(mainForm, text = clave + ": " + str(valor))
		label.place(x = 10, y = yValue)
		
		yValue += 20

dictionary = {}
columnas = ("Nombre", "Apellido", "DNI", "Edad", "Fecha Nacimiento", "Telefono", "Direccion", "Correo Electronico")

mainForm = tk.Tk()
mainForm.title("Ejercicio 2")
mainForm.geometry("400x300")

mainMenu = tk.Menu(mainForm)

fileMenu = tk.Menu(mainMenu, tearoff = 0)
fileMenu.add_command(label = "Salir", command = quit)

mainMenu.add_cascade(label = "Archivo", menu = fileMenu)

editMenu = tk.Menu(mainMenu, tearoff = 0)
editMenu.add_command(label = "Cargar datos", command = lambda: loadData(dictionary, columnas))
editMenu.add_command(label = "Mostrar datos", command = lambda: showData(dictionary))

mainMenu.add_cascade(label = "Personas", menu = editMenu)

mainForm.config(menu = mainMenu)

mainForm.mainloop()
