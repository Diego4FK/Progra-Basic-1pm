def ingresar_datos():
    datos = []
    print("Ingresa tus datos (escribe 'fin' para terminar):")
    while True:
        entrada = input("Dato: ")
        if entrada.lower() == 'fin':
            break
        try:
            dato = float(entrada)
            datos.append(dato)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return datos

def calcular_estadisticas(datos):
    if not datos:
        print("No hay datos para analizar.")
        return

    # Calcular estadísticas
    media = sum(datos) / len(datos)
    datos_ordenados = sorted(datos)
    n = len(datos)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]

    frecuencia = {}
    for valor in datos:
        if valor in frecuencia:
            frecuencia[valor] += 1
        else:
            frecuencia[valor] = 1
    moda = max(frecuencia, key=frecuencia.get)

    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")

# Ejemplo de uso
datos = ingresar_datos()
calcular_estadisticas(datos)
