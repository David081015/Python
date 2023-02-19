#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, preguntar al
#usuario por la fruta y el numero de kilos y muestre en pantalla el precio del numero de kilos,
#si la fruta no esta en el diccionario debe mostrar un mensaje de ello
def Smart(frutas, k):
    dic = {'Platano':1.35,'Manzana':0.80,'Pera':0.85,'Naranja':0.70}
    print((dic.get(frutas))*k)
    
print("Seleccione la fruta deseada: \n1-Platano \n2-Manzana \n3-Pera \n4-Naranja")
num = int(input())
print("Teclee la cantidad de kilos")
kilo = int(input())
if(num == 1):
    Smart("Platano", kilo)
elif(num == 2):
    Smart("Manzana", kilo)
elif(num == 3):
    Smart("Pera", kilo)
elif(num == 4):
    Smart("Naranja", kilo)
else:
    print("No existe la fruta")