# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

frutas = list(precios_frutas.keys())
print(frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.


contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero

nombre_busqueda = input("Ingrese el nombre del contacto a buscar: ")
if nombre_busqueda in contactos:
    print("El número de teléfono de", nombre_busqueda, "es:", contactos[nombre_busqueda])
else:
    print("Contacto no encontrado.")
    
# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.


frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
conteo_palabras = {}
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1
print("Conteo de palabras:", conteo_palabras)


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.


alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {101, 102, 103, 104}
parcial_2 = {103, 104, 105, 106}
aprobados_ambos = parcial_1.intersection(parcial_2)
aprobados_uno = parcial_1.symmetric_difference(parcial_2)
aprobados_total = parcial_1.union(parcial_2)
print("Aprobados en ambos parciales:", aprobados_ambos)
print("Aprobados en solo uno de los parciales:", aprobados_uno)
print("Total de aprobados en al menos un parcial:", aprobados_total)


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos = {}
def consultar_stock(producto):
    return productos.get(producto, "Producto no encontrado.")

def agregar_stock(producto, cantidad):
    if producto in productos:
        productos[producto] += cantidad
    else:
        productos[producto] = cantidad

def agregar_producto(producto, cantidad):
    if producto not in productos:
        productos[producto] = cantidad
    else:
        print("El producto ya existe. Use 'agregar_stock' para aumentar el stock.")
        agregar_stock(producto, cantidad)
        
while True:
    accion = input("Ingrese 'consultar' para consultar stock, 'agregar' para agregar stock, 'nuevo' para agregar un nuevo producto o 'salir' para terminar: ").lower()
    if accion == 'consultar':
        producto = input("Ingrese el nombre del producto a consultar: ")
        print(consultar_stock(producto))
    elif accion == 'agregar':
        producto = input("Ingrese el nombre del producto a agregar stock: ")
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        agregar_stock(producto, cantidad)
        print(f"Stock actualizado de {producto}: {productos[producto]}")
    elif accion == 'nuevo':
        producto = input("Ingrese el nombre del nuevo producto: ")
        cantidad = int(input("Ingrese la cantidad inicial: "))
        agregar_producto(producto, cantidad)
        print(f"Producto {producto} agregado con stock inicial de {cantidad}.")
    elif accion == 'salir':
        break
    else:
        print("Acción no reconocida. Intente nuevamente.")
        
        
# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora

agenda = {("Lunes", "10:00"): "Reunión",
        ("Martes", "14:00"): "Clase de ingles",
         }

def consultar_evento(dia, hora):
    return agenda.get((dia, hora), "No hay evento programado.")
def agregar_evento(dia, hora, evento):
    agenda[(dia, hora)] = evento
while True: 
    accion = input("Ingrese 'consultar' para consultar un evento, 'agregar' para agregar un evento o 'salir' para terminar: ").lower()
    if accion == 'consultar':
        dia = input("Ingrese el día: ")
        hora = input("Ingrese la hora: ")
        print(consultar_evento(dia, hora))
    elif accion == 'agregar':
        dia = input("Ingrese el día del evento: ")
        hora = input("Ingrese la hora del evento: ")
        evento = input("Ingrese el nombre del evento: ")
        agregar_evento(dia, hora, evento)
        print(f"Evento '{evento}' agregado para {dia} a las {hora}.")
    elif accion == 'salir':
        break
    else:
        print("Acción no reconocida. Intente nuevamente.")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.


original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {capital: pais for pais, capital in original.items()}
print("Diccionario original:", original)
print("Diccionario invertido:", invertido)

