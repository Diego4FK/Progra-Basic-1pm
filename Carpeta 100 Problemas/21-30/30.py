def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def ingresar_lista():
    lista = []
    print("Ingresa los números en la lista (escribe 'fin' para terminar):")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            lista.append(numero)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return lista

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Calcular factorial")
        print("2. Calcular n-ésimo término de la secuencia de Fibonacci")
        print("3. Sumar una lista de números")
        print("4. Calcular la potencia de un número")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            try:
                n = int(input("Ingresa un número entero: "))
                print(f"Factorial de {n}: {factorial(n)}")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
        elif opcion == "2":
            try:
                n = int(input("Ingresa un número entero: "))
                print(f"Fibonacci de {n}: {fibonacci(n)}")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
        elif opcion == "3":
            lista = ingresar_lista()
            print(f"Suma de la lista: {suma_lista(lista)}")
        elif opcion == "4":
            try:
                base = float(input("Ingresa la base: "))
                exponente = int(input("Ingresa el exponente: "))
                print(f"{base} elevado a la potencia de {exponente}: {potencia(base, exponente)}")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == "5":
            print("Gracias por usar el programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

menu()
