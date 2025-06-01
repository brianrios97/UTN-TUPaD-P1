n = 2                  # T(B1) = O(1) → Asignación simple
suma = 0               # T(B2) = O(1) → Asignación simple
for i in range(1, n+1):   # T(B3) = O(n) → Bucle con n iteraciones
    suma = suma + i       # T(B4) = O(2) por iteración (suma + asignación)
print(suma)            # T(B5) = O(1) → Operación de impresión
# Análisis de la complejidad temporal
# T(n) = T(B1) + T(B2) + T(B3) + T(B4) + T(B5)
# T(n) = O(1) + O(1) + O[(n) * (2)] + O(1)
# T(n) = O(n) (lineal)
# Total: 1 + 1 + n * 2 + 1 = 2n + 3 operaciones
# Función O(n) - Suma de los primeros n números enteros
# Complejidad espacial:
# S(n) = O(1) (constante)
# Complejidad espacial: O(1) (constante)

