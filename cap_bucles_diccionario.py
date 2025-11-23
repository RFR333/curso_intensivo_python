# Pasar bucle por diccionario.
user_0 = {
    'user_name': 'efermi',
    'first': 'enrico',
    'last': 'fermi',

}

for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}")


favorite_lenguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, languages in favorite_lenguages.items():
    print(f"{name.title()}'s favorite lenguage is {languages.title()}.")


# Acceder a las claves del diccionario.

for name in favorite_lenguages.keys():
    print(name.title())



for name in favorite_lenguages:
    print(name.title())


