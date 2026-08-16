import sys

import pygame
import consts
import game_field
import screen
import soldier



move_f


def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN