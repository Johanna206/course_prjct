""" Memory/Matching game
made with python3 """

# used for reading csv file
import csv
import random
import pygame
from pygame.locals import *

# load the deck of cards into 'deck' (a nested dictionary from a csv where each row is a card)
# deck is a nested dictionary where each entry is one of 78 cards
tarot_csv = open('tarot_deck.csv', mode='r')
csv_reader = csv.DictReader(tarot_csv)
line_count = 0
deck = {}
card_name_list = []
for card in csv_reader:
    if line_count == 0:
        # print(f'Column names are: {", ".join(card)}')
        line_count += 1
    deck[card['Card Name']] = card
    card_name_list.append(card['Card Name'])
    line_count += 1

# place a full deck of cards into the draw pile
draw = card_name_list
# shuffle the cards
random.shuffle(draw)
# draw 5 cards
draw = draw[0:5]
# duplicate those 5 cards
draw = draw + draw
# reshuffle the duplicate cards
random.shuffle(draw)

# Initialize a window or screen for display with captions 
pygame.init()
surface = pygame.display.set_mode((1300, 800))
pygame.display.set_caption('Tarot Matching Game')
# define colors to use in pygame
black = (0,0,0)
white = (255,255,255)
surface.fill(white)
# define a font and size for winner message
font = pygame.font.Font('font/AlexBrush-Regular.ttf', 42)
# define card image dimensions
width_height = (200, 333)
# load image of back of card
back = pygame.image.load('processed/back.jpg')
# draw rectangles where cards will go, there are 10 spots to put cards 
l1 = (50,50)
l2 = (300,50)
l3 = (550,50)
l4 = (800,50)
l5 = (1050,50)
l6 = (50,433)
l7 = (300,433)
l8 = (550,433)
l9 = (800,433)
l10 = (1050,433)
locations = (l1, l2, l3, l4, l5, l6, l7, l8, l9, l10)
# draw the back of the card on each spot
for l in locations:
    surface.blit(back, l)
pygame.display.flip()


# create a class so that each of the 10 cards can be represented by an object
class Card:
    flips = 0
    def __init__(self, name, location):
        self.name = name
        self.file = 'processed/' + deck[name]['Image File']
        self.match = False
        self.faceUp = False
        self.dimensions = (200, 333)
        self.location = location
    
    def __str__(self):
        return f"{self.name}"

    def define_rect(self):
        return pygame.Rect(self.location, self.dimensions)

    def draw_face(self):
        if self.match == False:
            f = self.file
            face = pygame.image.load(f)
            surface.blit(face, self.location)
            pygame.display.flip()
            self.faceUp = True
            Card.flips += 1
        if self.match == True:
            f = self.file
            face = pygame.image.load(f)
            surface.blit(face, self.location)
            pygame.display.flip()
            self.faceUp = False
    
    def draw_back(self):
        if self.match == False:
            surface.blit(back, self.location)
            pygame.display.flip()
            self.faceUp = False
        if self.match == True:
            self.draw_face()


# create a list of 10 cards, where each card is an object of class Card
cards = []
for i in range(10):
    cards.append(Card(draw[i], locations[i]))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # count the number of flipped cards (no including the matched cards)
            cards_up = sum(bool(card.faceUp) for card in cards)
            for card in cards:
                # rec is the clickable area of the card
                rec = card.define_rect()
                # if two cards are face up then they are not a match and a click anywhere flips them back
                if cards_up == 2:
                    previous_card = None
                    for card in cards:
                        card.draw_back()
                # if no cards are face up then the card is flipped and it becomes the previous card
                if rec.collidepoint(x, y) and card.faceUp == False and cards_up == 0:
                    card.draw_face()
                    previous_card = card
                # if one card is face up then there could be a match
                if rec.collidepoint(x, y) and card.faceUp == False and cards_up == 1:
                    card.draw_face()
                    # if there is a match, the card object info is updated
                    if previous_card.name == card.name:
                        card.match = True
                        previous_card.match = True
                        card.faceUp = False
                        previous_card.faceUp = False
                        # update number of matches found
                        matches_found = sum(bool(card.match) for card in cards)
                        # it takes 10 matches to win 
                        if matches_found == 10:
                            msg = f'You won in {Card.flips} flips!'
                            msg_txt = font.render(msg, True, black)
                            surface.blit(msg_txt, (510, 385))
                            pygame.display.flip()
                            


                    