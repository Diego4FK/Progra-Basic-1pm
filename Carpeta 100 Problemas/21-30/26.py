agenda = {}

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    correo = input("Ingrese el correo electrónico: ")
    
    agenda[nombre] = {"Teléfono": telefono, "Correo": correo}
    print(f"Contacto '{nombre}' agregado exitosamente.\n")

def buscar_contacto():
    nombre = input("Ingrese el nombre a buscar: ")
    if nombre in agenda:
        print(f"\nNombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['Teléfono']}")
        print(f"Correo: {agenda[nombre]['Correo']}\n")
    else:
        print(f"\nEl contacto '{nombre}' no existe en la agenda.\n")

def listar_contactos():
    if not agenda:
        print("\nLa agenda está vacía.\n")
    else:
        print("\nLista de contactos:")
        for nombre, info in agenda.items():
            print(f"{nombre} - {info['Teléfono']} - {info['Correo']}")
        print()

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"\nEl contacto '{nombre}' ha sido eliminado.\n")
    else:
        print(f"\nEl contacto '{nombre}' no existe en la agenda.\n")

# Menú 
while True:
    print("\n📒 AGENDA DE CONTACTOS 📒")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Listar contactos")
    print("4. Eliminar contacto")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        listar_contactos()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("Saliendo de la agenda...")
        break
    else:
        print("Opción inválida, intente nuevamente.\n")
