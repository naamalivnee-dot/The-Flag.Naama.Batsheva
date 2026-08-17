import pygame
import sys
import consts

import game_field

pygame.init()


def handle_user_events(row,col):
    game_board = game_field.Updated_board()
    game_board[row][col]=consts.NO_MINE

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
                if row<consts.ROWS_ON_THE_GAME_BOARD-4:
                    row+=1

    game_board[row][col] = consts.SOLDIER_MOVING_SQUARE
    return row,col

def soldier_touches_the_mines(row,col): #index of SOLDIER_MOVING_SQUARE
    game_board = game_field.Updated_board()
    if col<consts.COLUMNS_ON_THE_GAME_BOARD:
        if game_board[row][col+1]==consts.MINE_SQUARE:
            return True

    if row<consts.ROWS_ON_THE_GAME_BOARD:
        if game_board[row+1][col] == consts.MINE_SQUARE:
            return True

    else:
        return False

def Identification_of_the_soldier_body(row,col): #index of SOLDIER_MOVING_SQUARE
    soldier_body_list=[]
    for i in range(row+1,row+4):
        for j in range(col,col+1):
            soldier_body_list.append(i)
            soldier_body_list.append(j)


def soldier_touches_the_flag(row,col): #index of SOLDIER_MOVING_SQUARE
    game_board = game_field.Updated_board()
    for i in range(row+1,row+4):
        for j in range(col,col+1):
            if game_board[i][j+1] == consts.FLAG_SQUARE:
                return True
                break
    else:
        return False


def main():
    row,col=handle_user_events(4, 2)
    if soldier_touches_the_mines(row,col)==True:
        print("Soldier touches them!")
        exit()
    if soldier_touches_the_flag(row,col)==True:
        print("win")

main()





