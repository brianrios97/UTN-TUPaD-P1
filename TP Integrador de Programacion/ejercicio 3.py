import time

def sumN(n):	 
	start = time.time() 	# O(1)	
	# Suma de los primeros n números enteros
	res = 0  	# O(1)
	for i in range(1, n + 1): # O(n)
		res += i 	# O(n)
	# Fin de la suma	
	end = time.time() 	# O(1)
	return res, (end - start) * 1000	
print("n\t sumN(ms)") # O(1)		
for i in range(1,9): # O(1)
	# Llamada a la función sumN con 10^i
	_,tiempo_total=sumN(10**i)	# O(1)
	print(f"{10**i}\t {tiempo_total} ")	# O(1)	
	
 
# Análisis de la complejidad temporal
# T(n) = T(B1) + T(B2) + T(B3)
# T(n) = O(1) + O(1) + O(n)
# T(n) = O(n)
# Complejidad temporal: O(n) (lineal)
# Análisis de la complejidad espacial
# S(n) = O(1) (constante, solo se usa una variable para el resultado)
# Complejidad espacial: O(1) (constante, solo se usa una variable para el resultado)