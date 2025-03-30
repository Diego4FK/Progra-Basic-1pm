def convert_units(value, conversion_type): #Se define una funcion para realizar calculos simples de conversion
    conversions = {
        "km_to_miles": lambda x: x * 0.621371,
        "miles_to_km": lambda x: x / 0.621371,
        "celsius_to_fahrenheit": lambda x: (x * 9/5) + 32,
        "fahrenheit_to_celsius": lambda x: (x - 32) * 5/9,
        "gallons_to_liters": lambda x: x * 3.78541,
        "liters_to_gallons": lambda x: x / 3.78541
    }
    
    if conversion_type in conversions:
        return conversions[conversion_type](value)
    else:
        return "Tipo de conversión no válido"

def km_ml(z, value):
    if z == 1:
        return convert_units(value, "km_to_miles")
    elif z == 2:
        return convert_units(value, "miles_to_km")
    else:
        return "Opción no válida"

x=0
while x>3 or x<=0: #Ingresamos los datos dentro del ciclo
 print("-"*120)
 print("Datos que puede ingresar para la conversion:")
 print("1.Distancia")
 print("2.Temperatura")
 print("3.Cantidad")
 print("-"*120)
 x=int(input("Dato que desea convertir: "))

 if x > 3 or x <= 0:
        print("La opción que ingresó no es válida :V") 
 else:
        if x == 1:
            print("1. De kilómetros a millas") #Para los 3 casos se utiliza un if para controlar que opcion se puede seleccionar
            print("2. De millas a kilómetros")
            z = int(input("De qué unidad a qué unidad desea convertir: "))
            if z != 1 and z != 2:
                print("La opción que ingresó no es válida")
            else:
                value = float(input("Ingrese el valor a convertir: "))
                print("Resultado:", km_ml(z, value))

        elif x == 2:
            print("1. De Celsius a Fahrenheit")
            print("2. De Fahrenheit a Celsius")
            z = int(input("De qué unidad a qué unidad desea convertir: "))
            if z != 1 and z != 2:
                print("La opción que ingresó no es válida")
            else:
                conversion_type = "celsius_to_fahrenheit" if z == 1 else "fahrenheit_to_celsius"
                value = float(input("Ingrese el valor a convertir: "))
                print("Resultado:", convert_units(value, conversion_type)) #Se imprime la conversion

        elif x == 3:
            print("1. De galones a litros")
            print("2. De litros a galones")
            z = int(input("De qué unidad a qué unidad desea convertir: "))
            if z != 1 and z != 2:
                print("La opción que ingresó no es válida")
            else:
                conversion_type = "gallons_to_liters" if z == 1 else "liters_to_gallons"
                value = float(input("Ingrese el valor a convertir: "))
                print("Resultado:", convert_units(value, conversion_type))