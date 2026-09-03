import random
import matplotlib.pyplot as plt
import time 

# Función para generar una lista aleatoria de tamaño n
def generar_lista_aleatoria(n, minimo=0, maximo=1000):
    return [random.randint(minimo, maximo) for _ in range(n)]

def bubble_sort(arr, n):
    tiempo_inicial = time.time()
    pasos = 0 
    intercambios = 0
    for i in range(n):
        pasos += 1
        for j in range(0, n - i - 1):
            pasos += 1
            if arr[j] > arr[j+1]:
                intercambios += 2
                arr[j], arr[j+1] = arr[j+1], arr[j]

    tiempo_final = time.time() - tiempo_inicial
    return pasos, tiempo_final, intercambios

def insertion_sort(arr):
    tiempo_inicial = time.time()
    pasos = 0
    intercambios = 0

    for i in range(1, len(arr)):
        pasos += 1 
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            pasos += 1 
            intercambios += 1 
            arr[j + 1] = arr[j]
            j -= 1
            
        intercambios += 1 
        arr[j + 1] = key
    tiempo_final = time.time() - tiempo_inicial
    return pasos, tiempo_final, intercambios

def comparacion(num_Pruebas, num_Entrada, paso_Parametro):
    # Resultados de la prueba
    pasos_B, tiempos_B, intercambios_B = [], [], []
    pasos_I, tiempos_I, intercambios_I = [], [], []
    
    # Iterador, que genera los tamaños de entrada para las pruebas en base al paso de incremento
    tamanos_n = [paso_Parametro * i for i in range(1, num_Entrada + 1)]

    for n in tamanos_n:
        # Resultados para el promedio 
        p_b_sub, t_b_sub, i_b_sub = 0, 0, 0
        p_i_sub, t_i_sub, i_i_sub = 0, 0, 0

        for _ in range(num_Pruebas):
            # Probar Bubble Sort
            arr_b = generar_lista_aleatoria(n, 1, 100)
            pasos, tiempo, intercambios = bubble_sort(arr_b, n)
            p_b_sub += pasos
            t_b_sub += tiempo
            i_b_sub += intercambios

            # Probar Insertion Sort 
            arr_i = generar_lista_aleatoria(n, 1, 100)
            pasos, tiempo, intercambios = insertion_sort(arr_i)
            p_i_sub += pasos
            t_i_sub += tiempo
            i_i_sub += intercambios

        # Se guardan los promedios en los arreglos globales 
        pasos_B.append(p_b_sub / num_Pruebas)
        tiempos_B.append(t_b_sub / num_Pruebas)
        intercambios_B.append(i_b_sub / num_Pruebas)

        pasos_I.append(p_i_sub / num_Pruebas)
        tiempos_I.append(t_i_sub / num_Pruebas)
        intercambios_I.append(i_i_sub / num_Pruebas)

    # Devuelve los resultados de la comparación
    return tamanos_n, (pasos_B, tiempos_B, intercambios_B), (pasos_I, tiempos_I, intercambios_I)

# Función para graficar los resultados de la comparación
def graficar_resultados(n_valores, bubble_datos, insertion_datos):
    # Graficar los resultados de la interacciones 
    plt.figure(figsize=(8, 6))
    plt.plot(n_valores, bubble_datos[0], marker='o' ,label='Bubble Sort')
    plt.plot(n_valores, insertion_datos[0], marker='s', label='Insertion Sort')
        
    plt.title('Interacciones de Bubble Sort vs Insertion Sort')
    plt.xlabel('Tamaño de la entrada')
    plt.ylabel('Interacciones')
    plt.legend()
    
    # Graficar los resultados de los tiempos
    plt.figure(figsize=(8, 6))
    plt.plot(n_valores, bubble_datos[1], marker='o' ,label='Bubble Sort')
    plt.plot(n_valores, insertion_datos[1], marker='s', label='Insertion Sort')
        
    plt.title('Tiempo de Bubble Sort vs Insertion Sort')
    plt.xlabel('Tamaño de la entrada')
    plt.ylabel('Tiempo')
    plt.legend()
    

    # Graficar los resultados de los intercambios
    plt.figure(figsize=(8, 6))
    plt.plot(n_valores, bubble_datos[2], marker='o' ,label='Bubble Sort')
    plt.plot(n_valores, insertion_datos[2], marker='s', label='Insertion Sort')
        
    plt.title('Intercambios de Bubble Sort vs Insertion Sort')
    plt.xlabel('Tamaño de la entrada')
    plt.ylabel('Intercambios')
    plt.legend()
    plt.show() 

num_Pruebas    = int(input("Ingresa el numero de pruebas: "))
num_Entrada    = int(input("Ingresa el numero de entradas: "))
paso_Parametro = int(input("Ingresa el paso de incremento: "))

arreglo_x, datos_bubble, datos_insertion = comparacion(num_Pruebas, num_Entrada, paso_Parametro)
graficar_resultados(arreglo_x, datos_bubble, datos_insertion)