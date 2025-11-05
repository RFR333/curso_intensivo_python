# ejercicio 3.1.
nombres = ['antonio', 'maribel', 'pedro', 'pilar', 'miguel', 'rafael']
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])
print(nombres[4])
print(nombres[5])

# Ejercicio 3.2.
message = "Hola! cómo estas"
print(f"{message} {nombres[0].title()}?")
print(f"{message} {nombres[1].title()}?")
print(f"{message} {nombres[2].title()}?")
print(f"{message} {nombres[3].title()}?")
print(f"{message} {nombres[4].title()}?")
print(f"{message} {nombres[5].title()}?")

print(f"{message} {nombres[-1].title()}") # Acceder al último elemento.

# Ejercicio 3.3. Mi propia lista.
mi_lista = ['moto', 'coche', 'avion', 'barco', 'bicicleta']
message = "Me gustaria tener un/a"
print(f"{message} {mi_lista[0]} y viajar.")
print(f"{message} {mi_lista[1]} y viajar.")
print(f"{message} {mi_lista[2]} y viajar.")
print(f"{message} {mi_lista[3]} y viajar.")
print(f"{message} {mi_lista[4]} y viajar.")

# Ejercicio 3.4 lista de invitados.
personas_especiales = ['Pilar', 'victoria', 'miriam']

print(f"¿{personas_especiales[0]} Te gustaria cenar conmigo?")
print(f"¿{personas_especiales[1]} Te gustaria cenar conmigo?")
print(f"¿{personas_especiales[2]} Te gustaria cenar conmigo?")

# Ejercicio 3.5 Cambiar lista de invitados.
personas_especiales.remove('miriam')
personas_especiales.append('ricard')
print(", ".join(personas_especiales))

print(f"¿{personas_especiales[0]} Te gustaria cenar conmigo?")
print(f"¿{personas_especiales[1]} Te gustaria cenar conmigo?")
print(f"¿{personas_especiales[2]} Te gustaria cenar conmigo?")

# Ejercicio 3.6 Más invitados.
personas_especiales.insert(0, 'antonio')
personas_especiales.insert(2, 'pedro')
personas_especiales.append('mariano')

print(", ".join(personas_especiales))

print(f"¿{personas_especiales[0]} te gustaría cenar conmigo?")
print(f"¿{personas_especiales[1]} te gustaría cenar conmigo?")
print(f"¿{personas_especiales[2]} te gustaría cenar conmigo?")
print(f"¿{personas_especiales[3]} te gustaría cenar conmigo?")
print(f"¿{personas_especiales[4]} te gustaría cenar conmigo?")
print(f"¿{personas_especiales[5]} te gustaría cenar conmigo?")

# Ejercicio 3.7 Reducir la lista.
print(f"{personas_especiales[0]} me han cancelado la reserva... tendré que reducir invitados. ")
print(f"{personas_especiales[1]} me han cancelado la reserva... tendré que reducir invitados.")
print(f"{personas_especiales[2]} me han cancelado la reserva... tendré que reducir invitados.")
print(f"{personas_especiales[3]} me han cancelado la reserva... tendré que reducir invitados.")
print(f"{personas_especiales[4]} me han cancelado la reserva... tendré que reducir invitados.")
print(f"{personas_especiales[5]} me han cancelado la reserva... tendré que reducir invitados.")

message = "tienes cancelada la cena con Rafa"
print(f"{personas_especiales[0]} {message} el viernes")
print(f" {personas_especiales[2]} {message} el viernes")
print(f" {personas_especiales[4]} {message} el viernes")
print(f" {personas_especiales[5]} {message} el viernes")
print(", ".join(personas_especiales))

personas_especiales.pop(0)
personas_especiales.pop(1)
personas_especiales.pop(2)
personas_especiales.pop(2)

print(", ".join(personas_especiales))

# Ejercicio 3.8-Ver el mundo.
viajes = ['brasil', 'australia', 'italia', 'marruecos', 'india']
print(sorted(viajes))
print(", ".join(viajes))
viajes.reverse()
print(", ".join(viajes))
viajes.sort()
print(", ".join(viajes))
viajes.sort(reverse=True)
print(", ".join(viajes))
len(viajes)

# Ejercicio 3.9- Invitados a cenar.
print(f"\nEl número de invitados es: {len(personas_especiales)} invitados.")

# Ejercicio 3.10- Todas las funciones.
rios = ['amazonas', 'nilo', 'eúfrates', 'ebro', 'missisipi', 'segura']

rios.append('tigris')
print(", ".join(rios))

rios.pop()
print(", ".join(rios))

rios.pop(2)
print(", ".join(rios))

rios.append('tigris')
rios.insert(0, 'eúfrates')
print(", ".join(rios))

del rios[-1]
rios.sort()
guardar_rio = 'eúfrates' # envolvemos en variable para reutilizar.
rios.remove(guardar_rio)
print(", ".join(rios))
print(guardar_rio)




