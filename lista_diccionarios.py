# Pasar bucle por todas claves del diccionario
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

friends =['phil', 'sarah']

for key in favorite_languages.keys():
    print(f"Hi {key.title()}")
    
    if key in friends:
        language = favorite_languages[key].title()
        print(f"\t{key.title()},I see you love {language}!") 
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll")


# Pasar bucle por las claves en orden particular.
for key in sorted(favorite_languages.keys()):
    print(f"{key.title()}, thank you for taking the poll.")

# Pasar bucle por todos los valores de un diccionario, método values().
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Uso de set(): "conjunto", para que no se repitan las salidas.
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
