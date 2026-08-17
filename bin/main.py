import sys
import pygame
import consts
import game_field
import screen
import soldier


def main():
    pygame.init()
    met=game_field.Updated_board()
    while screen.display_screen(screen)==True:
        row,col=soldier.handle_user_events(4, 2)

        screen.draw_soldier(met)




main()
