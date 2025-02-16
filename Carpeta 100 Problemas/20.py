def busqueda_lineal(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i  
    return -1  

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio  
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  


lista = [10, 20, 30, 40, 50]

print("\nBúsqueda Lineal:")
print("Índice del 30:", busqueda_lineal(lista, 30))  


lista_ordenada = sorted(lista)
print("\nBúsqueda Binaria:")
print("Índice del 30:", busqueda_binaria(lista_ordenada, 30)) 
