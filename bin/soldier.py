import pygame
import sys
import consts
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



