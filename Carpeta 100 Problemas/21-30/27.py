def convertir_longitud(valor, unidad_origen, unidad_destino):
    factores = {
        "m": 1, "km": 0.001, "cm": 100, "mm": 1000,
        "in": 39.3701, "ft": 3.28084, "yd": 1.09361, "mi": 0.000621371 }
    if unidad_origen in factores and unidad_destino in factores:
        return valor * (factores[unidad_destino] / factores[unidad_origen])
    return None

def convertir_masa(valor, unidad_origen, unidad_destino):
    factores = {
        "kg": 1, "g": 1000, "mg": 1000000,
        "lb": 2.20462, "oz": 35.274
    }
    if unidad_origen in factores and unidad_destino in factores:
        return valor * (factores[unidad_destino] / factores[unidad_origen])
    return None

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "C" and unidad_destino == "F":
        return valor * 9/5 + 32
    elif unidad_origen == "F" and unidad_destino == "C":
        return (valor - 32) * 5/9
    elif unidad_origen == "C" and unidad_destino == "K":
        return valor + 273.15
    elif unidad_origen == "K" and unidad_destino == "C":
        return valor - 273.15
    elif unidad_origen == "F" and unidad_destino == "K":
        return (valor - 32) * 5/9 + 273.15
    elif unidad_origen == "K" and unidad_destino == "F":
        return (valor - 273.15) * 9/5 + 32
    return None

while True:
    print("\n CONVERSOR DE UNIDADES ")
    print("1. Convertir longitud (m, km, cm, mm, in, ft, yd, mi)")
    print("2. Convertir masa (kg, g, mg, lb, oz)")
    print("3. Convertir temperatura (C, F, K)")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion in ["1", "2", "3"]:
        valor = float(input("Ingrese el valor a convertir: "))
        unidad_origen = input("Ingrese la unidad de origen: ").strip().lower()
        unidad_destino = input("Ingrese la unidad de destino: ").strip().lower()

        if opcion == "1":
            resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
        elif opcion == "2":
            resultado = convertir_masa(valor, unidad_origen, unidad_destino)
        elif opcion == "3":
            resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)

        if resultado is not None:
            print(f"\n Resultado: {valor} {unidad_origen} = {resultado:.4f} {unidad_destino}\n")
        else:
            print("\n Unidades no válidas, intente de nuevo.\n")

    elif opcion == "4":
        print("Saliendo del conversor...")
        break
    else:
        print("\n Opción no válida, intente de nuevo.\n")
