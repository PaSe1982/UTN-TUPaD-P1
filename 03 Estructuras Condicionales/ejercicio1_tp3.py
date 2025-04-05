""" TRABAJO PRACTICO N° 3  """



""" 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

## Declaramos una variable entera, llamada "edad", y le pedimos al usuario que ingrese la misma

#edad = int(input("Por favor, ingrese su edad "))

## Abrimos la condicional if, si edad > que 18, se mostrara por pantalla: Es mayor de edad, y por ultimo la palabra adios

#if edad > 18:
#    print("Es mayor de edad")

## En caso de que sea menor que 18 años, pasara por alto y solo mostrará por pantalla la palabra adios.

#else:
#    pass
#print("Adios")




""" 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar
por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”."""

# nota = float(input("Por favor, ingrese su nota "))
# if nota >= 6:
#    print("aprobado")
# else:
#    print("desaprobado")



""" 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir 
por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese
un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar."""

# num = int(input("Por favor ingrese un numero par: "))
# if num % 2 == 0:
#    print("Ha ingresado un numero par")
# else:
#    print("Por favor ingrese un numero par")


""" 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías 
pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años."""

# edad = int(input("Ingrese su edad:  "))

# if edad <= 0: 
#    print("Por favor ingrese un valor valido > a 0")

# elif edad < 12:
#    print("Es un niño/a: menor de 12 años")
# elif edad >= 12 and edad < 18:
#    print("Es un Adolecente: mayor o igual que 12 y menor que 18 años")
# elif edad >=18 and edad < 30:
#    print("Es un adulto/a joven: mayor o igual que 18 y menor que 30 años")
# else:
#    print("Es un adulto/a: mayor o igual que 30 años")
# print("vuelva a correr el programa, adios!")


""" 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado 
una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña
de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos
que tiene un iterable tal como una lista o un string. """

#contraseña = str(input("Por favor ingrese una contraseña de entre 8 y 14 caracteres: "))
#if 8 <= len(contraseña) <= 14:
#    print("Usted ha ingresado una contraseña correcta")
#else:
#    print("ERROR: la contraseña debe tener entre 8 y 14 caracteres, vuelva a intentar")

"""6) escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare 
para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
DATOS:
    La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir 
    la forma de una distribución normal a partir del siguiente criterio: 
    ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
    ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda.
    ● Sin sesgo: cuando la media, la mediana y la moda son iguales. """

## Agregamos las librerias
# from statistics import mode, median, mean
# from random import randint

# # Se crea una lista de 50 numeros aleatorios entre el 1 y el 100
# numeros_aleatorios = [randint(1, 100) for i in range(50)]

# media = mean(numeros_aleatorios) # Es el promedio de los 50 numeros
# moda = mode(numeros_aleatorios)  # Es el valor que mas se repite
# mediana = median(numeros_aleatorios) # Es la suma del menor numero y el mayor numero (de los 50), dividido dos
# print(numeros_aleatorios)
# print(f"media: {media} moda: {moda} mediana: {mediana}")



# Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# Sin sesgo: cuando la media, la mediana y la moda son iguales.


# if media > mediana and mediana > moda:
#     print("El sesgo es positivo")
# elif media < mediana and mediana < moda:
#     print("El sesgo es negativo")
# elif media == mediana == moda:
#     print("Sin sesgo")
# else:
#     print("Sesgo atípico")


"""7) Escribir un programa que solicite una frase 
o palabra al usuario. Si el string ingresado termina con vocal,
añadir un signo de exclamación al final e imprimir el string resultante por pantalla;
en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla."""

# # defino la variable que almacena la frase o la palabra

# frase = str(input("Igrese frase o palabra: "))

# # esta variable se queda con la ultima letra

# ultima_letra = str.lower(frase[-1])

# # acá comparamos la ultima letra con las vocales, en caso de ser vocal, se le agrega un signo de exclamacion
# # a la frase o palabra, y se imprime por pantalla.

# if ultima_letra in "aeiou":
#     print(f"{frase}!")
# else:
#     print(frase)

"""8) Escribir un programa que solicite al usuario que ingrese su nombre 
y el número 1, 2 o 3 dependiendo de la opción que desee:

1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario 
e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y 
title() de Python para convertir entre mayúsculas y minúsculas."""

# # Le pedimos al usuario que ingrese su nombre

# nombre = str(input("Ingrese su nombre: "))

# # Ahora le pedimos que ingrese una de las tres opciones para que vea su nombre como aparece en
# # dichas opciones

# opcion = int(input("Ingrese la opcion en la que desea ver escrito su nomnbre: 1)MAYUSCULA, 2)minuscula o 3)Titulo: "))

# # Realizamos un IF para ver que opcion elige y según la ocion, se imprime el nombre en pantalla, en caso de que
# # elija una opcion incorrecta, se imprime un aviso de error y una frase de que lo vuelva a intentar
# if opcion == 1:
#     MAYUSCULA = nombre.upper()
#     print({MAYUSCULA})
# elif opcion == 2:
#     minuscula = nombre.lower()
#     print({minuscula})
# elif opcion == 3:
#     primera_mayusc = nombre.title()
#     print({primera_mayusc})
# else:
#     print(f"Eligió una opcion incorrecta, vuelva a intentarlo")



""" 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una 
de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:

● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

# grado = float(input("Coloque el grado de Ritcher registrado > 0 y < 10: "))
# if  grado < 3:
#     print("La magnitud del terremoto es MUY LEVE")
# elif 3<= grado < 4:
#     print("La magnitud del terremoto es LEVE")
# elif 4<= grado < 5:
#     print("La magnitud del terremoto es MODERADO")
# elif 5<= grado < 6:
#     print("La magnitud del terremoto es FUERTE")
# elif 6<= grado < 7:
#     print("La magnitud del terremoto es MUY FUERTE")
# elif grado >= 7:
#     print("La magnitud del terremoto es EXTREMO")
# else:
#     print(f"Grado de la secala equivodado, verifique haber colocado un numero")

""" 10) Utilizando la información aportada sobre las estaciones del año:
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), 
qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano."""

hemisferio = str(input("Coloque S si viven en el Hemisferio Sur, o N si vive en el Hermisferio Norte: "))

mes = int(input("Coloque el numero del mes en el que se encuentra del 1 al 12: "))
dia = int(input("Coloque el numero del día en el que se encuentra del 1 al 31: "))


fecha = mes * 100 + dia  # ejemplo: 1 de febrero -> 101
# Hacemos un IF para saber en que hermisferio se encuentra, dependiendo cual de las dos opciones elija, se va a ejecutar una u otra.
if hemisferio == "S"or "s":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:   # utilizamos una conversion para colocar mes y dia en un numeros continuos MMDD
        estacion = "Verano"
    elif 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida" # En caso de que coloque una respuesta incorrecta imprimimos por pantalla FECHA INVALIDA o HEMISFERIO INVALIDO.

elif hemisferio == "N"or"n":
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Invierno"
    elif 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    elif 921 <= fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio inválido"

print(f"Usted se encuentra en {estacion}.") # Se muestra por pantalla la estacion correspondiente a las opciones eleginas.