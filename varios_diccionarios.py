# Aliens.py
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Lista vacia para guardar aliens.
aliens = []

# Crear 30 aliens verdes.
for alien_number in range(30):
    new_alien ={'color': 'green', 'points': 5, 'speed': 'slow',}
    aliens.append(new_alien)
    # mostrar primeros 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("Aliens creados")

# muestra cuantos aliens se han creado.
print(f"Total number of aliens: {len(aliens)}")

for alien in aliens [:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[3:6]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
        
# Muestra los 5 primeros aliens.
for alien in aliens[:5]:
    print(alien)

# Lista en diccionario.
# Pizza.py.
# Guarda la informacion de una pizzaa que se esta pidiendo.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Resume el pedido.
print(f"You ordered a {pizza['crust']} - crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t" + topping)


# Favorite_language.py.
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# Diccionario en diccionario.
# many_uders.py
users = {
    'aenstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',   
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")







