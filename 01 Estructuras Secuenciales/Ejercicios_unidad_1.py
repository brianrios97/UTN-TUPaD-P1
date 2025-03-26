# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola mundo")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Ingrese un nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
edad = input("Que edad tienes?: ")
residencia = input("Cual es el lugar en donde vives?: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
import math

radio = float(input("Ingrese el numero de radio del circulo que quieres calcular: "))
area = (radio ** 2) * math.pi
perimetro = 2 * math.pi * radio
print(f"El area del circulo es {area:.2f} y su perimetro {perimetro:.2f}")


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = float(input("Ingrese los segundos, para calcular a cuantas horas equivale: "))
minutos = segundos / 60
horas = minutos / 60
print(f"La hora es: {horas}")


# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

tabla = int(input("Ingrese un numero para calcular su tabla de multiplicar hasta 10: "))
for i in range(1,11):
    print(f"{tabla} * {i} = {tabla * i}")
    
# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos

num1 = int(input("Ingrese un numero Entero: "))
num2 = int(input("Ingrese un segundo numero Entero: "))
print(f"{num1 + num2}")
print(f"{num1 - num2}")
print(f"{num1 * num2}")
print(f"{num1 / num2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su pesos en kg: "))

imc = peso / (altura ** 2)
print(f"su Indice de masa corporal es: {imc:.2f}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9 / 5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

celcius = float(input("Ingrese una temperatura en grados celcius: "))
farenheit = (9/5 * celcius) + 32

print(f"La temperatura en farenheit es: {farenheit:.2f}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

suma = 0  

for i in range(3):
    numero = float(input(f"Ingrese el número {i + 1}: "))  
    suma += numero  
promedio = suma / 3
print(f"El promedio de los tres números es: {promedio:.2f}")