def suma_serie_aritmetica(a, d, n):
    return (n / 2) * (2 * a + (n - 1) * d)

def suma_serie_geometrica(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)

def suma_serie_ingresada():
    numeros = list(map(int, input("Ingrese la serie separada por espacios: ").split()))
    return sum(numeros)

while True:
    print("\nMenú de opciones:")
    print("1. Suma de una serie aritmética")
    print("2. Suma de una serie geométrica")
    print("3. Suma de una serie ingresada manualmente")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        a = int(input("Ingrese el primer término: "))
        d = int(input("Ingrese la diferencia común: "))
        n = int(input("Ingrese el número de términos: "))
        print("Suma de la serie aritmética:", suma_serie_aritmetica(a, d, n))
    
    elif opcion == "2":
        a = int(input("Ingrese el primer término: "))
        r = int(input("Ingrese la razón común: "))
        n = int(input("Ingrese el número de términos: "))
        print("Suma de la serie geométrica:", suma_serie_geometrica(a, r, n))
    
    elif opcion == "3":
        print("Suma de la serie ingresada:", suma_serie_ingresada())

    elif opcion == "4":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida, intente de nuevo.")
