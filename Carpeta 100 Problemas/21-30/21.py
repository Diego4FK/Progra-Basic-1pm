import math

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_esfera(radio):
    return (4/3) * math.pi * radio ** 3

def area_rectangulo(base, altura):
    return base * altura

def volumen_prisma_rectangular(base, altura, profundidad):
    return base * altura * profundidad

def area_triangulo(base, altura):
    return (base * altura) / 2

def volumen_piramide(base, altura):
    return (base * altura) / 3

def main():
    print("Seleccione una figura geométrica:")
    print("1. Círculo (Área)")
    print("2. Esfera (Volumen)")
    print("3. Rectángulo (Área)")
    print("4. Prisma Rectangular (Volumen)")
    print("5. Triángulo (Área)")
    print("6. Pirámide (Volumen)")
    
    opcion = int(input("Ingrese el número de la opción: "))
    
    if opcion == 1:
        radio = float(input("Ingrese el radio del círculo: "))
        print(f"El área del círculo es: {area_circulo(radio):.2f}")
    elif opcion == 2:
        radio = float(input("Ingrese el radio de la esfera: "))
        print(f"El volumen de la esfera es: {volumen_esfera(radio):.2f}")
    elif opcion == 3:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        print(f"El área del rectángulo es: {area_rectangulo(base, altura):.2f}")
    elif opcion == 4:
        base = float(input("Ingrese la base del prisma: "))
        altura = float(input("Ingrese la altura del prisma: "))
        profundidad = float(input("Ingrese la profundidad del prisma: "))
        print(f"El volumen del prisma es: {volumen_prisma_rectangular(base, altura, profundidad):.2f}")
    elif opcion == 5:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print(f"El área del triángulo es: {area_triangulo(base, altura):.2f}")
    elif opcion == 6:
        base = float(input("Ingrese el área de la base de la pirámide: "))
        altura = float(input("Ingrese la altura de la pirámide: "))
        print(f"El volumen de la pirámide es: {volumen_piramide(base, altura):.2f}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

