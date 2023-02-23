# Conecta 4, la entrada va ser dos jugadores, jugador 1 O, jugador 2 X.
#El tablero es de 6x7, se debe visualizar el recorrido de las fichas. 
#El jugador debe elegir la columna donde quiere su ficha, gana el primero que agrupe 4 fichas en horizontal, 
#vertical o diagonal. Si se acaba el espacio en el tablero es empate, 
#de lo contrario mostrara un mensaje con el ganador.

# Crea un tablero de 6 filas y 7 columnas
filas, columnas = 6, 7
tablero = [[0] * 6 for i in range(7)]

# Función para dejar caer una ficha en una columna
def dejar_ficha(tablero, fila, columna, ficha):
    tablero[fila][columna] = ficha

# Función para verificar si una columna está llena
def columna_llena(tablero, columna):
    return tablero[0][columna] != 0

# Función para obtener la primera fila vacía en una columna
def obtener_fila_vacia(tablero, columna):
    for fila in range(filas-1, -1, -1):
        if tablero[fila][columna] == 0:
            return fila

# Función para verificar si alguien ganó
def ganador(tablero, ficha):
    # Verifica las victorias horizontales
    for fila in range(filas):
        for columna in range(columnas-3):
            if tablero[fila][columna] == ficha and tablero[fila][columna+1] == ficha and tablero[fila][columna+2] == ficha and tablero[fila][columna+3] == ficha:
                return True

    # Verifica las victorias verticales
    for fila in range(filas-3):
        for columna in range(columnas):
            if tablero[fila][columna] == ficha and tablero[fila+1][columna] == ficha and tablero[fila+2][columna] == ficha and tablero[fila+3][columna] == ficha:
                return True

    # Verifica las victorias diagonales hacia arriba
    for fila in range(3, filas):
        for columna in range(columnas-3):
            if tablero[fila][columna] == ficha and tablero[fila-1][columna+1] == ficha and tablero[fila-2][columna+2] == ficha and tablero[fila-3][columna+3] == ficha:
                return True

    # Verifica las victorias diagonales hacia abajo
    for fila in range(filas-3):
        for columna in range(columnas-3):
            if tablero[fila][columna] == ficha and tablero[fila+1][columna+1] == ficha and tablero[fila+2][columna+2] == ficha and tablero[fila+3][columna+3] == ficha:
                return True

# Loop principal del juego
game_over = False
turno = 0

while not game_over:
    # Turno del jugador 1
    if turno == 0:
        columna = int(input("Jugador 1, elige una columna (0-6): "))

        if not columna_llena(tablero, columna):
            fila = obtener_fila_vacia(tablero, columna)
            dejar_ficha(tablero, fila, columna, 1)

            if ganador(tablero, 1):
                print("¡Jugador 1 gana!")
                game_over = True

    # Turno del jugador 2
    else:
        columna = int(input("Jugador 2, elige una columna (0-6): "))