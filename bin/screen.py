import pygame
import consts


#def initial_screen():
background_color = consts.BACKGROUND_COLOR_GREEN
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption(consts.GAME_OPENING_TEXT_FOR_SOLDIER)
screen.fill(background_color)
pygame.display.flip()
running = True

# game loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
#return screen
#print(initial_screen())
