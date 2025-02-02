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


  


