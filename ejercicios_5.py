# 5-1. Pruebas condicionales
car = 'subaru'
print("Is car == 'subaru'?")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Crea 10 True y 10 false.

moto = 'suzuki'
print("Is moto == 'suzuki")
print(moto == 'suzuki') # True
print(moto == 'yamaha') # False

bicicleta = 'panther'
print(bicicleta == 'panther') # True
print(bicicleta == 'bh') # False

coche = 'mercedes'
print(coche == 'mercedes') # True
print(coche == 'seat') # False

ordenador = 'windows'
print("\nOrdenador = windows")
print(ordenador == 'windows') # True
print("\nOrdenador = mac")
print(ordenador == 'mac')

televisor = 'lg'
print("\nTelevisor = lg")
print(televisor == 'lg')
print("\nTelevisor = philips")
print(televisor == 'philips')

# 5-2. Más condicionales.
edad_0 = 16
edad_1 = 21
print(edad_0 >= 21 and edad_1 >= 21) # False
print(edad_0 >= 21 or edad_1 >= 21) # True
edad_0 = 21
print(edad_0 >= 21 and edad_1 >= 21) # True

motos = ['aprilia', 'montesa', 'gilera', 'rieju', 'honda', 'suzuki']
print("Aprila esta en motos?")
print('aprilia' in motos) # True.
print("\nYamaha esta en motos?")
print('yamaha' in motos) # False.

print("\nMontesa esta en motos?")
print('montesa' in motos) # True.
print("\nHysquabarna esta en motos?")
print('hysquarbarna' in motos) # False.

print("\nMotor Hispania esta en motos?")
print('motor hispania' in motos)# False.
print("\nEsta Honda en Motos?")
print('honda' in motos) # True.

# Ejercicio 5-3. Colores de aliens
color_alien = 'verde'

if color_alien == 'amarillo':
    print("\nAlien derribado!!! has ganado 5 puntos!!!\n")
if color_alien == 'verde':
    print("Alien derribado!!! haqs ganado 5 puntos!!!\n")

color_alien1 = 'amarillo'

if color_alien1 == 'verde':
    print("alien derribado!!! has ganado 5 puntos")
else:
    print("alien derribado!!! has ganado 10 puntos\n")

color_alien = 'verde'
color_alien1 = 'amarillo'
color_alien2 = 'rojo'

if color_alien == 'verde':
    print("Enhorabuena has derribado el alien verde, 5 puntos!!!\n")
elif color_alien == 'amarillo':
    print("Enhorabuena has derribado el alien amarillo, 10 puntos!!!\n")
else:
    print("Enhorabuena has derribado el alien rojo, 15 puntos!!!\n")

color_alien = 'verde'

if color_alien == 'verde':
    print("Enhorabuena has derribado el alien verde, 5 puntos!!!\n")
elif color_alien == 'amarillo':
    print("Enhorabuena has derribado el alien amarillo, 10 puntos!!!\n")
else:
    print("Enhorabuena has derribado el alien rojo, 15 puntos!!!\n")

color_alien = 'amarillo'

if color_alien == 'verde':
    print("Enhorabuena has derribado el alien verde, 5 puntos!!!\n")
elif color_alien == 'amarillo':
    print("Enhorabuena has derribado el alien amarillo, 10 puntos!!!\n")
else:
    print("Enhorabuena has derribado el alien rojo, 15 puntos!!!\n")

color_alien = 'rojo'

if color_alien == 'verde':
    print("bien!!! has eliminado el alien verde!! 5 puntos")
elif color_alien == 'amarillo':
    print(" has eliminado el alien amarillo!!! 10 puntos")
else:
    print("Bien!!! Has eliminado el alien rojo!!! 15 puntos\n")

# Ejercicio 5-6. Etapas vitales.
edad = 1

if edad < 2:
    print("Todavía es un bebé\n")
elif edad >=2 and edad < 4:
    print("Todavía es un niño pequeño\n")
elif edad > 4 and edad < 13:
    print("Es un niño")
elif edad > 13 and edad <= 20:
    print("Es un adolescente\n")
elif edad > 20 and edad < 65:
    print("Es un adulto\n")
else:
    print("Tiene más de 65 años\n")

# ejercicio 5-7. Fruta favorita.
frutas_favoritas = ['plátano', 'fresas', 'manzanas', 'mandarinas', 'kiwis', 'cerezas']

if 'fresas' in frutas_favoritas:
    print(f"Pues si que te gustan las fresas")

if 'plátano' in frutas_favoritas:
    print("Pues te gustan los platanos")

if 'manzanas' in frutas_favoritas:
    print("Te gustan mucho las manzanas")

if 'mandarinas' in frutas_favoritas:
    print("También te gustan las mandarinas")

if 'kiwis' in frutas_favoritas:
    ("Tambien te gustan muchos los kiwis")

    if 'cerezas' in frutas_favoritas:
        print("Te gustan mucho las cerezas\n")


# Ejercicio 5-8. hola, admin:
usuarios = ['admin', 'kamil', 'maria', 'juan', 'sofia']

for usuario in usuarios:
   if usuario == 'admin':
       print(f"Bienvenido administrador, tienes acceso total")
   else:
       print(f"bienvenido {usuario}")

# Ejercicio 5-9. sin usuarios.
if not usuarios:
    print("La lista esta vacia")
else:
    for usuario in usuarios:
        print(usuario)

current_users = ['topo', 'kamicace', 'tigreton', 'pink panther', 'chamarin']
new_users = ['chamarin', 'armero', 'klaus', 'fly', 'topo']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user in current_users:
        print(f"El nombre: {new_user.title()}, ya esta en uso")
    else:
        print(f"nuevo usuario: {new_user.title()}")

# Ejercicio 5-11. Números ordinales.

for n in range(1, 10):
    if n == 1:
        print("\n1st")
    elif n == 2:
        print("2nd")
    elif n == 3:
        print("3rd")
    else:
        print(F"{n}th")

