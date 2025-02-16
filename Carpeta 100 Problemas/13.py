def convertir_temperatura(valor, origen, destino):
    if origen == "C":
        if destino == "F":
            return valor * 9/5 + 32  # Celsius a Fahrenheit
        elif destino == "K":
            return valor + 273.15  # Celsius a Kelvin

    elif origen == "F":
        if destino == "C":
            return (valor - 32) * 5/9  # Fahrenheit a Celsius
        elif destino == "K":
            return (valor - 32) * 5/9 + 273.15  # Fahrenheit a Kelvin

    elif origen == "K":
        if destino == "C":
            return valor - 273.15  # Kelvin a Celsius
        elif destino == "F":
            return (valor - 273.15) * 9/5 + 32  # Kelvin a Fahrenheit

    return "Conversión no válida"

valor = float(input("Ingresa la temperatura: "))
origen = input("Ingresa la escala original (C, F, K): ").upper()
destino = input("Ingresa la escala a convertir (C, F, K): ").upper()

resultado = convertir_temperatura(valor, origen, destino)
print(f"Temperatura convertida: {resultado} {destino}")

