# Análisis de operaciones primitivas por línea

x = 2                 # 1 operación: asignación

x = y + 3             # 2 operaciones:
                     #   - 1 suma (y + 3)
                     #   - 1 asignación (x =)

return a[0] + 1       # 3 operaciones:
                     #   - 1 acceso a lista (a[0])
                     #   - 1 suma (+1)
                     #   - 1 retorno (return)

return node is None or node.elem > 5
                     # 5 operaciones:
                     #   - 1 comparación (node is None)
                     #   - 1 acceso a atributo (node.elem)
                     #   - 1 comparación (node.elem > 5)
                     #   - 1 operador lógico (or)
                     #   - 1 retorno (return)

print("Hola")         # 1 operación: impresión



