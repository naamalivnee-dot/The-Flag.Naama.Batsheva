import pygame
import consts
import random

from bin import game_field


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

def grass():
    screen = green_screen()
    image = pygame.image.load('grass.png')
    grass_height = consts.GRASS_HEIGHT * consts.CONVERT_TO_SCREEN
    grass_width = consts.GRASS_WIDTH * consts.CONVERT_TO_SCREEN
    for i in range(consts.CONVERT_TO_SCREEN):
        img_small = pygame.transform.scale(image, (grass_height, grass_width))
        x = random.randint(0, consts.WINDOW_WIDTH - grass_width)
        y = random.randint(0, consts.WINDOW_HEIGHT - grass_height)
        screen.blit(img_small, (x, y))
    pygame.display.flip()
    return screen

def net_screen():
    screen = blank_screen()
    color_line = consts.BACKGROUND_COLOR_GREEN
    for i in range(consts.WINDOW_HEIGHT):
        x = i * consts.CONVERT_TO_SCREEN
        pygame.draw.line(screen, color_line, (x, 0), (x, consts.WINDOW_WIDTH))
    for i in range(consts.WINDOW_WIDTH):
        y = i * consts.CONVERT_TO_SCREEN
        pygame.draw.line(screen, color_line, (0, y), (consts.WINDOW_WIDTH, y))
    pygame.display.flip()
    return screen


def mine(met):
    screen = net_screen()
    image = pygame.image.load('mine.png')
    mine_height = consts.MINE_HEIGHT * consts.CONVERT_TO_SCREEN
    mine_width = consts.MINE_WIDTH * consts.CONVERT_TO_SCREEN
    img_small = pygame.transform.scale(image, (mine_width, mine_height))
    for i in range(len(met)):
        for j in range(len(met[i])):
            if met[i][j] == consts.MINE_SQUARE:
                y = i * consts.CONVERT_TO_SCREEN
                x = j * consts.CONVERT_TO_SCREEN
                screen.blit(img_small, (x, y))
    pygame.display.flip()
    return screen


def flag():
    screen = grass()
    image = pygame.image.load('flag.png')
    flag_height = consts.FLAG_HEIGHT * consts.CONVERT_TO_SCREEN
    flag_width = consts.FLAG_WIDTH * consts.CONVERT_TO_SCREEN
    img_small = pygame.transform.scale(image, (flag_width, flag_height))
    x = consts.WINDOW_WIDTH - flag_width
    y = consts.WINDOW_HEIGHT - flag_height
    screen.blit(img_small, (x, y))
    pygame.display.flip()
    return screen

def draw_soldier(met):
    screen = flag()
    image = pygame.image.load('soldier.png')
    soldier_height = consts.SOLDIER_HEIGHT * consts.CONVERT_TO_SCREEN
    soldier_width = consts.SOLDIER_WIDTH * consts.CONVERT_TO_SCREEN
    img_small = pygame.transform.scale(image, (soldier_width, soldier_height))
    for i in range(len(met)):
        for j in range(len(met[i])):
            if met[i][j] == consts.SOLDIER_MOVING_SQUARE:
                y = i
                x = j
                screen.blit(img_small, (x, y))
    pygame.display.flip()
    return screen




def draw_night_soldier(met):
    screen = mine_screen()
    image = pygame.image.load('soldier_nigth.png')
    soldier_height = consts.SOLDIER_HEIGHT * consts.CONVERT_TO_SCREEN
    soldier_width = consts.SOLDIER_WIDTH * consts.CONVERT_TO_SCREEN
    img_small = pygame.transform.scale(image, (soldier_width, soldier_height))
    for i in range(len(met)):
        for j in range(len(met[i])):
            if met[i][j] == consts.SOLDIER_SQUARE:
                y = i
                x = j
                screen.blit(img_small, (x, y))
    pygame.display.flip()
    return screen








def display_screen(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

#display_screen(flag())
display_screen(draw_soldier(game_field.Updated_board()))



def mine_screen():
    game_board = game_field.create_board()
    met = game_field.Updated_board()
    return mine(met)
    #display_screen(mine_screen(met))
#display_screen(mine_screen())
#main_net_screen()

display_screen(draw_night_soldier(game_field.Updated_board()))


#def winning_screen():
    #screen = draw_soldier(game_field.Updated_board())
    #pygame.init()
    #font = pygame.font.Font('freesansbold.ttf', 100)
    #text = font.render('you win!', True, consts.WHITE)
    #screen.blit(text, (consts.WINDOW_HEIGHT/2, consts.WINDOW_WIDTH/2))
    #pygame.display.update()
    #return screen


#display_screen(winning_screen())


