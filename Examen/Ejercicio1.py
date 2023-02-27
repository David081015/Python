# 1.- Dividir un cierto entero n por otro m hasta n=1 obteniendo una secuencia de numeros cada numeros
#de esta secuncia almacenados en una lista, las secuencias deben cumplir hasta llegar a n=1 si n=1 se
#debera imprimir la secuencia entera en dado caso imprimir en pantalla "secuencia invalida"
n = int(input("Numero: "))
m = int(input("Otro: "))
Lista = []
Salir = False
while(Salir == False ):
    Lista.append(n)
    n = n/m
    if(n == 1):
        print(Lista)
        Salir = True
    if(n != 1):
        print("Secuencia invalida")
        Salir = True