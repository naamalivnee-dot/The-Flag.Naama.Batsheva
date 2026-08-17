import pygame
import sys
import consts
import screen
import game_field





def handle_user_events(mat, row,col):
    mat[row][col]=consts.NO_MINE
    window = screen.flag(screen.grass(screen.green_screen()))


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("left")
                    if col>0:
                        col-=1

                elif event.key == pygame.K_RIGHT:
                    print("right")
                    if col<consts.COLUMNS_ON_THE_GAME_BOARD-2:
                        col+=1

                elif event.key == pygame.K_UP:
                    print("up")
                    if row>0:
                        row-=1

                elif event.key == pygame.K_DOWN:
                    print("down")
                    if row<consts.ROWS_ON_THE_GAME_BOARD-4:
                        row+=1
        game_field.Updated_board()
        screen.draw_soldier(window,row,col)
        #screen.screen(row, col)
        #mat[row][col] = consts.SOLDIER_MOVING_SQUARE
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
'''
def Identification_of_the_soldier_body(row,col): #index of SOLDIER_MOVING_SQUARE
    soldier_body_list=[]
    for i in range(row+1,row+4):
        for j in range(col,col+1):
            soldier_body_list.append(i)
            soldier_body_list.append(j)
'''


def soldier_touches_the_flag(row,col): #index of SOLDIER_MOVING_SQUARE
    game_board = game_field.Updated_board()
    for i in range(row+1,row+4):
        for j in range(col,col+1):
            if game_board[i][j+1] == consts.FLAG_SQUARE:
                return True
                break
    else:
        return False

'''
def main():
    row,col=handle_user_events(4, 2)
    if soldier_touches_the_mines(row,col)==True:
        print("Soldier touches them!")
        exit()
    if soldier_touches_the_flag(row,col)==True:
        print("win")

main()
'''





