def ingresar_matriz(filas, columnas):
    print(f"Ingrese los valores de una matriz de {filas}x{columnas}:")
    matriz = []
    for i in range(filas):
        fila = list(map(int, input(f"Fila {i+1}: ").split()))
        while len(fila) != columnas:
            print("Error: Ingrese la cantidad correcta de elementos.")
            fila = list(map(int, input(f"Fila {i+1}: ").split()))
        matriz.append(fila)
    return matriz

def sumar_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiplicar_matrices(A, B):
    filas_A, columnas_A = len(A), len(A[0])
    filas_B, columnas_B = len(B), len(B[0])

    if columnas_A != filas_B:
        print("No se pueden multiplicar las matrices, dimensiones inválidas.")
        return None

    C = [[sum(A[i][k] * B[k][j] for k in range(columnas_A)) for j in range(columnas_B)] for i in range(filas_A)]
    return C

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

print("Matriz A:")
A = ingresar_matriz(filas, columnas)

print("Matriz B:")
B = ingresar_matriz(filas, columnas)

print("\nSuma de matrices:")
for fila in sumar_matrices(A, B):
    print(fila)

print("\nMultiplicación de matrices:")
resultado = multiplicar_matrices(A, B)
if resultado:
    for fila in resultado:
        print(fila)
