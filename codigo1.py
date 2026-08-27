"""
import tkinter as tk
from tkinter import END, messagebox, ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(width=200, height=200)
        self.title("Practica")
        self.lblNombre = tk.Label(self, text="Ingrese su nombre")
        self.lblNombre.place(x = 20, y = 20)
        self.entry_nombre = tk.Entry(self, width = 20)
        self.entry_nombre.place(x = 20, y = 40)
        self.button = tk.Button(self, text="Mostrar", command=lambda:self.Mostrar(self.entry_nombre.get()))
        self.button.place(x = 50, y = 40)
    def Mostrar(self, nombre):
        messagebox.showinfo(title="Mensaje", message="Hola " + nombre)

if __name__ == "__main__":
    app = App()
    app.mainloop()

import random

def generar_lista_aleatoria(n, minimo=0, maximo=100):
    return [random.randint(minimo, maximo) for _ in range(n)]

print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())

aleatorios=generar_lista_aleatoria(n)
print(aleatorios)
"""
""""
entrada = input ()
x = "Bienvenido al "
if entrada == "CUCEI": 
    print (x + entrada)

print ("\n")
print ("--------------------------------------------------------------------------------")

"""
"""
n= [1,2,3,4,5,6,7]
print ("Primer for","\n")
for i in n:
    print (i)

print ("----------------------------------------------------------------------------")

print ("\n")
print ("Segundo for", "\n")

for n in range (n ,0):
    print (n)

print ("------------------------------------------------------------------------------------------")

"""
'''
import time 

def bubble_sort (arr):
    #Complejidad 
    n = len (arr)

    for i in range (n):

        for j in range (0,n-i-1):

            #comparacion O(1)
            if arr [j] > arr [j+1]:
                #intercambio O(1)
                arr[j], arr[j+1] = arr[j+1], arr[j]

def generador ():
    arr = []
    suma = 0
    for i in range (5):
        suma += i 
        print (i)
    return arr

array  = [6,5,3,1,8,7,2,4] # O(1)

bubble_sort (array) # O (n*2)

print ("\n") # O(1)
print ("Lista ordenada:", array, "\n") #O(n)
print ("-----------------------------------------------------------------------------------------------------")
generador ()

 suma (T x Frec . Op . Elemental)
import random
import numpy as np
import matplotlib.pyplot as plt

def generar_lista_aleatoria(n, minimo=0, maximo=100):
    return [random.randint(minimo, maximo) for _ in range(n)]


def bubble_sort (arr, n):
    #Complejidad 
    k = 0
    for i in range (n):
        k += 1
        for j in range (0,n-i-1):
            k += 1
            #comparacion O(1)
            if arr [j] > arr [j+1]:
                #intercambio O(1)
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return k

# Crear un arreglo de datos con NumPy

resultados = []
entrada = [10, 20, 30, 40, 50]
arreglo = generar_lista_aleatoria(10, 1, 100)
for i in entrada: 
    arrC = arreglo  
    res = bubble_sort(arrC, i)
    resultados.append(res)



arreglo_x = np.array(entrada)
arreglo_y = np.array(resultados)

# Graficar los arreglos
plt.plot(arreglo_x, arreglo_y, marker='o')

# Añadir títulos y etiquetas
plt.title('Gráfica de un arreglo')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar la gráfica
plt.show()
'''

import random
import numpy as np
import matplotlib.pyplot as plt

def generar_lista_aleatoria(n, minimo=0, maximo=100):
    return [random.randint(minimo, maximo) for _ in range(n)]

def bubble_sort(arr, n):
    k = 0 
    for i in range(n):
        k += 1
        for j in range(0, n - i - 1):
            k += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return k

entrada = [1, 50, 100, 150, 200, 250, 300, 350, 400, 500,550]
resultados = []

for n in entrada: 
    arreglo_nuevo = generar_lista_aleatoria(n, 1, 100)
    
    res = bubble_sort(arreglo_nuevo, n)
    resultados.append(res)

arreglo_x = np.array(entrada)
arreglo_y = np.array(resultados)

plt.figure(figsize=(8, 5))
plt.plot(arreglo_x, arreglo_y,marker='o')

plt.legend()
plt.show()
