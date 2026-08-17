import pygame
import sys
import consts

import game_field

pygame.init()


def handle_user_events(row,col):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                pass
                #need to enter the other screen with the mines

            elif event.key == pygame.K_LEFT:
                if col>0:
                    col-=1

            elif event.key == pygame.K_RIGHT:
                if col<consts.COLUMNS_ON_THE_GAME_BOARD-2:
                    col+=1

            elif event.key == pygame.K_UP:
                if row>0:
                    row-=1

            elif event.key == pygame.K_DOWN:
                if row<consts.COLUMNS_ON_THE_GAME_BOARD-4:
                    row+=1

    return row,col

def Moving_soldier_on_the_game_board():
    game_board = game_field.Updated_board()
    row, col=handle_user_events(4, 5)##
    if game_board[row][col]==consts.MINE_SQUARE:
        return True
    elif col>0 and game_board[row][col-1]==consts.MINE_SQUARE:
        return True

def soldier_touches_the_flag():
    game_board=game_field.Updated_board()
    for row in range(consts.ROWS_ON_THE_GAME_BOARD):
        for col in range(consts.COLUMNS_ON_THE_GAME_BOARD):
            if game_board[row][col]==consts.SOLDIER_MOVING_SQUARE:
                if game_board[row][col]==consts.SOLDIER_SQUARE:


def main():

main()





