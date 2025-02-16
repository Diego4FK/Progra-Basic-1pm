def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    contador_vocales = 0
    contador_consonantes = 0

    for caracter in cadena:
        if caracter in vocales:
            contador_vocales += 1
        elif caracter in consonantes:
            contador_consonantes += 1

    return contador_vocales, contador_consonantes

# Pedir al usuario una cadena
texto = input("Ingresa una cadena: ")

# Contar vocales y consonantes
vocales, consonantes = contar_vocales_consonantes(texto)

# Mostrar resultados
print(f"Número de vocales: {vocales}")
print(f"Número de consonantes: {consonantes}")
