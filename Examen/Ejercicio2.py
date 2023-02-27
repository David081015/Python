# 2.- Programa que indique cual es mayor de 2 numeros con 3 digitos(cada uno), pero hay un problema
#con la intefaz y esta toma los numeros al reves
Num1 = input("Numero 1: ")
Num2 = input("Numero 2: ")
Num1 = (Num1[::-1])
Num2 = (Num2[::-1])
if(int(Num1) > int(Num2)):
    print(Num1)
else:
    print(Num2)