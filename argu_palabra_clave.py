# Argumentos de palabra clave.

def describe_pet(animal_type, pet_name):
    """Muestra información sobre una mascota."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}")

describe_pet(animal_type= 'hamster', pet_name='harry')

# Con argumentos de palabra clave, el orden no importa porque cada valor
# se asigna explícitamente a su parámetro. 
# Valores predeterminados (default values):
# Si no se proporciona un argumento, Python usa el valor que está definido por defecto.

# Solo pasamos pet_name. animal_type tomará el valor predeterminado ('dog').
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.capitalize()}")
describe_pet(pet_name='willie')

# Con dos valores en argumento.
describe_pet(pet_name='willie', animal_type='dog')


