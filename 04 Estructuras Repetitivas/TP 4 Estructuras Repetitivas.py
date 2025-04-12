# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (0,101):
    print(i)
    
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene

# Le pedimos al usuario que ingrese el numero a analizar
num_a_analizar = int(input("Ingrese un numero entero para determinar la cantidad de digitos que contiente: "))

# Convertimos el numero en string, para usar la funcion de len y que nos devuelve la cantidad de caracteres
cantidad_digitos = len(str(abs(num_a_analizar))) # Usamos abs para evitar problemas con números negativos

print(f"El número tiene {cantidad_digitos} dígito(s).")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese un segundo numero entero: "))

inicio = min(num1, num2) + 1
fin = max(num1, num2)
suma = 0

for i in range (inicio,fin):
    suma += i
    print(suma)


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# Pido al usuario un numero entero
num1 = int(input("Ingrese un numero entero: "))
num2 = -1 # Inicializo en un num distinto de 0
contador = num1

# Estructura mientras num2 sea distinto a 0, el programa va a solicitar numeros para sumar
while num2 != 0:
   num2 = int(input("Ingrese un segundo numero entero: "))
   contador += num2 
# Una vez ingresado el 0, el programa sale del bucle y me genera por salida de consola el valor del contador
print(contador)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
# Generamos un número aleatorio entre 0 y 9
num_a_adivinar = random.randint(0, 9)

contador = 1
num1 = int(input('Adivina el número (entre 0 y 9): '))
# Mientras el num ingresado sea distinto al numero generado, el bucle se repetira hasta que el usuario lo adivine
while num1 != num_a_adivinar:
     contador += 1
     num1 = int(input('No lo adivinaste, intenta de nuevo: '))

print(f"¡Correcto! Adivinaste el número en {contador} intento(s).")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario


num2 = int(input("Ingrese un numero entero: "))
suma = 0

for i in range (0,num2+1):
    suma += i
    print(suma)


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cont = 0
positivo = 0
negativo = 0
par = 0
impar = 0

while cont < 5:
    cont += 1 
    num = int(input("Ingrese un numero: "))
    
    if num % 2 == 0:
         par += 1 
    else:
        impar += 1
    if num > 0:
        positivo += 1
    else:
       negativo += 1
        
print(f"La cantidad de numeros positivos ingresados es de: {positivo}")
print(f"La cantidad de numeros negativos ingresados es de: {negativo}")
print(f"La cantidad de numeros pares ingresados es de: {par}")
print(f"La cantidad de numeros impares ingresados es de: {impar}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cont = 0
suma = 0

while cont < 5:
    num = int(input('Ingrese un numero: '))
    suma += num
    cont += 1
print(f"El promedio es de {suma / cont}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

# Pide un número entero al usuario y muestra sus dígitos invertidos

numero = input("Ingrese un número entero: ")

# Invertimos el string con slicing [::-1]
numero_invertido = numero[::-1]

print(f"El número invertido es: {numero_invertido}")