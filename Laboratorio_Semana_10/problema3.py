def obtener_nombre(contacto):
    return contacto["nombre"].lower() 

n=int(input("Ingrese la cantidad de contactos que desea añadir: "))
x=1
agenda=[]
while x<=n: #ciclo para ingresar los datos
    print("------------------------------------------------------------------------------------------------------------------------") 
    contacto=input("Ingrese el nombre del contacto: ")
    numero=int(input("Ingrese el numero del contacto: "))
    correo=input("Ingrese el correo del contacto: ")
    print("------------------------------------------------------------------------------------------------------------------------")
    dic_agenda={
        "Contacto: ": contacto,
        "Núemero: ": numero,
        "Correo: ": correo,
    }
    agenda.append(dic_agenda)
    x=x+1

agenda_ordenada = sorted(agenda, key=obtener_nombre)


latupla = tuple(agenda_ordenada)

agenda_ordenada = sorted(agenda, key=obtener_nombre)

# Convertir la lista ordenada en una tupla
latupla = tuple(agenda_ordenada)

print("." * 120)
print("Agenda ordenada alfabéticamente:")
for contacto in latupla:
    print(contacto)
print("." * 120)

ñ=input("Contacto que desea buscar: ")

resultado = next((persona for persona in latupla if persona["nombre"] == ñ), None)
if ñ in latupla:
    print("______________________________________________________________________________________________________________")
    print("¡Encontrado!",resultado)
    print("______________________________________________________________________________________________________________")
else:
    print("______________________________________________________________________________________________________________")
    print("No encontrado")
    print("______________________________________________________________________________________________________________") 