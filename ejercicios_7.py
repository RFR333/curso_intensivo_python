# ejercicio 7-1. Coche de alquiler.

elegir_modelo = input("introduce el modelo deseado.")
print(f"\nVeamos si tenemos un {elegir_modelo.capitalize()} para usted.")

# Ejercicio 7-2. Mesa de restaurante.
comensales = input("Cuantos comensales seran a comer? ")
comensales = int(comensales)

if comensales >= 8:
    print("Lo siento tendrán que esperar , no tenemos mesas tan grandes.")
else:
    print("Su mesa está lista.")



# Ejercicio 7-3. Múltiplos de 10.
num_usuario = input("Introduce un número para saber si es múltiplo de 10.")
num_usuario = int(num_usuario)

if num_usuario % 10 == 0:
    print(f"El número: {num_usuario}, és múltiplo de 10")
else:
    print(f"El número: {num_usuario}, no és múltiplo de 10") 

# Ejercicio 7-4. ingrdientes pizza.
prompt = "\nIntroduce ingredientes para tu pizza."
prompt += "Introduce 'quit' para acabar"

ingredientes = ""
while ingredientes != 'quit':
    ingredientes = input(prompt)
    print(f"\nEl ingrediente '{ingredientes}' se añadira a la pizza.")

# Ejerciciop 7-5. Entradas de cine.

prompt = "\n¿Tu edad?"
prompt += "\nIntroduce 'quit' para salir."

while True:
    edad =input(prompt)

    if edad == 'quit':
        break
    edad = int(edad)

    if edad < 3:
        print("Tu entrada és gratis.")
    elif edad <= 12:
        print("Tu entrada vale 8€.")
    else:
        print("\nTu entrada vale 15€.")

# Ejercicio 7-6.Tres salidas.# Con 'active'.

prompt = "\nIntroduce un ingrediente para tu pizza:"
prompt += "\nEscribe 'quit' para salir: "

active = True
while active:
    ingrediente = input(prompt)

    if ingrediente == 'quit':
        active = False
    else:
        print(f"Se añadirá '{ingrediente}' a la pizza")

# Con break
prompt = "\nIntroduce un ingrediente para tu pizza:"
prompt += "\nEscribe 'quit' para salir: "

ingredientes = []

while True:
    ingrediente = input(prompt)

    if ingrediente == 'quit':
        break
    else:
        ingredientes.append(ingrediente)
        print(f"\nSe añadirá '{ingrediente}' en tu pizza.")

print("\ningredientes añadidos:", ingredientes)
