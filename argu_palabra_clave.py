
# Con argumentos de palabra clave, el orden no importa porque cada valor
# se asigna explícitamente a su parámetro. 
# Valores predeterminados (default values):
# Si no se proporciona un argumento, Python usa el valor que está definido por defecto.

# Solo pasamos pet_name. animal_type tomará el valor predeterminado ('dog').
def describe_pet(pet_name, animal_type='dog'):
    if pet_name == 'willie 1':
        print('1º')
    else:
        print('2º')
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.capitalize()}")
describe_pet(pet_name='willie 1')
# Con dos valores en argumento.
describe_pet(pet_name='willie 2', animal_type='dog')
print("-" * 40)

# Argumentos de palabra clave.
def describe_pet(animal_type, pet_name):
    """Muestra información sobre una mascota."""
    print(f"3º\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}")

describe_pet(animal_type= 'hamster', pet_name='harry')

print("-" * 40)

# Valores de retorno.
# Devolver solo un valor:
# formated_name.py
def get_formated_name(first_name, last_name):
    """Devuelve un nombre completo, con formato adecuado"""
    full_name = f"4º\n{first_name} {last_name}"
    return full_name.title()

musician = get_formated_name('jimi', 'hendrix')
print(musician)

print("-" * 40)


