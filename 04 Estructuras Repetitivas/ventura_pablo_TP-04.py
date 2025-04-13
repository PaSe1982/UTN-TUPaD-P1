"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea
Ejercicio 1: Ciclo for que muestra por pantalla los numeros del 0 al 100"""

# for i in range(101): ## usamos un ciclo for donde por defecto, el contador i ya arranca de "0"
#   print(i)

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

# num = abs(int(input("Ingrese un mumero entero: ")))  ## la funcion "abs" no tiene en cuenta los signos, solo toma el valor absoluto 
# cont = 0

# if num == 0:
#     cont == 1
# else:
#     while num > 0:
#         num = num // 10    ## Con esto logramos quedarnos solo con la parte entera
#         cont += 1
# print(f"La cantidad de digitos ingresados es {cont}: ")

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

# suma_num = 0
# num1 = int(input(f"Ingrese un numero entero: "))
# num2 = int(input(f"Ingrese otro numero mayor que {num1}: "))
# if num1>=num2:   ## Nos aseguramos de que el programa se ejecute sin error, en caso de que ponga un numero fueda de las indicaciones por pantalla, le sale un cartel que está ingrensando numeros equivocados
#     print(f"Los numeros ingresados no respetan la consigna, vuelva a intentarlo")
# else:
#     while num1+1<num2:
#         num1 += 1
#         suma_num = suma_num + num1
#     print(f"La suma de los numeros que se encuentran entre los ingresados, es: {suma_num} ")




"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

# num = int(input("Ingrese un numero entero: "))
# sumatoria = 0
# while num != 0:
#     sumatoria = sumatoria + num
#     num = int(input("Ingrese un numero entero: "))
# print(f"La sumatoria de numeros ingresados es: {sumatoria}")

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número"""

# cont_intentos = 1
# from random import randint
# num_adivino = randint(0,9)
# num = int(input("Ingrese un numero entero entre 0 y 9: "))
# while num_adivino != num:
#     num = int(input("Ingrese un numero entero entre 0 y 9: "))
#     cont_intentos += 1
# print(f"Felicitaciones, acertó el número secretro, la cantidad de intentos realizados fueron: {cont_intentos}")

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente"""

# for i in range(101):
#     if i%2 == 0:
#         print(f"Los numeros pares del 0 al 100 son los siguientes: {i}")

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""
# suma = 0
# num_elegido = int(input("Ingrese un valor entero y positivo: "))
# if num_elegido >= 0:
#     for i in range(num_elegido):
#         suma = suma + i
#     print(f"La suma es: {suma}")
# else:
#     print(f"Error, ingresó un numero erroneo")

"""8) Escribe un programa que permita al usuario ingresar 100 números enteros.
Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

# con_par = 0
# con_impar = 0
# num_positivo = 0
# num_negativo = 0
# cont_numero = 1


# while cont_numero <= 100:       # Bucle while que repite la operacion hasta que se ingresen 100 numeros

#     num = int(input(f"{cont_numero} - Ingrese 100 números enteros:")) # a medida que se ingresen los numeros voy mostrando por pantalla el contador de los mismos           
#     if num % 2 == 0:
#         con_par += 1
#     else:
#         con_impar += 1
#     if num > 0:
#         num_positivo +=1
#     elif num < 0:
#         num_negativo +=1
#     cont_numero += 1 

    
# print(f"Cantidad de numeros pares ingresados: ", con_par)
# print(f"Cantidad de numeros impares ingresados: ", con_impar)
# print(f"Cantidad de numeros positivos ingresados: ", num_positivo)
# print(f"Cantidad de numeros negativos ingresados: ", num_negativo)

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

# cont_numero = 0
# sumatoria = 0

# while cont_numero < 5:
#     num = int(input(f"{cont_numero} - Ingrese 100 números enteros para encontrar la media:"))
#     cont_numero += 1
#     sumatoria = sumatoria + num
# media = float(sumatoria/(cont_numero))
# print(f"La media de los valores ingresados es: {media}")

"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

# numero_invertido = 0
# num = int(input("Ingrese un número mayor que 0: "))

# while num > 0:
#         digito = num % 10                                    # saco el último dígito
#         numero_invertido = numero_invertido * 10 + digito    # lo agrego al invertido
#         num = num // 10                                      # le saco el último dígito
# print(f"El número invertido es: {numero_invertido}")        # PD: la verdad no sabia como hacerlo
