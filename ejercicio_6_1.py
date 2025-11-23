# Ejercicio 6-1. Persona:
persona = {
    'nombre': 'pilar',
    'apellido': 'serrano',
    'edad': '39',
    'ciudad': 'barcelona'
}

print(persona)

print(f"Nombre: {persona['nombre'].title()}")
print(f"Apellido: {persona['apellido'].title( )}")
print(persona['edad'])
print(persona['ciudad'])

# Ejercicio 6-2. Números favoritos.

numeros_favoritos = {
    'pilar': 5,
    'rafa': 8,
    'juan': 12,
    'maria': 3
}

for persona, numero in numeros_favoritos.items():
    print(f"El número favorito de {persona.title()} es {numero}")
  



