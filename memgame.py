#https://replit.com/@ritza/memory-game-starter-project%23main.py

import random
import pygame
from pygame.locals import *

# used for the back of the cards
BLACK = (0,0,0)  
WHITE = (255, 255, 255)

 # used for the front of the cards
RED = (255,0,0) 
LIME = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GREEN = (0,128,0)
PURPLE = (128,0,128)
TEAL = (0,128,128)
NAVY = (0,0,128)

COLORS = [RED, LIME, BLUE, YELLOW, GREEN, PURPLE, TEAL, NAVY]

def main():

    # Pygame setup: create screen and clock for game loop
    pygame.init()
    screen = pygame.display.set_mode((200, 200))
    clock = pygame.time.Clock()

    # Shuffle cards - exactly two of each card
    cards = []
    color_randomizer = COLORS + COLORS
    random.shuffle(color_randomizer)

    # Create cards with positions
    i = 0
    for row in range(4):
        for col in range(4):
            rect = pygame.Rect(row * 50, col * 50, 50, 50)
            color = color_randomizer[i]
            card = [color, rect]
            cards.append(card)
            pygame.draw.rect(screen, color, rect)
            i += 1

    # Main game loop
    while True: 

        # Draw each card
        for card in cards:
            pygame.draw.rect(screen, card[0], card[1])

        # Check for events from the user (e.g. mouse and key presses)
        for event in pygame.event.get():

            # Check where the user *releases* the mouse button
            if event.type == MOUSEBUTTONUP:
                for card in cards:

                    # find which card was pressed on and turn it over
                    # (change color to black)
                    if card[1].collidepoint(event.pos[0], event.pos[1]):
                        card[0] = BLACK

        # update the display and tick the clock
        # this is more important if you need to do updates without 
        # user interaction, e.g. for moving objects
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()