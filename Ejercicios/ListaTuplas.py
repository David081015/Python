#Escribir un programa que almacene las matrices en una tupla y muestre en pantalla su producto, el producto
#debe estar dado en listas anidadas.
A = [[1,2,3],[4,5,6]]
B = [[-1,0],[0,1],[1,1]]

C = [[0,0],[0,0]]
for i in range(len (A)):
    for j in range(len (B[0])):
        for k in range(len (B)):
            C[i][j] += A[i][k] * B[k][j]
for i in range(len(C)):
    C[i] = tuple(C[i])
C = tuple(C)
for i in range(len(C)):
    print(C[i]) 