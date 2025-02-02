def generar_pares_impares(limite):
    pares = []
    impares = list()
    
    for num in range(1, limite + 1):
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    return pares, impares


limite = int(input("Ingresa el límite: "))
pares, impares = generar_pares_impares(limite)

print(pares, "|", impares)

