n=int(input("Ingrese el numero del que desea saber si es primo o no: "))
m=2

if n==2:
   print("Su numero es primo")

while m<n:
   n % m
   
   if n%m==0:
      print("Su numero no es primo")
      break
   
   m=m+1
   
if m==n:
   print("su numero es primo")    



  


