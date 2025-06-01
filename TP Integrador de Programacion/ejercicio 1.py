import timeit
import random
import matplotlib.pyplot as plt

# Búsqueda Lineal (O(n))
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)): # O(n)
        if lista[i] == objetivo: # O(1) por iteración
            return i #  O(1)
    # Si no se encuentra el objetivo, retornar -1
    return -1 # -1 (O(1))
#   # Análisis de la complejidad temporal y espacial de la búsqueda lineal:
#   # Complejidad temporal:
#   # - Bucle for recorre n elementos: O(n)
#   # - Comparación y retorno son O(1) por iteración.
#   # Total: O(n) (lineal)
#   # Complejidad espacial:
#   # - Solo se usan variables escalares (i, objetivo): O(1)
#   # No se usan estructuras de datos adicionales.
#   # Total: O(1) (constante)


# Búsqueda Binaria (O(log n))
def busqueda_binaria(lista, objetivo):
    izquierda = 0   # O(1)
    derecha = len(lista) - 1        # O(1)
    while izquierda <= derecha:     # O(log n)
        medio = (izquierda + derecha) // 2      # O(1)
        if lista[medio] == objetivo:        # O(1)
            return medio    
        elif lista[medio] < objetivo:       # O(1)
            izquierda = medio + 1   
        else:   # O(1)
            derecha = medio - 1 # O(1)
    return -1# # O(1)
#   # Análisis de la complejidad temporal y espacial de la búsqueda binaria:    
#   # Complejidad temporal:
#   # - Bucle while reduce el rango de búsqueda a la mitad en cada iteración: O(log n)
#   # - Comparaciones y asignaciones son O(1) por iteración.
#   # Total: O(log n) (logarítmica)
#   # Complejidad espacial:
#   # - Solo se usan variables escalares (izquierda, derecha, medio): O(1)
#   # No se usan estructuras de datos adicionales.
#   # Total: O(1) (constante)


# Generar lista ordenada y objetivo
tamanos = [1000, 10000, 100000]
resultados_lineal = []
resultados_binaria = []

for tamano in tamanos:
    lista = sorted(random.sample(range(tamano * 10), tamano))
    objetivo = random.choice(lista)
    
    # Medir tiempo de búsqueda lineal
    tiempo_lineal = timeit.timeit(lambda: busqueda_lineal(lista, objetivo), number=1000)
    resultados_lineal.append(tiempo_lineal)
    
    # Medir tiempo de búsqueda binaria
    tiempo_binaria = timeit.timeit(lambda: busqueda_binaria(lista, objetivo), number=1000)
    resultados_binaria.append(tiempo_binaria)

# Gráfico
plt.plot(tamanos, resultados_lineal, marker='o', label='Búsqueda Lineal (O(n))')
plt.plot(tamanos, resultados_binaria, marker='o', label='Búsqueda Binaria (O(log n))')
plt.xlabel('Tamaño de la Lista')
plt.ylabel('Tiempo (segundos)')
plt.legend()
plt.title('Análisis Empírico: Búsqueda Lineal vs. Binaria')
plt.show()

print("Resultados de búsqueda lineal:", resultados_lineal)
print("Resultados de búsqueda binaria:", resultados_binaria)

