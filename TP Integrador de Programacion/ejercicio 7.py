# Bucles anidados
for i in range(n):             # Bucle externo → n iteraciones → O(n)
    for j in range(n):         # Bucle interno → n iteraciones por cada i → O(n)
        print(i * j)           # 2 operaciones por iteración: multiplicación + impresión → O(1)
# COMPLEJIDAD TEMPORAL:
# - El cuerpo interno se ejecuta n × n veces → n² veces
# - En cada iteración se realizan 2 operaciones constantes → O(1)
# T(n) = n × n × 2 = 2n² → O(n²)
# COMPLEJIDAD ESPACIAL:
# - Solo se usan variables escalares (i, j) → no se usan estructuras de datos
# S(n) = O(1) (constante)

