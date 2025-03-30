def calculadora(*Lista):
    return Lista["Datos: "]

def calcular_media(Lista):
    return sum(Lista) / len(Lista)   #calcula la media

def calcular_moda(Lista):  #calcula la moda
    frecuencias = {}
    for num in Lista:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1
    max_frecuencia = max(frecuencias.values())
    moda = [key for key, value in frecuencias.items() if value == max_frecuencia]
    return moda

def calcular_mediana(Lista):     
    Lista_ordenada = sorted(Lista)  # Ordena la lista
    n = len(Lista)
    mitad = n // 2

    if n % 2 == 0:  
        return (Lista_ordenada[mitad - 1] + Lista_ordenada[mitad]) / 2
    else:  
        return Lista_ordenada[mitad]

n=int(input("Cuantos numeros desea añadir: "))
c=1
Lista=[]

for _ in range(n):
    print("-"*120)
    numero=int(input("Ingrese el numero: "))
    print("-"*120)

    Lista.append(numero)

suma = lambda *Lista: sum(Lista)

print("-"*120)
print("Lista de numeros ingresados: ",Lista)
print("Media de los datos ingresados: ",calcular_media(Lista)) 
print("Moda de los datos ingresados: ",calcular_moda(Lista))
print("La mediana de los datos ingresados: ",calcular_mediana(Lista))
print("-"*120)