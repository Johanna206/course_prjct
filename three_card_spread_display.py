""" Three card spread descriptions can be found:
https://www.alittlesparkofjoy.com/three-card-tarot-spread/
Past/Present/Future """
'''files needed:
tarot_deck.csv
processed/images
'font/AlexBrush-Regular.ttf'
'''
# used for randomly picking cards
import random
# used for reading tarot card csv
import csv
# used for creating game
import pygame
from pygame.locals import *
# initialize all imported pygame modules
pygame.init()

# get the list of card files from the tarot deck csv
tarot_csv = open('tarot_deck.csv', mode='r')
csv_reader = csv.DictReader(tarot_csv)
line_count = 0
card_file = []
for card in csv_reader:
    if line_count == 0:
        line_count += 1
    card_file.append(card['Image File'])
    line_count += 1

# generate 3 random cards, removing each one from the deck after drawing it
card1 = card_file[random.randint(0,77)]
card_file.remove(card1)
card2 = card_file[random.randint(0,76)]
card_file.remove(card2)
card3 = card_file[random.randint(0,75)]
card_file.remove(card3)

# load images of each card and the back of the card into pygame
# randomly flips some upsidedown
back = pygame.image.load('processed/back.jpg')
flip1 = random.choice([True,False])
image1 = pygame.image.load('processed/'+card1)
image1 = pygame.transform.flip(image1, flip1, flip1)
flip2 = random.choice([True,False])
image2 = pygame.image.load('processed/'+card2)
image2 = pygame.transform.flip(image2, flip2, flip2)
flip3 = random.choice([True,False])
image3 = pygame.image.load('processed/'+card3)
image3 = pygame.transform.flip(image3, flip3, flip3)

# load font and messages into pygame
black = (0,0,0)
white = (255,255,255)
font = pygame.font.Font('font/AlexBrush-Regular.ttf', 32)
past = font.render('Past', True, white, black) 
present = font.render('Present', True, white, black) 
future = font.render('Future', True, white, black) 
click_here = font.render('click to flip', True, white, black)
clicked = font.render('click to flip', True, black, black)

# Initialize a window or screen for display with caption
surface = pygame.display.set_mode((800, 433))
pygame.display.set_caption('Tarot Game')

# Using blit to copy content from one surface to other (lay out the cards and text)
# rectangles are the clickable areas of the card
surface.blit(back, (50, 50))
rectangle1 = pygame.Rect((50, 50), (200,333))
surface.blit(back, (300, 50))
rectangle2 = pygame.Rect((300, 50), (200,333))
surface.blit(back, (550, 50))
rectangle3 = pygame.Rect((550, 50), (200,333))
surface.blit(past, (110, 10))
surface.blit(present, (350, 10))
surface.blit(future, (610, 10))
surface.blit(click_here, (90, 390))
pygame.display.flip()

# cards are dealt facedown and must be turned over in the correct order
c1_flip = False
c2_flip = False
c3_flip = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if rectangle1.collidepoint(x, y) and c2_flip == False:
                surface.blit(image1, (50,50))
                surface.blit(clicked, (90, 390))
                surface.blit(click_here, (340, 390))
                pygame.display.flip()
                c1_flip = True
            if rectangle2.collidepoint(x, y) and c1_flip == True and c3_flip == False:
                surface.blit(image2, (300,50))
                surface.blit(clicked, (340, 390))
                surface.blit(click_here, (590, 390))
                pygame.display.flip()
                c2_flip = True
            if rectangle3.collidepoint(x, y) and c2_flip == True:
                surface.blit(image3, (550,50))
                surface.blit(clicked, (590, 390))
                pygame.display.flip()
                c3_flip = True

# Uninitialize the display module
# pygame.quit()
# Raise a SystemExit exception, signaling an intention to exit the interpreter.
# sys.exit()


