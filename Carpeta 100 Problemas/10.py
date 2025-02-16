archivo = open("archivo.txt", "w")
archivo.write("Esta es la primera línea.\nSegunda línea del archivo.")
archivo.close()

archivo = open("archivo.txt", "r")
contenido = archivo.read()
print("Contenido del archivo:\n", contenido)
archivo.close()

archivo = open("archivo.txt", "a")
archivo.write("\nTercera línea añadida.")
archivo.close()

archivo = open("archivo.txt", "r")
lineas = archivo.readlines()
archivo.close()

lineas[0] = "Primera línea modificada\n"

archivo = open("archivo.txt", "w")
archivo.writelines(lineas)
archivo.close()

archivo = open("archivo.txt", "a")
archivo.write("\nAlso Try Minecraft :D")
archivo.close()

archivo = open("archivo.txt", "a")
archivo.write("\nAlso Try Terraria :D")
archivo.close()

archivo = open("archivo.txt", "a")
archivo.write("\nYou dont try LoL >:v")
archivo.close()

archivo = open("archivo.txt", "r")
print("\nContenido actualizado:")
print(archivo.read())
archivo.close()