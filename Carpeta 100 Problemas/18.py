print("Ingresa los coeficientes de la ecuacion cuadratica")

import cmath

a=int(input("Ingrese el coeficiente de a: "))
b=int(input("Ingrese el coeficiente de b: "))
c=int(input("Ingrese el coeficiente de c: "))


while a==0:
    print("Lo que estas ingresando no es una ecuación cuadratica")

if a!=0:
    d=cmath.sqrt(b**2 - 4*a*c)
    x1=(-b + d)/2**a
    x2=(-b + d)/2**a
    print(f"el resultado de la ecucacion en x1= ",x1," y en x2= ",x2)

















