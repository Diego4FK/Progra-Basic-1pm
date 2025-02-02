def interes_compuesto(capital, tasa, tiempo):
    monto = capital * (1 + tasa) ** tiempo
    return monto

capital = float(input("Ingresa el capital inicial: "))
tasa = float(input("Ingresa la tasa de interés (en porcentaje): ")) / 100
tiempo = float(input("Ingresa el tiempo: "))

monto_final = interes_compuesto(capital, tasa, tiempo)
print(f"\nEl monto final después de {tiempo} periodos será: {monto_final:.2f}")
