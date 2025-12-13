
# Eliminar todos los valores de una lista que coincidan.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Rellenar un diccionario con entrada de usuario.
#montain_poll.py
responses = {}

# Configura bandera para saber que la encuesta a está activa.
polling_active = True

while polling_active:
    # Pide el nombre y la respuesta de la persona.
    name = input("\nwhat is your name? ")
    response = input("which mountain would you like to climb someday? ")
    #Guarda la respueta en el diccionario.
    responses[name] = response

    #Averigua si alguien más va a hacer la encuesta.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#La encuesta está completa. Muestra los resultados.
print("\n---polls results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")

# otro ejemplo.

respuestas = {}
encuesta_activa = True

while encuesta_activa:
    nombre = input("¿Cuál es tu nombre? ")
    pelicula = input("¿Cuál es tu película favorita? ")

    respuestas[nombre] = pelicula

    repetir = input("¿Deseas continuar la encuesta? (si/no) ")
    if repetir == "no":
        encuesta_activa = False

print("\nResultados:")
for nombre, pelicula in respuestas.items():
    print(f"{nombre} eligió: {pelicula}")
