#Escribir un programa que pregunte el nombre de un producto, su precio y numero de unidades
#y va mostrar en pantalla el nombre de producto, seguido de su precio unitario con 6 digitos y dos decimales 
#el numero de unidades con 3 digitos y el coste total 8 digitos y 2 decimales.
Producto = input("Nombre del producto: ")
Precio = float(input("Precio unitario: "))
Unidades = int(input("Número de unidades: "))
print('{producto}: {unidades:3d} unidades x ${precio:6.2f} = ${total:8.2f}'.format(producto = Producto, unidades = Unidades, precio = Precio, total = Unidades * Precio))