import consts



def create_board():
    game_board= []
    for i in range(consts.ROWS_ON_THE_GAME_BOARD):
        rows = []
        for col in range(consts.COLUMNS_ON_THE_GAME_BOARD):
            col = "_"
            rows.append(col)
        game_board.append(rows)

    return game_board