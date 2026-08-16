import pygame
import consts
import random

def blank_screen():
    screen = pygame.display.set_mode((consts.WINDOW_WIDTH,consts.WINDOW_HEIGHT))
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
    for i in range(consts.CONVERT_TO_SCREEN):
        img_small = pygame.transform.scale(image, (consts.GRASS_HEIGHT, consts.GRASS_WIDTH))
        x = random.randint(consts.MAN_WIDTH, consts.WINDOW_WIDTH - consts.GRASS_WIDTH)
        y = random.randint(consts.MAN_HEIGHT, consts.WINDOW_HEIGHT - consts.GRASS_HEIGHT)
        screen.blit(img_small, (x, y))
    #screen.blit(image, (100, 100))
    pygame.display.flip()
    return screen

def net_screen():
    screen = blank_screen()
    color_line = consts.BACKGROUND_COLOR_GREEN
    for i in range(consts.WINDOW_HEIGHT):
        x = i * consts.CONVERT_TO_SCREEN
        pygame.draw.line(screen, color_line, (x, 0), (x, consts.WINDOW_WIDTH))
        pygame.display.flip()
    for i in range(consts.WINDOW_WIDTH):
        y = i * consts.CONVERT_TO_SCREEN
        pygame.draw.line(screen, color_line, (0, y), (consts.WINDOW_WIDTH, y))
        pygame.display.flip()
    return screen


def mine_screen():
    screen = net_screen()
    image = pygame.image.load('mine.png')
    img_small = pygame.transform.scale(image, (consts.MINE_HEIGHT, consts.MINE_WIDTH))




def display_screen(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

display_screen(bush())
display_screen(net_screen())
