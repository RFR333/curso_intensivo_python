# Definir una función.
# greeter.py
# Pasar información a una función.
def greet_user(username):
    """Muestra un simple saludo."""
    print(f"hello, {username.capitalize()}")

greet_user('jesse')

# Argumentos posicionales.
# pets.py
def describe_pet(animal_type, pet_name):
    """Muestra información sobre una mascota"""
    print(f"I have a {animal_type.capitalize()}.")
    print(f"My {animal_type.capitalize()}'s name is {pet_name.capitalize()}")

describe_pet('hamster', 'harry')

mascotas = []
while True:
    print("\nIntroduce los datos de una mascota (o escribe 'salir' para terminar):")

    animal = input("Tipo de animal: ")
    if animal.lower() == "salir":
        break

    nombre = input("Nombre de la mascota: ")
    if nombre.lower() == "salir":
        break
    mascotas.append((animal, nombre))

    describe_pet(animal, nombre)

# 🐾 Resumen final
print("\nResumen de mascotas añadidas:")
for animal, nombre in mascotas:
    print(f"- {animal.capitalize()}: {nombre.capitalize()}")





