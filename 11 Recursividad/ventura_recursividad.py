""" 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
"""

"""

# Funcion recursiva para calcular el factorial de un numero
def sacar_factorial(num):
# Caso base: Si el valor del numero es "0" o "1", el factorial es "1"
    if num <= 1:
        return 1
# Caso recursivo: Multiplico el numero, por el numero anterior    
    return num * sacar_factorial(num - 1)
# Se pide al usuario que ingrese un numero hasta el cual quiera factorear
limite = int(input("Hasta qué número querés ver los factoriales: "))

for i in range(1, limite + 1):
# Acá imprimo por pantalla el resultado del factorial de cada numero
    print(f"El factorial de {i} es {sacar_factorial(i)}")

"""

#----------------------------------------------------------------------------------
""" 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique"""

"""

# Esta es la funcion recursiva de Fibonacci para la cantidad "n" dada por el usuario
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

# Pedimos al usuario cuántos valores quiere ver...
cantidad = int(input("¿Cuántos números de la serie de Fibonacci querés ver?: "))
# Imprimimos por partalla el cada valor de la serie junto a su posicion
print("La serie de Fibonacci con sus posiciones es:")
# Al poner "cantidad + 1" estamos incluyendo ese ultimo numero que el usuairo ingresa
for i in range(cantidad+1):
    print(f"Para posición {i} = {fibo(i)}")

"""    

#----------------------------------------------------------------------------------    
""" 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula n^m  = n ∗ 𝑛^(𝑚−1).
Prueba esta función en un algoritmo general."""

"""

# Hago una función que saque la potencia de un número usando recursividad
def sacar_potencia(base, exponente):
    # Si el exponente es 0, cualquier número da 1
    if exponente == 0:
        return 1
    # Si no, multiplico la base por la función otra vez con uno menos
    return base * sacar_potencia(base, exponente - 1)
# Se le pide al usuario que ingrese los valores
base = int(input("Ingresá la base: "))
exp = int(input("Ingresá el exponente: "))

# Se imprime por pantalla el resultado
print(f"{base} elevado a la {exp} es igual a: {sacar_potencia(base, exp)}")

"""

#----------------------------------------------------------------------------------
""" 4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto."""

"""

# Esta función que convierte un número decimal a binario usando la recursividad
def decimal_a_binario(num):
    if num == 0:
        return ""
    return decimal_a_binario(num // 2) + str(num % 2)

# Esta es para manejar el caso cuando se pone 0
def convertir(num):
    if num == 0:
        return "0"
    return decimal_a_binario(num)

# Se le pide al usuario que ingrese un número
num = int(input("Escribí un número decimal para pasarlo a binario: "))

# Se imprime por pantallal el resultado
print(f"El número {num} en binario es: {convertir(num)}")

"""

#----------------------------------------------------------------------------------
""" 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()."""

"""

# Hago una función que diga si una palabra es palíndromo o no, usando recursividad
def es_palindromo(palabra):
    # Si la palabra tiene 0 o 1 letra, ya es palíndromo
    if len(palabra) <= 1:
        return True
    # Si la primera y la última letra no son iguales, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    # Si son iguales, saco esas dos letras y vuelvo a llamar la función
    return es_palindromo(palabra[1:-1])
texto = input("Escribí una palabra (sin espacios ni tildes): ").lower()
if es_palindromo(texto):
    print("Es un palíndromo ")
else:
    print("No es un palíndromo ")


"""

#----------------------------------------------------------------------------------
""" 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
"""

"""

# <defino función recursiva que sume los dígitos de un número entero positivo
def suma_digitos(n):
    # Si el número tiene un solo dígito, lo devuelvo directamente
    if n < 10:
        return n
    # Si tiene más de un dígito, sumo el último con el resto de la función
    return (n % 10) + suma_digitos(n // 10)

# Pruebas para ver si funciona
print(suma_digitos(15812))  # 17
print(suma_digitos(9))     # 9
print(suma_digitos(345))   # 12

"""

#----------------------------------------------------------------------------------
""" 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)
"""

"""

# Defino una función recursiva para contar cuántos bloques se necesitan en total para hacer la piramide
def contar_bloques(n):
    # Caso base: si hay un solo bloque, se devuelve "1"
    if n == 1:
        return 1
    # Caso recursivo: sumo los bloques de este nivel con los que vienen arriba
    return n + contar_bloques(n - 1)
bloques = int(input("¿Cuantos bloques tiene la base de la piramide?: "))
print(f"Para construir toda la pirámide se necesitan {contar_bloques(bloques)} bloques")

"""

#----------------------------------------------------------------------------------

""" 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4 
contar_digito(123456, 7) → 0
"""


# Defino una función recursiva para contar cuántas veces aparece un dígito dentro de un número
def contar_digito(numero, digito):
    # Caso base: si el número tiene un solo dígito
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    # Caso recursivo: reviso el último dígito y sumo si coincide
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# Pruebas para ver si funciona
print(contar_digito(12233421, 1))  # 2
print(contar_digito(5555223, 3))   # 1
print(contar_digito(123456, 8))    # 0

#----------------------------------------------------------------------------------