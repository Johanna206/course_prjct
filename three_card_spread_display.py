""" Three card spread descriptions can be found:
https://www.alittlesparkofjoy.com/three-card-tarot-spread/
Past/Present/Future """

# used for system info
import sys
# used for creating game
import pygame
from pygame.locals import *
# initialize all imported pygame modules
pygame.init()
# load the back of the card
back = pygame.image.load('processed/back.jpg')
# load font
black = (0,0,0)
white = (255,255,255)
font = pygame.font.Font('font/AlexBrush-Regular.ttf', 32)
past = font.render('Past', True, white, black) 
present = font.render('Present', True, white, black) 
future = font.render('Future', True, white, black) 

while True:
    # Initialize a window or screen for display
    surface = pygame.display.set_mode((800, 433))
    # Set the current window caption
    pygame.display.set_caption('Tarot Game')
    #    create an object to help track time
    clock = pygame.time.Clock()
    # Load and image
    
    # Using blit to copy content from one surface to other
    surface.blit(back, (50, 50))
    surface.blit(back, (300, 50))
    surface.blit(back, (550, 50))
    surface.blit(past, (110, 10))
    surface.blit(present, (350, 10))
    surface.blit(future, (610, 10))

    pygame.display.flip()
# Uninitialize the display module
    pygame.display.quit()
#Raise a SystemExit exception, signaling an intention to exit the interpreter.
#sys.exit()


