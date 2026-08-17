import sys
import pygame
import consts
import game_field
import screen
import soldier


def main():
    pygame.init()
    mat=game_field.Updated_board()
    #while screen.display_screen(screen)==True:
    row,col=soldier.handle_user_events(mat, 4, 2)
    screen.display_screen(screen.screen(row,col))
    return screen




main()
