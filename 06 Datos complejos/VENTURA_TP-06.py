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

#--------------------------------------------------------------------------------------------------------------------------