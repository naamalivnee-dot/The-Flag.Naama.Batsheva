import consts
import random



def create_board():
    game_board= []
    for i in range(consts.ROWS_ON_THE_GAME_BOARD):
        rows = []
        for col in range(consts.COLUMNS_ON_THE_GAME_BOARD):
            col = consts.NO_MINE
            rows.append(col)
        game_board.append(rows)
        print(game_board)
    return game_board
print(create_board())

def