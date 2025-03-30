class Vehiculo: #Definimos la clase
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Precio: ${self.precio}"

class Automovil(Vehiculo): #Subclase del vehiculo donde se define sus elementos
    def __init__(self, marca, modelo, año, precio, num_puertas):
        super().__init__(marca, modelo, año, precio)
        self.num_puertas = num_puertas

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Puertas: {self.num_puertas}"

class Motocicleta(Vehiculo): #Segunda subclase del vehiculo donde se define los elementos de la moto
    def __init__(self, marca, modelo, año, precio, cilindrada):
        super().__init__(marca, modelo, año, precio)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Cilindrada: {self.cilindrada}cc"

def registrar_vehiculo(): #Definimos una funcion para el ingreso de los datos del vehiculo que el usuario desea ingresar
    print("Seleccione el tipo de vehículo:")
    print("1. Automóvil")
    print("2. Motocicleta")
    tipo = int(input("Ingrese una opción: "))
    
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = int(input("Año: "))
    precio = float(input("Precio: "))
    
    if tipo == 1:
        num_puertas = int(input("Número de puertas: "))
        vehiculo = Automovil(marca, modelo, año, precio, num_puertas)
    elif tipo == 2:
        cilindrada = int(input("Cilindrada (cc): "))
        vehiculo = Motocicleta(marca, modelo, año, precio, cilindrada)
    else:
        print("Opción no válida.")
        return None
    
    return vehiculo
#se imprime los datos registrados
vehiculo_registrado = registrar_vehiculo()
if vehiculo_registrado:
    print("Vehículo registrado con éxito:")
    print(vehiculo_registrado.mostrar_informacion())
