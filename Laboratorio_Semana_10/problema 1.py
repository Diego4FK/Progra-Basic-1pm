txt=input("Ingrese el texto: ")
palabras=txt.lower().split()
unitwords=set(txt.lower().split())
contador={}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1  #la iniciamos en 1
    else:
        contador[palabra] = 1   #sumamos 1

masrepetida=max(contador, key=contador.get) #Se checa cual es la mas repetida
frecmax=contador[palabra] #Se checa cual es su cantidad de repeticiones

print("Frecuencia de palabras:", contador)
print("Palabras unicas:", unitwords)
print(f"La palabra mas frecuente es: -", masrepetida,"-, y su cantidad de repeticiones es:", frecmax)