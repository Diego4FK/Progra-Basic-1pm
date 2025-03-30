#Uso de estructuras de control
numeros = list(map(int, input("Ingrese números separados por espacios: ").split()))
print("Lista original:", numeros)

#Uso de funciones bien definidas
def ordenar_lista(lista):
    """Ordena una lista de números de menor a mayor."""
    return sorted(lista)

numeros_ordenados = ordenar_lista(numeros)
print("Lista ordenada:", numeros_ordenados)

class Persona:
    """Clase que representa una persona."""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        """Muestra la información de la persona."""
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

#Ingreso de datos por parte del usuario
nombre = input("Ingrese el nombre de la persona: ")
edad = int(input("Ingrese la edad de la persona: "))

#Crear una instancia de la clase Persona
persona = Persona(nombre, edad)
persona.mostrar_info()
