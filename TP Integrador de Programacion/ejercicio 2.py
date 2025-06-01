import timeit
import matplotlib.pyplot as plt

# Función O(n) - Suma iterativa
def suma_elementos(n):
    suma = 0   # -> O(1)
    for i in range(n): # -> O(n)
        suma += i # -> O(1) por iteración
    return suma # -> O(1)
# Total: O(n) (lineal)
# Complejidad temporal suma_elementos:
# - suma = 0   -> O(1)
# - for i in range(n): -> O(n)
#     suma += i        -> O(1) por iteración
# - return suma       -> O(1)
## T(n) = O(1) + O(n) + O(1) + O(1)
# Total: O(n) (lineal)
# Complejidad espacial suma_elementos:
# - suma, i: variables escalares -> O(1)
# Total: O(1) (constante)

# Función O(2^n) - Fibonacci recursivo (ineficiente)
def fibonacci(n): # -> O(2^n)
    # Casos base
    if n <= 1: # -> O(1)
        # Si n es 0 o 1, retorna n directamente
        return n #  -> O(1)
    # Llamadas recursivas
    else: # -> O(2^n)
        # Retorna la suma de las dos llamadas recursivas
        # fibonacci(n-1) y fibonacci(n-2)
        return fibonacci(n-1) + fibonacci(n-2)# -> O(1)
# Total: O(2^n) (exponencial)
# Complejidad temporal fibonacci:
# - Cada llamada genera 2 llamadas recursivas (excepto casos base)
# - T(n) = T(n-1) + T(n-2) + O(1)
# - Número de llamadas crece exponencialmente: O(2^n)
# Complejidad espacial fibonacci:
# - Profundidad máxima de la pila de recursión: O(n)
# Total: O(n) (lineal)

# Medición de tiempos
valores_n = range(1, 30)
tiempos_suma = []
tiempos_fibonacci = []

for n in valores_n:
    # Medir suma (O(n))
    tiempo_suma = timeit.timeit(lambda: suma_elementos(n), number=1000)
    tiempos_suma.append(tiempo_suma)
    
    # Medir Fibonacci (O(2^n))
    if n <= 25:  # Evitar tiempos muy largos
        tiempo_fib = timeit.timeit(lambda: fibonacci(n), number=1)
        tiempos_fibonacci.append(tiempo_fib)

# Gráficos
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(valores_n, tiempos_suma, marker='o', color='green')
plt.xlabel('n')
plt.ylabel('Tiempo (segundos)')
plt.title('Suma Iterativa (O(n))')

plt.subplot(1, 2, 2)
plt.plot(valores_n[:len(tiempos_fibonacci)], tiempos_fibonacci, marker='o', color='red')
plt.xlabel('n')
plt.ylabel('Tiempo (segundos)')
plt.title('Fibonacci Recursivo (O(2^n))')

plt.tight_layout()
plt.show()





