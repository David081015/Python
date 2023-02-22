# En una matriz 5x4, pedir al usuario los valores, en una segunda matriz guardar uno si el numero guardado
# en la misma posicion de la otra matriz es multiplo de 3, guardar un dos 2 si el numero es multiplo de 5
# o guardar un 3 si es multiplo de 3 y 5 a la vez, sino se cumple ninguna de las anteriores guardar un cero.
# Imprimir ambas matrices en formato de matriz.

Entrada = [[0] * 4 for i in range(5)]
Salida = [[0] * 4 for i in range(5)]

for i in range(5):
    for j in range(4):
        Entrada[i][j] = int(input("Ingrese un número para la posición [{},{}]: ".format(i,j)))
        if Entrada[i][j] % 3 == 0 and Entrada[i][j] % 5 == 0:
            Salida[i][j] = 3
        elif Entrada[i][j] % 3 == 0:
            Salida[i][j] = 1
        elif Entrada[i][j] % 5 == 0:
            Salida[i][j] = 2
        else:
            Salida[i][j] = 0

print("Matriz de entrada:")
for fila in Entrada:
    print(fila)

print("Matriz de salida:")
for fila in Salida:
    print(fila)
