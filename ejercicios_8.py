
# Ejercicio 8-1. Mensaje.

def mostrar_mensaje():
    print("En este capítulo estamos aprendiendo funciones.")

mostrar_mensaje()
print("-" * 40)

# Ejercicio 8_2. Libro favorito.

def libro_favorito(titulo):
    """libro favorito."""
    print(f"Mi libro favorito es: {titulo.capitalize()}")

libro_favorito('viven')
print("-" * 40)

# Ejercicio 8-3. Camiseta.
def camiseta(talla, texto):
    """Haz tu propia camiseta indicando talla y texto"""
    print(f"\nVoy a fabricar una camiseta de la talla: 👕 {talla}.")
    print(f"El texto es: \t'{texto}'")

camiseta('XL', 'I love python')
print("-" * 40)

# Ejercicio 8-4. Camisetas grandes.
"""Camiseta grande"""
def hacer_camiseta(talla, mensaje):
    print(f"\nVoy a fabricar una camiseta de la talla:👕 {talla}")
    print(f"el texto será: '\t{mensaje}'")

hacer_camiseta('XL', 'I love python')
hacer_camiseta('M', 'I love python')
hacer_camiseta('L', 'I love COMPUTER')
print("-" * 40)

# ejercicio 8-5. ciudades.
def describir_ciudad(ciudad, pais='españa'):
    print(f"\nLa ciudad: {ciudad.capitalize()}, está en: 🌍 {pais.capitalize()}")

describir_ciudad('barcelona')
describir_ciudad('madrid')
describir_ciudad('murcia')
describir_ciudad('dublín', 'irlanda')
print("-" * 40)

