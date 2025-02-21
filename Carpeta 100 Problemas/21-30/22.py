import random

def lanzar_dado():
    return random.randint(1, 6)

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

def main():
    print("Seleccione una opción:")
    print("1. Lanzar un dado")
    print("2. Lanzar una moneda")
    
    opcion = int(input("Ingrese el número de la opción: "))
    
    if opcion == 1:
        print(f"El resultado del dado es: {lanzar_dado()}")
    elif opcion == 2:
        print(f"El resultado de la moneda es: {lanzar_moneda()}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
