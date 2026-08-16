import pygame
import sys
import consts

def handle_user_events():
    print("press")
    pygame.key.get_pressed()
    pygame.init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #elif state["state"] != consts.RUNNING_STATE:
            #continue
        if event.type == KEYDOWN:
            if (pygame.K_LEFT == event.key):
                print("left")
            elif (pygame.K_RIGHT == event.key):
                print("right")
            elif (pygame.K_UP == event.key):
                print("up")
            elif (pygame.K_DOWN == event.key):
                print("down")







