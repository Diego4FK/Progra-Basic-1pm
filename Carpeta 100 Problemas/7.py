x=int(input("Ingresa el numero que quieres saber si es par o impar: "))
v=int(input("Ingresa el numero que quieres saber si es multiplo del numero anterior: "))


if x%2==0:
    print("El numero es par")
if x%2>0:
    print("El numero es impar")

if v%x==0 :
    print("Si es multiplo")

if v%x!=0 :
    print("No es multiplo ")







