def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]  

# Ejemplo de uso
texto = input("Ingresa una palabra o frase: ")
if es_palindromo(texto):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
