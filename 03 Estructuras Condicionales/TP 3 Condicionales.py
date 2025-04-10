# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: ")) # Le solicito al usuario que ingrese un numero entero indicando su edad
if edad > 18: #Condicional, que compara la edad ingresada con el 18
    print("Es mayor de edad") #Si el numero ingresado es mayor a 18, la consola me devuelve el mensaje
    
    
# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota = int(input("Ingrese la nota de su examen: ")) # Le solicito al usuario que ingrese su nota
if nota >= 6: # Si la nota es igual o mayor a 6
    print("Usted ha Aprobado") # La consola me imprime que aprobo
else: # En caso contrario, la consola imprime que desaprobaste
    print("Desaprobaste")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese un numero par: ")) # Le solicita al usuario un numero par
while num % 2 != 0: # Mientras el resto sea distinto de 0, significa que habra un numero impar
    print("Por favor, ingrese un número par.") # Por lo tanto se le solicita al usuario que ingrese un numero par
    num = int(input("Ingrese un número par: ")) 

print("Ha ingresado un número par.") # Cuando el usuario ingresa un numero par, se imprime que lo ha ingresado


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Usted pertenece a la categoria de niños")
elif 12 <= edad < 18:
    print("Usted pertenece a la categoria de Adolescente") 
elif 18 <= edad < 30:
    print("Usted pertenece a la categoria de Adulto/a joven") 
else:
    print("Usted pertenece a la categoria de Adulto/a")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string

password = (input("Ingrese un password de entre 8 y 14 caracteres: ")) # Se le solicita al usuario una contraseña
while len(password) < 8 or len(password) > 14: # La funcion len nos devuelve la cantidad de caracteres de un string, para poder compararlo con la restriccion
    password = (input("Ha ingresado una contraseña incorrecta, vuelve a intentarlo: ")) # Mientras la contraseña ingresada sea menor a 8, o superior a 14 caracteres, 
        # se le va a solicitar al usuario que vuelva a otro password
print("Ha ingresado una contraseña correcta") # Una vez que el bucle finaliza, se le devuelve al usuario que a ingresado una contraseña correcta

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:

# Importamos las funciones que se necesitan
import random
from statistics import mode, median, mean

# Creamos una lista con 50 numeros randoms de entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

# Guardamos nuestras variables
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Lista de números:", numeros_aleatorios)
print(f"La moda es", moda) # Calculamos la moda (el número que más se repite)
print(f"La mediana es", mediana) # Calculamos la mediana (el valor del medio)
print(f"El promedio es", media) # Calculamos la media o promedio (suma / cantidad)

# Hacemos las comparaciones
if media > mediana and mediana > moda:
    print("Existe un sesgo positivo en la muestra")
elif media < mediana and mediana < moda:
    print("Existe un sesgo negativo en la muestra")
elif mediana == moda == media:
    print("No existe sesgos, y la distribucion es simetrica")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# Le pido una palabra al usuario
palabra = (input("Ingrese una palabra: "))
# Guardo en una variable la ultima letra
ultimo_caracter = palabra[-1]
# con .lower me aseguro que el ultimo caracter sea en minuscula para comprar si estan dentro de las vocales
if ultimo_caracter.lower() in "aeiou": # Si tiene una vocal
    print(f'{palabra}!') # Me va a agregar un signo de exclamacion
else: # Caso contrario solo printeara la palabra
    print(palabra)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas


#  Se le pide al usuario que ingrese su nombre
palabra = (input("Ingrese su Nombre: "))

# Se le da al usuario las opciones
print(f"1. Si quiere su nombre en mayúsculas. Por ejemplo: {palabra.upper()}.")
print(f"2. Si quiere su nombre en minúsculas. Por ejemplo: {palabra.lower()}.")
print(f"3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: {palabra.capitalize()}.")

# Se le solicita al usuario que seleccione una opcion
num = int(input("Ingrese la opcion: "))

if num == 1:
    print(palabra.upper())  # Si elige la opcion 1, muestra el nombre en mayúsculas
elif num == 2:
    print(palabra.lower())  # Si elige la opcion 2, muestra el nombre en minúsculas
elif num == 3:
    print(palabra.title())  # Si elige la opcion 1, muestra el nombre con la primera letra mayúscula
else:
    print("Opción no válida. Por favor ingrese 1, 2 o 3.")  # En caso de que no eliga una opcion valida, se le hara saber



# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

num = float(input("Ingrese la magnitud de un terremoto: "))

if num < 3:
    print("El terremoto es muy leve, casi imperceptible.")
elif 3 <= num < 4:
    print("El terremoto es leve, ligeramente perceptible.")
elif 4 <= num < 5:
    print("El terremoto es moderado. Sentido por personas, pero generalmente no causa daños.")
elif 5 <= num < 6:
    print("El terremoto es fuerte, puede causar daños en estructuras débiles.")
elif 6 <= num < 7:
    print("El terremoto es muy fuerte, puede causar daños significativos.")
else:
    print("El terremoto es extremo, puede causar graves daños a gran escala.")


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.


# Se le solicita al usuario los datos:
hemisferio = input("Ingrese si vive en el hemisferio norte o sur (N/S): ").strip().upper()
dia = int(input("Ingrese el día del mes: "))
mes = input("Ingrese el mes actual: ").strip().lower()

# Diccionario de meses para convertirlos a números
meses = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12
}

# Convertimos el mes a número
num_mes = meses.get(mes)

# Función para determinar la estación
def obtener_estacion(hemisferio, dia, mes):
    if hemisferio == "N":
        if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia < 20):
            return "Invierno"
        elif (mes == 3 and dia >= 20) or mes in [4, 5] or (mes == 6 and dia < 21):
            return "Primavera"
        elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia < 23):
            return "Verano"
        elif (mes == 9 and dia >= 23) or mes in [10, 11] or (mes == 12 and dia < 21):
            return "Otoño"
    elif hemisferio == "S":
        if (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia < 23):
            return "Invierno"
        elif (mes == 9 and dia >= 23) or mes in [10, 11] or (mes == 12 and dia < 21):
            return "Primavera"
        elif (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia < 20):
            return "Verano"
        elif (mes == 3 and dia >= 20) or mes in [4, 5] or (mes == 6 and dia < 21):
            return "Otoño"
    else:
        return "Hemisferio inválido"

# Mostrar el resultado
if num_mes:
    estacion = obtener_estacion(hemisferio, dia, num_mes)
    print(f"Estás en {estacion}")
else:
    print("Mes inválido.")
