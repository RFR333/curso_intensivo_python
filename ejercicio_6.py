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

# Ejercicio 6-3.6-4 Glosario.
glosario = {
    'print()': 'Impimir en consola python',
    'variable': 'Esopacio en memoria',
    'sort()': 'Ordena alfabeticamente, modifica el archivo',
    'and':'Devuelve True si ambas condiciones se cumplen',
    'or': 'Devuelve True si se cumple al menos una condición',
    'not': 'Invierte el valor logico: True-> False y False-> True',
    'if': 'Evalua una condicion, si es verdadera, ejecuta código',
    'elif': 'Si no entra el if o , pasa a ejecutar elif',
    'else': 'Bloque que se ejecuta si no entra en ninguna condición anterior',
    'for': 'Bucle que recorre elementos de una lista, diccionario, cadena o rango',
    'while': 'Bucle que se ejecuta mientras se cumpla una condicion',
    'break': 'Sale inmediatamente de un bucle(detiene todo el bucle)',
    'continue': 'Salta iteración actual y continúa con la siguiente',
    'in': 'Comprueba si un valor está dentro de una lista,d diccionario, cadena, etc',
    'not in': 'Comprueba que un valor no esta en una lista, diccionario, etc',
    'def': 'Define una función',
    'return': 'devuelve un valor desde una función',
    'class': 'Crea una clase (programación orientada a objetos)',
    'Import': 'Impota módulos o librerias',
    'from': 'Importa algo específico de un módulo',
    'as': 'Crea un alias',
    'none': 'Significa ningún valor, es equivalente a "vacio".',
    'True': 'Valor booleano verdadero',
    'False': 'Valor booleano falso',
    'try': 'intenta ejecutar un bloque de código que podría fallar',
    'except': 'Bloque que se ejecuta si ocurre un error dentro de try',
    'finally': 'Bloque que se ejecuta siempre, ocurra error o no',
    'with': 'Maneja automáticamente recursos como archivos',

}

for key, value in glosario.items():
    print(f"\nLa palabra clave: {key.title()}: su definición es:{value.title()}")

# Ejercicio 6-5. Rios:
rios = {
    'nilo': 'egipto',
    'ebro': 'españa',
    'amazonas': 'sur america',
    'missisipi': 'estados unidos',
    'miño': 'españa',
}

for key, value in rios.items():
    print(f"\nEl rio {key.title()}, esta en {value.title()}")

for rio in rios:

    if rio == 'nilo':
        print(f"\nEl rio: {'nilo'.title()}, discurre por Egipto.")
    elif rio == 'ebro':
        print(f"\nEl rio: {'ebro'.title()}, el rio Ebro discurre por España.")
    elif rio == 'amazonas':
        print(f"\nEl rio: {'amazonas'.title()}, discurre por Sur América.")
    elif rio  == 'missisipi':
        print(f"\nEl rio {'missisipi'.title()}, discurre poe estados unidos.")
    elif rio == 'miño':
        print(f"\nEl rio {'miño'.title()}, discurre por España")

  
# Ejercicio 6-6.sondeos:


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['manolo', 'cristina']

# 1. Revisar a los que ya han respondido
for name in favorite_languages.keys():
    print(f"\n{name.title()}, gracias por completar la encuesta.")

# 2. Revisar quién NO ha respondido.
for friend in friends:
    if friend not in favorite_languages:

        print(f"\n{friend.title()}, por favor rellena la encuesta.")

# forma mas efectiva, mas abreviado.    
for person in friends:
    if person in favorite_languages:
        print(f"\n{person.title()}, ya completaste la encuesta. ¡Gracias!")
    else:
        print(f"\n{person.title()}, por favor completa la encuesta.")



# ejemplo diccionarios.
tienda_A = {
    "martillo": 12.50,
    "taladro": 79.90,
    "destornillador": 5.20,
    "sierra": 22.00
}
tienda_B = {
    "martillo": 11.00,
    "llave inglesa": 14.80,
    "taladro": 75.00,
    "cinta métrica": 3.50
}

print("\n--- Catálogo Tienda A ---")
for herramienta, precio in tienda_A.items():  # herramienta = clave(key), precio 0 valor(value).
    print(f"{herramienta.title()}: {precio}")

print("--- Catálogo Tienda B ---")
for herramienta, precio in tienda_B.items():
    print(f"{herramienta.title()}: {precio}")

for herramienta in tienda_B:
    if herramienta in tienda_A:
        print(f"\nHerramienta: {herramienta.title()}, ya esta en catálogo.")
        print(f"Precio A: {tienda_A[herramienta]} €")
        print(f"Precio B: {tienda_B[herramienta]} €")

    else:
        print(f"\nHay que comprar: {herramienta.title()}, no hay en stock.")


# Otro ejemplo.
digitalizacion = {
    "vhs": 14,
    "vhsc": 6,
    "minidv": 9,
    "hi8": 3,
    "audio_cassette": 12
}
cliente = {
    "vhs": 10,
    "minidv": 4,
    "betamax": 2,
    "audio_cassette": 5,
    "carrete_8mm": 1
}

print("\nInformación Diccionario 1")
for formato, cantidad in digitalizacion.items():
    print(f"\n {formato}, cantidad de cintas: {cantidad}")

print("\nInformación Diccionario 2")
for formato, cantidad in cliente.items():
    print(f"\n {formato}, cantidad de cintas: {cantidad}")

print("\nEstamos con bastante trabajo en este formato.")
for formato in sorted(cliente):
    if formato in digitalizacion:
        print(f"{formato.title()}")

# Comparar cantidades.
for formato, cantidad_cliente in cliente.items():
    # Comprobar que existe formato.
    if formato in digitalizacion:
        cantidad_tienda = digitalizacion[formato]
        print(f"\nFormato: {formato.title()}")
        print(f"Cliente trae: {cantidad_cliente}")
        print(f"Tu capacidad: {cantidad_tienda}")
        # comparación de cantidades.
        if cantidad_cliente > cantidad_tienda:
            print("El cliente trae MÁS de la capacidad de la tienda.")
        elif cantidad_cliente < cantidad_tienda:
            print("Hay capacidad de sobra para este formato.")
        else:
            print("Volumen exacto! Trae las cintas.")
    else:
        print(f"No trabajamos ese formato: {formato.title()}")