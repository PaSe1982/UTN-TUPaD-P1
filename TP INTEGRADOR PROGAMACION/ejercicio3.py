import unicodedata

# Normaliza texto (pasa a minúscula y elimina acentos)
def normalizar(texto):
    return unicodedata.normalize("NFKD", texto.lower()).encode("ascii", "ignore").decode("ascii")

# Lista de productos: nombre, tipo, uso, precio
productos = [
    ["Lápiz negro", "lápiz", "escribir", 300],
    ["Lápiz rojo", "lápiz", "escribir", 350],
    ["Lápiz azul", "lápiz", "escribir", 350],
    ["Goma para lápiz", "goma", "borrar", 400],
    ["Goma para lapicera", "goma", "borrar", 450],
    ["Regla 20cm", "regla", "medir", 600],
    ["Regla 30cm", "regla", "medir", 700],
    ["Cuaderno rayado", "cuaderno", "escribir", 1200],
    ["Cuaderno cuadriculado", "cuaderno", "escribir", 1300],
    ["Lapicera azul", "lapicera", "escribir", 900],
    ["Lapicera negra", "lapicera", "escribir", 900],
    ["Lapicera roja", "lapicera", "escribir", 950],
    ["Tijera escolar", "tijera", "cortar", 1000],
    ["Cartuchera grande", "cartuchera", "guardar", 1800],
    ["Cartuchera mediana", "cartuchera", "guardar", 1500],
    ["Cartuchera chica", "cartuchera", "guardar", 1200]
]

# Funciones auxiliares
def mostrar(lista):
    for p in lista:
        print("-", p[0], "-> $", p[3])

def mostrar_numerado(lista):
    for i, p in enumerate(lista, start=1):
        print(f"{i}. {p[0]} -> $ {p[3]}")

def buscar_producto(nombre, lista):
    for p in lista:
        if normalizar(p[0]) == normalizar(nombre):
            return p
    return None

def buscar_variantes(nombre, lista):
    return [p for p in lista if normalizar(nombre) in normalizar(p[0])]

def buscar_por_uso(nombre, lista):
    for p in lista:
        if normalizar(nombre) in normalizar(p[0]):
            uso = p[2]
            return [x for x in lista if x[2] == uso and normalizar(nombre) not in normalizar(x[0])]
    return []

def validar_respuesta_si_no():
    while True:
        respuesta = input("¿Querés agregar otro artículo? (sí/no): ").strip().lower()
        if respuesta in ["sí", "si", "no"]:
            return respuesta
        print("La respuesta ingresada no es válida. Por favor respondé con 'sí' o 'no'.")

# Programa principal
carrito = []

print("\n¡Bienvenido/a a la librería EL SAPO PEPE!\nEstos son los artículos disponibles:\n")
mostrar(productos)

while True:
    nombre = input("\n¿Cómo se llama el producto que necesitás?: ").strip()
    resultado = buscar_producto(nombre, productos)

    elegido = None
    if resultado:
        elegido = resultado
    else:
        variantes = buscar_variantes(nombre, productos)
        if variantes:
            print("\nTenemos estas variantes:\n")
            mostrar_numerado(variantes)
            try:
                opcion = int(input("\nElegí el número del producto que querés: "))
                if 1 <= opcion <= len(variantes):
                    elegido = variantes[opcion - 1]
                else:
                    print("Opción fuera de rango. Producto no agregado.")
                    continue
            except ValueError:
                print("Entrada inválida. No se agregó ningún producto.")
                continue
        else:
            similares = buscar_por_uso(nombre, productos)
            print("\nEse producto no está disponible, ya lo agendo para comprar.\n")
            if similares:
                print("Te puedo ofrecer productos que cumplen una función similar:\n")
                mostrar(similares)
            else:
                print("Esto es todo lo que tenemos para ofrecerte:\n")
                mostrar(productos)
            continue

    try:
        cantidad = int(input(f"\n¿Cuántas unidades de '{elegido[0]}' querés comprar?: "))
        if cantidad <= 0:
            print("Cantidad inválida. Debe ser al menos 1.")
            continue
        carrito.append([elegido[0], elegido[1], elegido[2], elegido[3], cantidad])
        print(f"\nAgregado: {elegido[0]} - {cantidad} unidad(es) - Total: $ {elegido[3] * cantidad}\n")
    except ValueError:
        print("Cantidad inválida.")
        continue

    continuar = validar_respuesta_si_no()
    if continuar in ["no"]:
        break

# Mostrar resumen si se compró algo
if carrito:
    print("\nResumen de tu compra:\n")
    total_general = 0
    for item in carrito:
        nombre, tipo, uso, precio, cantidad = item
        total_parcial = precio * cantidad
        total_general += total_parcial
        unidad_txt = "unidad" if cantidad == 1 else "unidades"
        print(f"- {nombre} ({cantidad} {unidad_txt}) = $ {total_parcial}")

    print(f"\nEl total a abonar es: $ {total_general}\n")
else:
    print("\nNo se realizó ninguna compra.")