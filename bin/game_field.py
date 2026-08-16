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

    return game_board

def Flag_position(game_board):
    Flag_row=consts.ROWS_ON_THE_GAME_BOARD-consts.FLAG_HEIGHT
    flag_col=consts.COLUMNS_ON_THE_GAME_BOARD-consts.FLAG_WIDTH

    for row in range(Flag_row,consts.ROWS_ON_THE_GAME_BOARD):
        for col in range(flag_col,consts.COLUMNS_ON_THE_GAME_BOARD):
            game_board[row][col] = consts.FLAG_SQUARE

    return game_board

def Touching_the_flag():
    pass

def Placing_mines_in_game_board(game_board):
    for i in range(20):
        row=random.randint(0, consts.ROWS_ON_THE_GAME_BOARD-1)
        col=random.randint(0, consts.COLUMNS_ON_THE_GAME_BOARD-1)
        if game_board[row][col] != consts.MINE_SQUARE and game_board[row][col]!=consts.FLAG_SQUARE:
            game_board[row][col]=consts.MINE_SQUARE

    return game_board

def main():
    game_board=create_board()
    Flag_position(game_board)
    game_board=Placing_mines_in_game_board(game_board)
    print(game_board)


main()