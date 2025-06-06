# Lista de productos con nombre y precio
productos = [
    ["Mouse", 2500],
    ["Teclado", 3500],
    ["Monitor", 22000],
    ["Auriculares", 4800]
]

# Mostrar todos los productos
def mostrar(lista):
    for p in lista:
        print(p[0], "-> $", p[1])

# Ordenar productos por precio (manual)
def ordenar_por_precio(lista):
    return sorted(lista, key=lambda x: x[1])  # si preferís te hago sin sorted también

# Ordenar productos por nombre (manual)
def ordenar_por_nombre(lista):
    return sorted(lista)

# Buscar producto por nombre (búsqueda simple)
def buscar(nombre, lista):
    for p in lista:
        if p[0].lower() == nombre.lower():
            return p
    return None

# Mostrar productos ordenados por precio
print("Productos ordenados por precio:")
mostrar(ordenar_por_precio(productos))

# Mostrar productos ordenados por nombre
print("\nProductos ordenados por nombre:")
mostrar(ordenar_por_nombre(productos))

# Buscar producto
nombre_buscado = input("\n¿Qué producto querés buscar?: ")
resultado = buscar(nombre_buscado, productos)

if resultado:
    print("Producto encontrado:", resultado[0], "- $", resultado[1])
else:
    print("No se encontró el producto.")