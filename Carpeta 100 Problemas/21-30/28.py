class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f"{self.titular}, has depositado ${monto}. Saldo actual: ${self.saldo}.")

    def retirar(self, monto):
        self.saldo -= monto
        print(f"{self.titular}, has retirado ${monto}. Saldo actual: ${self.saldo}.")

    def mostrar_saldo(self):
        print(f"{self.titular}, tu saldo actual es: ${self.saldo}")

def crear_cuenta():
    nombre = input("Ingrese el nombre del titular de la cuenta: ")
    saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
    cuenta = CuentaBancaria(nombre, saldo_inicial)
    return cuenta

def menu():
    cuenta = crear_cuenta()
    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            cuenta.mostrar_saldo()
        elif opcion == "2":
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == "3":
            monto = float(input("Ingrese el monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == "4":
            print("Gracias por usar el programa de cuenta bancaria.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

menu()
