# Conecta 4, la entrada va ser dos jugadores, jugador 1 O, jugador 2 X.
#El tablero es de 6x7, se debe visualizar el recorrido de las fichas. 
#El jugador debe elegir la columna donde quiere su ficha, gana el primero que agrupe 4 fichas en horizontal, 
#vertical o diagonal. Si se acaba el espacio en el tablero es empate, 
#de lo contrario mostrara un mensaje con el ganador.

import numpy as np

def create_board():
    board = np.zeros((6, 7))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(6):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(4):
        for r in range(6):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(7):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(4):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(4):
        for r in range(3, 6):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def play_game():
    board = create_board()
    game_over = False
    turn = 0

    while not game_over:
        # Player 1 input
        if turn == 0:
            col = int(input("Player 1 make your selection (0-6): "))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)

                if winning_move(board, 1):
                    print("Player 1 wins!")
                    game_over = True

        # Player 2 input
        else:
            col = int(input("Player 2 make your selection (0-6): "))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                if winning_move(board, 2):
                    print("Player 2 wins!")
                    game_over = True

        print_board(board)
        turn += 1
        turn %= 2

play_game()
