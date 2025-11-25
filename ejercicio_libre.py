producto = {
    "nombre": "Taladro eléctrico",
    "categoria": "Herramientas",
    "precio": 79.90,
    "stock": 12,
    "caracteristicas": {
        "potencia": "500W",
        "peso": "1.2kg",
        "inalambrico": False
    },
    "proveedor": {
        "nombre": "Suministros BCN",
        "telefono": "934112233"
    }
}

print(producto['nombre']) # acceso al nombre.
print(producto['categoria']) # acceso a la categoria.
print(producto['precio']) # acceso al precio.
print(producto['stock']) # acceso al stock.
print(producto['caracteristicas']['potencia']) # acceso  al subdiccionario, potencia.
print(producto['caracteristicas']['peso']) # acceso al subdiccionario, peso.
print(producto['caracteristicas']['inalambrico']) # acceso al subdiccionario, inalambrico.
print(producto['proveedor']['nombre']) # acceso al subdiccionario, nombre del proveedor.
print(producto['proveedor']['telefono']) #  acceso al subdiccionario, telefono del proveedor.

# Modificar un dato.

print("\nModificando el stock...\n")
producto = {
    "nombre": "Taladro eléctrico",
    "categoria": "Herramientas",
    "precio": 79.90,
    "stock": 12,
    "caracteristicas": {
        "potencia": "500W",
        "peso": "1.2kg",
        "inalambrico": False
    },
    "proveedor": {
        "nombre": "Suministros BCN",
        "telefono": "934112233"
    }
}

producto['stock'] = 20
print(producto['stock']) # acceso al dato modificado.
# Añadir un nuevo par clave valor.
print("\nAñadiendo un nuevo par clave valor..\n")
producto['descuento'] = 10 # descuentoen porcentaje.
print(producto['descuento']) # acceso al nuevo par clave valor.
print(producto)
# Eliminar un par clave valor.
print("\nEliminando el par clave valor descuento...\n")
del producto['descuento']
print(producto)

# Ejercicio 4.5- máximo de una lista.
numeros = [3, 7, 2, 9, 4, 1, 8, 6, 5]
max_num = numeros[0]
for num in numeros:
    if num > max_num:
        max_num = num

print(f"El número mayor de la lista es: {max_num}")

# Ejercicio 5.1- bicicletas y métodos de listas.
bycicles = ['trek', 'cannondale', 'redline', 'specialized']
print(bycicles)

print(bycicles[0].title()) # accede al primer elemento de la lista.
print(bycicles[-1].title()) # accede al ultimo elemento de la lista.
 

 


