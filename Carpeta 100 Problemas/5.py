n=int(input("Ingrese el numero del que desea saber si es primo o no: "))
m=2

if n>1:
    while m<n:
      n % m
   
      if n%m==0:
         print("Su numero no es primo")
         break
   
      m=m+1
     
    if m==n or n==2:
     print("su numero es primo")    

if n==1:
   print("Su numero no es primo")

#Usamos un while para que se pudiera verificar de una forma muy primitiva si el numero tenia mas divisores y no tener que hacerlo uno por uno
#el % es para obtener su residuo

  


