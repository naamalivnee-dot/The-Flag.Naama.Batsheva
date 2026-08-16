import pygame
import consts
import random

def blank_screen():
    #background_color = consts.BACKGROUND_COLOR_GREEN
    screen = pygame.display.set_mode((1000,500))
    #pygame.display.set_caption(consts.GAME_OPENING_TEXT_FOR_SOLDIER)
    #screen.fill(background_color)
    pygame.display.flip()
    return screen

def green_screen():
    screen = blank_screen()
    background_color = consts.BACKGROUND_COLOR_GREEN
    screen.fill(background_color)
    pygame.display.flip()
    return screen

def bush():
    screen = green_screen()
    image = pygame.image.load('grass.png')
    for i in range(20):
        img_small = pygame.transform.scale(image, (40, 30))
        x = random.randint(0,920)
        y = random.randint(0,440)
        screen.blit(img_small, (x, y))
    #screen.blit(image, (100, 100))
    pygame.display.flip()
    return screen

def display_screen(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

#display_screen(bush())
