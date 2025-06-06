""" TRABAJO PRACTICO INTEGRADOR DE PROGRAMACION
            BUSQUEDA Y ORDENAMIENTO"""

productos = [
    {"nombre": "Mouse", "precio": 2500},
    {"nombre": "Teclado", "precio": 3500},
    {"nombre": "Monitor", "precio": 22000},
    {"nombre": "Auriculares", "precio": 4800}
]
def mostrar_productos(lista):
    for p in lista:
        print(f"{p['nombre']}: ${p['precio']}")

def ordenar_por_precio():
    return sorted(productos, key=lambda x: x['precio'])

def ordenar_por_nombre():
    return sorted(productos, key=lambda x: x['nombre'])

def busqueda_lineal(nombre):
    for p in productos:
        if p['nombre'].lower() == nombre.lower():
            return p
    return None

# Prueba de funciones
print("Productos ordenados por precio:")
mostrar_productos(ordenar_por_precio())

print("\nProductos ordenados por nombre:")
mostrar_productos(ordenar_por_nombre())

buscar = input("\nIngrese un producto para buscar: ")
resultado = busqueda_lineal(buscar)
if resultado:
    print(f"Producto encontrado: {resultado['nombre']} - ${resultado['precio']}")
else:
    print("Producto no encontrado.")



