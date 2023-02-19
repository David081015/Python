#Estructuras de control

#if
# a = 4
# #b = 2
# b = 0

# #Si no tiene nada adentro el if marca error, para evitar esto se escribe pass adentro
# if b!=0:
#     print(a/b)
# print(b)

# a = 10
# if a > 5 and a < 15:
#     print("A mayor que 5 y menor que 15")

# if a > 5: print("Es > 5");print("Dentro del if");print(a+b)

# #x = 5
# x = 9
# if x==5:
#     print("Es 5")
# else:
#     print("No es 5")

# x = 8

# if x==5:
#     print("Es 5")
# elif x==6:
#     print("Es 6")
# elif x==7:
#     print("Es 7")
# else:
#     print(8)

# print("Es 8" if x == 8 else "No es 5")

# a = 10
# #b = 5
# b = 0
# c = a/b if b!=0 else -1
# print(c)

#for
# for i in "python":
#     print(i)

# lista = [[56,34,2],[12,4,5],[9,3,2]]

# for i in lista:
#     for j in i:
#         print(j)

#Range
# r = range(6)
# print(r)
# for r in range(3):
#     print(r)

# for i in range(5,20):
#     print(i)

# for s in range(5,20,2):
#     print(s)

# cadena = "python"
# for letra in cadena:
#     if letra == "y":
#         print(letra)
#         break

# for letra in cadena:
#     if letra == "p":
#         continue
#     print(letra)

#While
# x = 5
# while x > 0:
#     x -=1
#     print(x)

# x = 5
# while x > 0: x-=1; print(x)

# x =5
# while x > 0:
#     x-=1
#     print(x)
# else:
#     print("Bucle finalizado")
#     x=5

#Nunca llega el else
# while True:
#     x-=1
#     print(x)
# else: print("fin del bucle")

# while x > 0:
#     x-=1
#     print(x)
#     if x == 4:
#         break
# else:
#     print("fin del bucle")

z = 14 #7
x = 2 #1
while z > 0:
    print(' '*z + '*'*x + ' '*z)
    z -=1
    x +=2