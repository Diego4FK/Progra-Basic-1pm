n=int(input("Ingrese el numero de productos que quiere registrar: "))
c=1
productos=[]
while c<=n: #Ciclo para el ingreso de los datos de los productos
    Producto=input("Ingrese el producto: ")
    Categoría=input("Ingrese su categoría: ")
    Cantidad=int(input("ingrese la cantidad: "))
    Precio=int(input("Ingrese su precio: "))
    dic_producto = {
        "Producto": Producto,
        "Categoría": Categoría,
        "Cantidad": Cantidad,
        "Precio": Precio
     }
    productos.append(dic_producto)
    c=c+1

productos = sorted(productos, key=lambda x: x["Precio"], reverse=True)

# Mostrar los productos ordenados
print("\nProductos registrados (ordenados por precio de mayor a menor):")
for prod in productos:
    print(prod)
print("\nProductos registrados:")
for prod in productos:
    print(prod)
s=0
z=s
while z==s: #cICLO PARA BUSCAR UN PRODUCTO
 x=input("Producto que esta buscando: ")
 if x in dic_producto:
    print("Producto encontrado:", dic_producto[x])
 else:
    print("Producto no encontrado")
 n=input("Desea buscar otro producto?(s/n) ")
 if n!=s:
    break 
