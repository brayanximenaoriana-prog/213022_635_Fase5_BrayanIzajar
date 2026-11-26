# UNAD - Fundamentos de Programacion
# Fase 5 - Evaluacion Final POA
# Estudiante: Brayan Izajar Escobar
# Grupo: 213022_635
# Problema 2 - Promocion de un restaurante

# Constantes de la promocion
CATEGORIA = "Platos fuertes"
UMBRAL = 20000
DESCUENTO = 0.15

# Matriz de productos
productos = [
    ["Bandeja paisa", "Platos fuertes", 30000],
    ["Pollo a la plancha", "Platos fuertes", 25000],
    ["Hamburguesa", "Platos fuertes", 18000],
    ["Limonada", "Bebidas", 6000],
    ["Helado", "Postres", 8000],
    ["Ensalada especial", "Platos fuertes", 20000],
    ["Torta especial", "Postres", 25000]
]

# Funcion para calcular el precio final
def calcular_precio_final(categoria, precio):
    if categoria == CATEGORIA and precio > UMBRAL:
        return precio - precio * DESCUENTO
    else:
        return precio

# Mostrar los resultados de cada producto
print("PROMOCION DEL RESTAURANTE - 15 %")
print("-" * 50)

for nombre, categoria, precio in productos:
    precio_final = calcular_precio_final(categoria, precio)
    print("Producto:", nombre)
    print("Precio base: $", precio)
    print("Precio final: $", round(precio_final, 2))
    print("-" * 50)
