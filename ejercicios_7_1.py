# Ejercicio 7-8.Bocateria

pedidos_bocadillos = ['lomo','pastrami', 'tortilla', 'pechuga pollo','pastrami', 'jamón', 'jamón dulce', 'pastrami']

pedidos_terminados = []

iniciar_pedido = True
while pedidos_bocadillos:
    pedidos = pedidos_bocadillos.pop()

    print(f"Haciendo bocadillo: \t-{pedidos.capitalize()}")
    pedidos_terminados.append(pedidos)
# muestra todos los pedidos terminados.
print("Los bocadillos acabados son:\n")
for pedido_terminado in pedidos_terminados:
    print(f"\tBocadillo de: \t-{pedido_terminado.capitalize()}")

# Ejecicio 7-9. Ya no hay pastrami:
pedidos_bocadillos = ['lomo','pastrami', 'tortilla', 'pechuga pollo','pastrami', 'jamón',
                       'jamón dulce', 'pastrami']

print("\nEl pastrami se ha agotado, lo sentimos.")
while 'pastrami' in pedidos_bocadillos:
    pedidos_bocadillos.remove('pastrami')
print("\nLos pedidos disponibles son:")
for pedido_bocadillo in pedidos_bocadillos:
    print(f"\t-{pedido_bocadillo.capitalize()}")


# Ejercicio 7-10. Vacaciones de ensueño.
# Diccionario para guardar las respuestas.
respuestas = {}

# Bandera para iniciar bucle.
encuesta_activa = True

while encuesta_activa:
    
    nombre = input("\nEscribe tu nombre.")
    lugar = input("\nSi pudieses visitar cualquier lugar del mundo")

    # Guardamos la respuesta en  el diccionario.
    respuestas[nombre] = lugar

    #. Preguntamos si otra persona quiere hacer la encuesta.
    repetir = input("\nQuieres que otra persona responda? (si/no)")

    if repetir.lower() == 'no':
        encuesta_activa = False

# mostrar resultados de la encuesta.
print("\n---Resultados de la encuesta")
for nombre, lugar in respuestas.items():
    print(f"A {nombre.capitalize()} le gustaria ir a {lugar.capitalize()}")


