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

        if event.type == pygame.KEYDOWN:
            if event.type == KEYDOWN:
                if (event.key == pygame.K_LEFT):
                    sprite = pygame.image.load('left.png')
                elif (event.key == pygame.K_RIGHT):
                    sprite = pygame.image.load('right.png')
                elif (event.key == pygame.K_UP):
                    sprite = pygame.image.load('up.png')
                elif (event.key == pygame.K_DOWN):
                    sprite = pygame.image.load('down.png')
