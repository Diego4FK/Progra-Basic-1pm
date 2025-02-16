import random

def generar_numeros_aleatorios(n, distribucion="uniforme"):
    if distribucion == "uniforme":
        return [random.uniform(0, 100) for _ in range(n)]
    elif distribucion == "normal":
        return [random.gauss(50, 15) for _ in range(n)]  # media=50, desviación=15
    elif distribucion == "exponencial":
        return [random.expovariate(1/30) for _ in range(n)]  # lambda = 1/30
    else:
        raise ValueError("Distribución no soportada")

# Pruebas
print("Números aleatorios con distribución uniforme:", generar_numeros_aleatorios(10, "uniforme"))
print("Números aleatorios con distribución normal:", generar_numeros_aleatorios(10, "normal"))
print("Números aleatorios con distribución exponencial:", generar_numeros_aleatorios(10, "exponencial"))
