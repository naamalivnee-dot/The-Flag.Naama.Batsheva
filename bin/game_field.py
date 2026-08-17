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


def Touching_the_flag(game_board):
    Flag_row=consts.ROWS_ON_THE_GAME_BOARD-consts.FLAG_HEIGHT
    flag_col=consts.COLUMNS_ON_THE_GAME_BOARD-consts.FLAG_WIDTH

    for row in range(Flag_row,consts.ROWS_ON_THE_GAME_BOARD):
        for col in range(flag_col,consts.COLUMNS_ON_THE_GAME_BOARD):
            game_board[row][col] = consts.FLAG_SQUARE


def Touching_the_soldier(game_board):
    for row in range(consts.SOLDIER_HEIGHT):
        for col in range(consts.SOLDIER_WIDTH):
            game_board[row][col] = consts.SOLDIER_SQUARE


def Placing_mines_in_game_board(game_board):
    placed_mines=0
    while placed_mines<20:
        row=random.randint(0, consts.ROWS_ON_THE_GAME_BOARD-1)
        col=random.randint(0, consts.COLUMNS_ON_THE_GAME_BOARD-1)
        if game_board[row][col] != consts.MINE_SQUARE and game_board[row][col]!=consts.FLAG_SQUARE and  game_board[row][col] != consts.SOLDIER_SQUARE:
            game_board[row][col]=consts.MINE_SQUARE
            placed_mines += 1



def moving_soldier_piece(game_board):
    game_board[consts.SOLDIER_HEIGHT-1][consts.SOLDIER_WIDTH-1]=consts.SOLDIER_MOVING_SQUARE
    return game_board


def  Updated_board():
    game_board=create_board()
    Touching_the_flag(game_board)
    Touching_the_soldier(game_board)
    Placing_mines_in_game_board(game_board)
    game_board=moving_soldier_piece(game_board)
    return game_board

def main():
    game_board=Updated_board()
    for row in game_board:
        for col in row:
            print(col, end=" ")
        print()
# main()