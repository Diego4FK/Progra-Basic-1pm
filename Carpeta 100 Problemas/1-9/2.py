a=int(input("Ingrese el primer numero:"))
b=int(input("Ingrese el segundo numero:"))

if b==0 : 
   print("La division no es posible de realizar debido a que el numerador es 0")

print("adicion =", a + b)
print("sustraccion", a - b)
print("Multiplicacion", a*b)

if b!=0 :
   print("División", a/b)

#Trate de que esto fuera de una manera un poco mejorada y que no soltara un error matematico si introducias un 0, por eso se utilizaron los if
