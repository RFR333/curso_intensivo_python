bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0]) # accede al primer elemento de la lista.
print(bicycles[0].title()) # con mejor salida.
print(bicycles[1].title()) # 2º elemento.
print(bicycles[3].title()) # 4º elemento.
print(bicycles[-1].title()) # Accede al último elemento de la lista.

# Mensaje conla primero bicicleta de la lista.
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

# métodos para trabajar con listas.

motorcycles = ['honda', 'yamaha', 'suzuki']

# Añadir un elemento con método upper()
motorcycles.append('ducati')
print(motorcycles)

# método pop(), permite eliminar el ultimo elemento...sin argumento.
last_owned = motorcycles.pop()
print(f"The last  motorcycle I owned was a {last_owned.title()}")

# Método pop(), con argumento permite eliminar cualquier elemento por 
# posición y si lo envuelves en variable puedes reutilizar el elemento.
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

# vuelvo a añadir  honda y ducati.
motorcycles.append('honda')
motorcycles.append('ducati')
print(", ".join(motorcycles))

# remove(), permite trabajar con el valor eliminado.
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"nA {too_expensive.title()} is too expensive for me.")
print(", ".join(motorcycles))
motorcycles.append('aprilia')

# Método remove(), Eliminar un elemento por valor.
# motorcycles.remove('ducati')
# print(motorcycles)

# Método sort(), ordena alfabéticamente.Metodo reverse(True) alfabeto inverso.
# motorcycles.sort()
print(", ".join(motorcycles))

# Con el método sorted() se ordena alfabética temporalmente, se mantiene la lista original.

print("this is the original list:")
print(motorcycles)

print("\nHere is the sorted list.")
print(sorted(motorcycles))

print("\nhere is the original list again:")
print(", ".join(motorcycles))

# Método reverse(), invierte el orden de la lista.si se aplica otra vez vuelve al original.
motorcycles.reverse()
print(motorcycles)

# Método len(), numero de datos.
print(len(motorcycles))

# Dividir una lista.
jugadores = ['charles', 'martina', 'michael', 'florence', 'eli']
print(jugadores[0:3])

# Omitir el principio o final del indice.
# Sin indice inicial,python empieza en 0.
print(jugadores[:4]) # del 0 al 3.

# Omitir al final.
print(jugadores[2:]) # del 3 al final.

# Acceder desde el final de la lista.
print(jugadores[-3:]) # imprime 3 ultimos nombres.

# Si se pone un tercer argumento seia saltos entre datos.
print(jugadores[0:4:2]) # uno si uno no.

# Bucles en listas.
# pasar por un trozo de la lista.
print("Estos son los tres primeros jugadores de mi equipo")
for jugador in jugadores[:3]:
    print(jugador.title())

# Copiar una lista.
# ([:]) esto dice a Python que haga un trozo yque empiece en el1er lugary termine en el último.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("my fevorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)


print(friend_foods)

print("Probando sincronización con GitHub")