dimensiones = (200, 50)
print(dimensiones[0])
print(dimensiones[1])

# Si intentamos cambiar da error.
#dimensiones[0] = 250, da error por que no se puede cambiar tupla.
for dimension in dimensiones:
    print(dimension)

# Sobreescribir una tupla.
dimensiones =(400, 100)
print("\ndimensiones modificadas:")
for dimension in dimensiones:
    print(dimension)

