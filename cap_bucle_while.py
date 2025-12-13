# Función IMPUT().
# parrot.py.
message = input("Tell me something, and I will repeat it back you: ")
print(message)

# greeter.py.
name = input("Please enter your name: ")
print(f"\nHello, {name}")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your nickname name? "

name = input(prompt)
print(f"\nHello, {name}")

# Función int(). integer, número entero.
age = input("How old are you? ")
age = int(age)
age >= 18
print(f"Tu edad es: {age} años. ")

height = input("How tall are you, in cm? ")
height = float(height)

if height >= 48:
    print("\nYou're tall enough ride!")
else:
    print("\nYou'll be able to ride when you're a little older,.")

# Operador módulo, (%): divide un número entre otro y devolver resto.

# Par o impar.
number = input("Introduce un número, y te diré si es par o impar.")
number = int(number)

if number % 2 == 0:
    print(f"El número: {number}, es PAR.")
else:
    print(f"El número: {number}, es impar")


# El bucle While en acción
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# se ejecuta mientras se cumpla la condición,si current_number es menor o igual que 5 sigue.





