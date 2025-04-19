#-----------------------------------------------------------------------------------------------------
#  Práctico 2: Funciones en Python - ALUMNO: VENTURA PABLO SEBASTIAN
#-----------------------------------------------------------------------------------------------------


""" 1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""

# FUNCIONES

def hola_mundo():       # Se realiza la funcion en donde se muestra en pantalla "Hola Mundo"
    print("Hola Mundo")

# PRINCIPAL

hola_mundo() # Se llama a la funcion, mostrando por pantalla el texto que aparece en la funcion

#--------------------------------------------------------------------------------------------------------

""" 2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
“Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""

# FUNCIONES

def saludar_usuario(nombre):
    return (f"Hola {nombre} !!!")

# PRINCIPAL

nombre = input("Como te llamas? ")
saludo = saludar_usuario(nombre)
print(saludo)

#--------------------------------------------------------------------------------------------------------

""" 3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
los datos al usuario y llamar a esta función con los valores ingresados."""

# FUNCIONES

def informacion_personal(nombre, apellido, edad, residencia):
    
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} ")


# PRINCIPAL

nombre = input("Ingresa tu nombre? ")         ## SE PIDE QUE INGRESE LOS DATOS PERSONALES 
apellido = input("Ingresa tu apellido? ")
edad = input("Cual es tu edad? ")
residencia = input("De donde sos? ")

informacion_personal(nombre, apellido, edad, residencia) ## AL LLAMAR A LA FUNCION SE IMPRIME LOS VALORES MENCIONADOS EN UNA ORACION

#------------------------------------------------------------------------------------------------------------------

""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
como parámetro y devuelva el área del círculo. calcular_perimetro_
circulo(radio) que reciba el radio como parámetro y devuelva
el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
funciones para mostrar los resultados."""

from math import pi ## Importo de la libreria de Math el numero PI

FUNCIONES

def calcular_area_circulo(radio):  # Funcion para calcular el area
    
    return pi * (radio**2)

def calcular_perimetro_circulo(radio):  # # Funcion para calcular el perimetro
    return 2 * pi * radio

# PRINCIPAL

radio = float(input("Ingrese el radio del circulo al cual quiere calcular el area: "))  # Se le pide al usuario que ingrese el valor del radio de un circulo
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
# Se muestra por pantalla el resultado del area y del perimetro correspondiente al circulo cuyo radio han introducido,
#  y se utiliza : .2f para obtener solo dos decimales
print(f"El area del ciculo es: {area:.2f} y el perimetro es {perimetro:.2f}")  


#-----------------------------------------------------------------------------------------------------------------------------
""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar
el resultado usando esta función."""

FUNCIONES
def segundos_a_horas(seg):
    return seg/3600


PRINCIPAL

segundos = int(input("Ingrese la cantidad de segundos a convertir: "))
while segundos <= 0:
    segundos = int(input("Ingrese un valor valido: "))

horas = segundos_a_horas(segundos)      # El usuario ingresa un numero correspondiente a la cantidas de segundos a convertir
print(f"Los segundos que ingresó equivalen a {horas:.3f} horas")


#------------------------------------------------------------------------------------------------------
""" 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro e imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""

# FUNCIONES

def tabla_multiplicar(num): # Funcion que genera una tabla de multiplicar con el numero que ingresó el usuario
    for i in range(1,11):
        resultado = num * i
        print(f"{num} X {i} = {resultado}")


# PRINCIPAL

# Se pide al usuario que ingrese un numero entero del 1 al 10

numero = int(input("Ingrese un numero entero del 1 al 10 para saber su tabla de multiplicar: ")) 

# Bucle while para evitar que coloque numeros erroneos
while numero<1 or numero>10:
    numero = int(input("Numero equivocado, vuelva a elegir un numero entero del 1 al 10: "))

# Se imprime tabla siempre y cuando el numero ingresado esté en el rango del 1 al 10
tabla_multiplicar(numero)

#--------------------------------------------------------------------------------------------------------------

""" 7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado
de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
de forma clara."""

# FUNCIONES

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    tupla =[suma,resta, multiplicacion, division]
    return tupla


# PRINCIPAL

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
operaciones = operaciones_basicas(num1, num2)
print(f"La suma de los numeros ingresados es: {operaciones[0]}")
print(f"La resta de los numeros ingresados es: {operaciones[1]}")
print(f"La multiplicacion de los numeros ingresados es: {operaciones[2]}")
print(f"La diviison de los numeros ingresados es: {operaciones[3]}")

#------------------------------------------------------------------------------

""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
para mostrar el resultado con dos decimales."""

# FUNCIONES
def calcular_imc(peso, altura):
    imc = (peso /(altura**2))
    return imc


# PRINCIPAL
peso = float(input("Ingrese su peso corporal en Kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
indice_calculado = calcular_imc(peso,altura)
print(f"El IMC calculado es: {indice_calculado:.2f}")

#---------------------------------------------------------------------------------------------------


""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""

# FUNCIONES 
def celsius_a_fahrenheit(celsius):
    temperatura = (celsius * 1.8) + 32
    return temperatura

# PRINCIPALES
celsius = float(input("Ingrese la termperatura en °C que desea convertir a ° Farenheit: "))
conversion = celsius_a_fahrenheit(celsius)
print(f"La conversion de °C a °F es: {conversion:.2f}")

#-----------------------------------------------------------------------------------------


""" 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función. """

# FUNCION

def calcular_promedio(a, b, c):
    promedio = (a + b + c)/3
    return promedio


# PRINCIPAL

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los tres números ingresados es: {promedio:.2f}")
