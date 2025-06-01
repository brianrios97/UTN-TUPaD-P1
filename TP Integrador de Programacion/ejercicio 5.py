def analizar_numero(x):
    if x < 0:
        resultado = "Negativo"         # 1 comparación + 1 asignación # T(B1)
    elif x == 0:
        resultado = "Cero"             # 2 comparaciones (incluye x < 0) + 1 asignación # T(B2)
    else:
        resultado = "Positivo"         # 2 comparaciones (x < 0 y x == 0) + 1 asignación # T(B3)
    return resultado                   # 1 operación (retorno) # T(B4)
# Análisis de la complejidad temporal
# T(n) = T(B1) + T(B2) + T(B3) + T(B4)
# T(n) = max(T(B1), T(B2), T(B3)) + T(B4)
# T(n) = O(1) + O(1) + O(1) + O(1)
# T(n) = O(1)
# Complejidad temporal: O(1) (constante)
# Complejidad espacial: O(1) (constante, solo se usa una variable para el resultado)

