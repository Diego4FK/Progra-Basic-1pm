def generar_histograma(datos, num_bins):
    minimo, maximo = min(datos), max(datos)
    rango = (maximo - minimo) / num_bins  

    bins = [minimo + i * rango for i in range(num_bins + 1)]
    frecuencia = [0] * num_bins

    for dato in datos:
        for i in range(num_bins):
            if bins[i] <= dato < bins[i + 1]:
                frecuencia[i] += 1
                break
    frecuencia[-1] += datos.count(maximo)

    for i in range(num_bins):
        print(f"{bins[i]:.1f} - {bins[i+1]:.1f}: {'#' * frecuencia[i]} ({frecuencia[i]})")

datos = [12, 15, 14, 10, 10, 9, 8, 15, 14, 13, 15, 17, 18, 19, 10, 9, 8, 7, 6, 5]

generar_histograma(datos, num_bins=5)
