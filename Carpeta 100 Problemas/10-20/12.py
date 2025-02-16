print("Ingresa 3 numeros para analizar")

a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el tercer numero: "))

if a>b and a>c:
    if b>c:
        print(f"Entonces",(a)," es el numero mayor, ",(b)," el segundo y ",(c)," el numero mas chico")
    else:
        print(f"Entonces",(a)," es el numero mayor, ",(c)," el segundo y ",(b)," el numero mas chico")
else:
    if b>a and b>c:
        if a>c:
          print(f"Entonces",(b)," es el numero mayor, ",(a)," el segundo y ",(c)," el numero mas chico")
        else:
         print(f"Entonces",(b)," es el numero mayor, ",(c)," el segundo y ",(a)," el numero mas chico")
if c>a:
    if a>b:    
        print(f"Entonces",(c)," es el numero mayor, ",(a)," el segundo y ",(b)," el numero mas chico")
    else:
        print(f"Entonces",(c)," es el numero mayor, ",(b)," el segundo y ",(a)," el numero mas chico")








