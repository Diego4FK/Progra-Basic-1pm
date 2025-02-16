n=int(input("Ingresa el limite: "))
limite = n 
a, b = 0, 1  

while a <= limite:
    print(a)  
    a, b = b, a + b  

