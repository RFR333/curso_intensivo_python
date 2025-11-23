# Sentencias if.
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Comprobar desigualdad.
# (!=), no es igual.

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovias!")

# Comparaciones numéricas.
age = 18
if age == 18:
    print('true')
#True.

# 
answer = 17

if answer != 42:
    print("That is not the correct answer. please try again!")

# Comparaciones matemáticas.
age = 19
age < 21
print(True)

age <= 21
print(True)
age > 21
print(False)

age >= 21
print(False)

# Comprobar varias condiciones con AND.

age_0 = 22
age_1 = 18
age_0 <= 21 and age_1 >= 21
print(False)
age_1 =22
age_0 >= 21 and age_1 >= 21
print (True)

# Usar OR para comprobar varias condiciones.
age_0 >= 21 or age_1 >= 21
print(True)

age_0 = 18
age_0 >= 21 or age_1 >= 21
print(False)

# Comprobar si hay un valor en una lista.
requested_toppings = ['mushrooms', 'onios', 'pineapple']
'mushrooms' in requested_toppings
print(True)

'pepperini' in requested_topping
print(False)

# Comprobar que un valor no esta en la lista.
banned_users = ['andrew', 'carolina', 'david'] 
user = 'marie'

if user not in  banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Clases de sentencias if.
# Simple.
edad = 19
if edad >= 18:
    print("\nEres mayor de edad y puedes votar!")
    print("Ya estas censado para votar?")

# Sentencias if-else.
edad = 17
if edad >= 18:
    print("\nEres mayor de edad y puedes votar!")
    print("Ya estas censado para votar?")
else:
    print("\nLo siento no tienes edad de votar.")
    print("por favor registrate para poder votar")

# Cadena if-elif-else.
edad = 12
if edad < 4:
    print("\nLa entrada a menor de 4 es gratis.")
elif edad < 18:
    print("\nEl precio para menores de 18 es de 25 euros.")
else:
    print("\nLa entrada vale 40 euros.")

# Cualquier cifra por encima de 17 se ira para el else.
edad = 19
if edad < 4:
    precio = 0
elif edad < 18:
    precio = 25
else:
    precio = 40

print(f"\nLa entrada te cuesta {precio} euros.")

edad = 67

if edad <= 4:
    precio = 0
elif edad < 18:
    precio = 25
elif edad < 65:
    precio = 40
elif edad >= 65: # omitir  bloque else por claridad del codigo.
    precio = 20
print(f"\nLa entrada cuesta {precio} euros\n")

# Comprobar todas las condiciones de interés.
ingredientes_requeridos = ['champiñones', 'extra queso']

if 'champiñones' in ingredientes_requeridos:
    print("Añadiendo champiñones\n")
if 'pepperoni'in ingredientes_requeridos:
    print("Añadiendo pepperoni\n")
if 'extra queso' in ingredientes_requeridos:
    print("Anadiendo extra queso\n")

print("¡Tu pizza está recien hecha!\n")

# Sentencias if con listas.
ingredientes_requeridos = ['champiñones', 'pimientos verdes', 'extra queso']

for ingrediente_requerido in ingredientes_requeridos:
    print(f"Añadiendo {ingrediente_requerido}.")

print("\nLa pizza esta lista\n")

for ingrediente_requerido in ingredientes_requeridos:
    if ingrediente_requerido == 'pimientos verdes':
        print("Lo sentimos, los pimientos verdes se han acabado.")

    else:
        print(f"Añadiendo ingredientes: {ingrediente_requerido}")
print("\nLa pizza ya está lista.")

# Comprobar si una lista no está vacia.
ingredientes_necesarios = []

if ingredientes_necesarios:
    for ingrediente_necesario in ingredientes_necesarios:
        print(f"Añadiendo{ingrediente_necesario}.") 
    
else:
    print("\nEsta seguro que quieres esta pizza?\n")

# Usar múltiples listas.
ingredientes_disponibles = ['champiñones', 'olivas', 'pimientos verdes', 'pepperoni',
                            'piña', 'extra queso']
ingredientes_necesarios = ['champiñones', 'patatas fritas', 'extra queso']

for ingrediente_necesario in ingredientes_necesarios:
    if ingrediente_necesario in ingredientes_disponibles:
        print(f"Añadiendo {ingrediente_necesario}")
    else:
        print(f"lo sentimos no hay {ingrediente_necesario}")

print("\nSu pizza esta lista")
    