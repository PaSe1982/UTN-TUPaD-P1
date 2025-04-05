# TRABAJO PRACTICO N° 3

## EJERCICIO I

## Declaramos una variable entera, llamada "edad", y le pedimos al usuario que ingrese la misma

#edad = int(input("Por favor, ingrese su edad "))

## Abrimos la condicional if, si edad > que 18, se mostrara por pantalla: Es mayor de edad, y por ultimo la palabra adios

#if edad > 18:
#    print("Es mayor de edad")

## En caso de que sea menor que 18 años, pasara por alto y solo mostrará por pantalla la palabra adios.

#else:
#    pass
#print("Adios")




## EJERCICIO 2:

# nota = float(input("Por favor, ingrese su nota "))
# if nota >= 6:
#    print("aprobado")
# else:
#    print("desaprobado")



## EJERCICIO 3:

# num = int(input("Por favor ingrese un numero par: "))
# if num % 2 == 0:
#    print("Ha ingresado un numero par")
# else:
#    print("Por favor ingrese un numero par")


## EJERCICIO 4:

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


## EJERCICIO 5:

#contraseña = str(input("Por favor ingrese una contraseña de entre 8 y 14 caracteres: "))
#if 8 <= len(contraseña) <= 14:
#    print("Usted ha ingresado una contraseña correcta")
#else:
#    print("ERROR: la contraseña debe tener entre 8 y 14 caracteres, vuelva a intentar")

## EJERCICIO 6:

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

