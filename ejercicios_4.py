# Ejercicio 4-1. Pizzas.
pizzas = ['peperoni', 'carbonara', '4 quesos', 'suprema']

for pizza in pizzas:
    print(f"La pizza {pizza.title()}, me gusta mucho")
print("Me encanta la pizza!!!")

# Ejercicio 4-2. Animales.
animales = ['caballo', 'burro', 'camello']
for animal in animales:
    print(animal.title())

for animal in animales:
    if animal == 'caballo':
        print(f"El {animal}, es un animal majestuoso.")
    elif animal == 'burro':
        print(f"El {animal}, és un animal muy tozudo.")
    else:
        print(f"El {animal}, es muy resistente.")

for animal in animales:
    print(f"soy un {animal} y soy domesticable.")

# Función range(x, y) con parámetros cuenta , hay que poner +1 para 
# llegar al número requerido.
for value in range(1, 5): 
    print(value) # resultado 4, para 5 hay que poner 6 de argumento.

#range() con un tercer argumento.
for value in range(2, 11, 2):
    print(value)

cuadrados = []
for value in range(1, 11): 
    cuadrados.append(value ** 2)

print(cuadrados)
 
# Trabajar con listas de números, estadística sencilla.
digitos =[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digitos))
print(max(digitos))
print(sum(digitos))

# Listas de comprensión.
cuadrados = [value**2 for value in range(1, 11)]
print(cuadrados)

# Ejercicio 4.3, contar hasta veinte ambos inclusive
numeros = []

for value in range(1, 21):
    print(value)
    if value == 20:
        break

# Ejercicio 4.4, Un millón.
numeros = list(range(1, 1_000_001))
    
print(min(numeros))
print(max(numeros))

# Ejercicio 4.6- números impares.
for value in range(1, 21, 2):
    print(value)
    if value == 20:
        break
 # Ejercicio 4.6- contar de tres en tres.
lista = []

for value in range(0, 31, 3):
    print(value)
    if value == 30:
        break
# Ejercicio 4.7- los cubos hasta 10.
cubos = []

for value in range(1, 11):
    cubos.append(value ** 3)
    
print(cubos) 
   
#Ejercicio 4.9- comprensión de cubos.
cubos1 = [value ** 3 for value in range(1, 11)]
print(cubos1)

pizzas = ['peperoni', 'carbonara', '4 quesos', 'suprema']

# Ejercicio 4-10. Trozos.
print("Estos son los tres primeros elementos de la lista:")
print(pizzas[0:3])

print("Estos son los tres últimos elementos de la lista:")
print(pizzas[-3:])

print("estos son los tres elementos centrales:")
print(pizzas[1:4])

# Ejercicio 4-11. Mis pizzas, sus pizzas.
friend_pizzas= ['pizza', 'falafel', 'barbacue', 'cannoli', 'peperoni']
# añadir pizza a lista original
pizzas.append('margarita')
print(pizzas)
#Añadir pizza a lista de amigo.
friend_pizzas.append('carbonara')
print(friend_pizzas)
# Imprimir lista con bucle for.
print("Mis pizzas favoritas son:")

for pizza in pizzas:
    print(pizza)

# Imprimir lista de amigo con bucle for.
print("Las pizzas de la lista de mi amigo son:")

for friend_pizza in friend_pizzas:
    print(friend_pizza)

# Ejercicio 4.12- Más bucles.

my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream', 'hamburger']
friend_foods = ['peperoni', 'carbonara', '4 quesos', 'suprema', 'margarita']

print("estas son mis comidas preferidas")
for my_food in my_foods:
    print(my_food)
print("Estas son las comidas de mi colega")
for friend_food in friend_foods:
    print(friend_food)


         # Ejercicio 4-13 Bufet.
comidas = ('ensalada', 'patatas', 'berengenas', 'acelgas', 'pollo')
print("\nComidas del restaurant")
for comida in comidas:
    print(comida)
# Intento de cambiar tupla, no se puede
# acabado = 'patatas'
# comidas.remove(acabado)

print("\nSe han acabado las berengenas y la ensalada")
comidas =('entremeses','patatas', 'calabacines', 'acelgas', 'pollo')
for comida in comidas:
    print(comida)
    