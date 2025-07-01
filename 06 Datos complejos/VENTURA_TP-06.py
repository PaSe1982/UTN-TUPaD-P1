""" 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""
"""
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Se agregan nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Mostramos el diccionario actualizado
print(precios_frutas)

"""
#-----------------------------------------------------------------------------------------------------------------------------

""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""
"""

precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

# Actualizamos los precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostramos los precios actualizados
print(precios_frutas)

"""
#---------------------------------------------------------------------------------------------------------

""" 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios
"""
"""
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

# Creamos una lista con solo el nombre de las frutas
lista_frutas = list(precios_frutas.keys())

# Mostramos la lista nueva
print(lista_frutas)

"""
#----------------------------------------------------------------------------------------------------------------------------

""" 4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""
"""

contactos = {}

# Cargamos 5 contactos
print("Cargá 5 contactos por favor: ")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número telefónico de {nombre}: ")
    contactos[nombre] = numero

# Consultar un número por nombre
consulta = input("Nombre a buscar: ")

if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print(f"No se encontró el contacto '{consulta}'.")

"""    

#-------------------------------------------------------------------------------------------------------------

""" 5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra
"""
"""

# Pedimos al usuario que ingrese una frase
frase = input("Escribí una frase por favor: ")

# Separamos la frase en palabras
palabras = frase.split()

# Obtenemos palabras únicas con set
palabras_unicas = set(palabras)

# Contamos las apariciones
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostramos los resultados
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

"""
#-----------------------------------------------------------------------------------------------------

""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
"""
"""
# Creamos un diccionario para guardar los alumnos y sus notas
alumnos = {}
# Repetimos 3 veces para cargar los datos de cada alumno
for _ in range(3):
    nombre = input("Nombre del alumno: ")
# Pedimos 3 notas y las guardamos en una tupla
    notas = (
        int(input("Nota 1: ")),
        int(input("Nota 2: ")),
        int(input("Nota 3: "))
    )
# Guardamos las notas en el diccionario con el nombre como clave
    alumnos[nombre] = notas
# Mostramos por pantalla el promedio de cada alumno
print("\nPromedios:")
for nombre in alumnos:
    notas = alumnos[nombre]
    promedio = sum(notas) / 3
    print(nombre, "->", promedio)

    """
#--------------------------------------------------------------------------------------------------------------------------
""" 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""
"""
# Lista de estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Juan", "Lucía", "Martín", "Sofía"}
parcial2 = {"Lucía", "Pedro", "Sofía", "Marcos", "Camila"}

# 1) Los que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2
print("Aprobaron los dos parciales:", ambos)

# 2) Los que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

# 3) Todos los que aprobaron al menos un parcial (unión, sin repetir)
todos = parcial1 | parcial2
print("Aprobaron al menos un parcial:", todos)
"""
#--------------------------------------------------------------------------------------------------------------------------

""" 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""
"""
# Diccionario con productos y su stock
stock = {
    "lapicera": 10,
    "cuaderno": 5,
    "lapicera": 8
}

# Le pedimos al usuario que ingrese un producto que quiera agregar o consultar
producto = input("¿Qué producto querés consultar o agregar? ").lower()

# Si el producto ya existe
if producto in stock:
    print(f"Hay {stock[producto]} unidades de '{producto}' en stock.")
    
    # Le preguntamos si quiere agregrr más unidades
    opcion = input("¿Querés agregar unidades? (si/no): ").lower()
    if opcion == "si":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] += unidades
        print(f"Ahora hay {stock[producto]} unidades de '{producto}'.")
    else:
        print("OK, no se modificó el stock.")
else:
    # Si el producto no está, lo agregamos
    print(f"'{producto}' no está en el stock.")
    agregar = input("¿Querés agregar este nuevo producto? (sí/no): ").lower()
    if agregar == "si":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] = unidades
        print(f"Producto '{producto}' agregado con {unidades} unidades.")
    else:
        print("OK, no se agregó el producto.")

# Mostramos el stock final
print("\nStock actualizado:")
for prod, cant in stock.items():
    print(f"{prod}: {cant} unidades")

"""
#--------------------------------------------------------------------------------------------------------------------------

""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Ejemplo:
Permití consultar qué actividad hay en cierto día y hora.
"""
"""
# Agenda con actividades
agenda = {
    ("lunes", "10:00"): "Consulta médica de Silvina",
    ("martes", "15:30"): "Clases de Programación en la UTN",
    ("miercoles", "12:00"): "Gym", 
    ("viernes", "19:00"): "Editar video del TP con Nicolás"
    }

# Le pedimos al usuario el día y la hora que quiere consultar
dia = input("¿Qué día querés consultar?: ").lower()
hora = input("¿A qué hora?: ")

# Creamos la tupla con esos datos
clave = (dia, hora)

# Consultamos si esa clave existe en la agenda
if clave in agenda:
    print(f"A esa hora tenés: {agenda[clave]}")
else:
    print("No hay ninguna actividad agendada en ese horario.")

"""
#--------------------------------------------------------------------------------------------------------------------------
"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""

"""
# Diccionario original: país → capital
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

# Diccionario invertido: capital → país
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

# Mostramos el resultado
print("Dicccionario invertido:")
print(invertido)

"""