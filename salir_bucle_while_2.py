# Dejar que el usuario elija cuándo salir.
prompt = "\nTell me someting, and I repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message  != 'quit':
        print(message)

# Bucle while con listas y diccionario.
# Confirmed_users.py
""" Empieza con usuarios que hay que verificar,
y una lista vacía para alojar a los usuarios confirmados."""

unconfirmed_users = ['alice', 'brian', 'candace']

confirmed_users = []
# Verifica cada usuario hasta que no quede ninguno sin confirmar.
# Mueve a cada usuario verificado a la lista de usuarios confirmados.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"verifing user: {current_user.capitalize()}")
    confirmed_users.append(current_user)
    print(confirmed_users)
 
# Muestra todos los usuarios confirmados.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.capitalize())



