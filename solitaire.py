""" Aces Up solitaire card rules found at
https://en.wikipedia.org/wiki/Aces_Up
 """
# used for reading csv file
import csv
import random

# load the deck of cards into 'deck' (a nested dictionary from a csv where each row is a card)
# deck is a nested dictionary where each entry is one of 78 cards
tarot_csv = open('tarot_deck.csv', mode='r')
csv_reader = csv.DictReader(tarot_csv)
line_count = 0
deck = {}
card_name_list = []
for card in csv_reader:
    if line_count == 0:
        print(f'Column names are: {", ".join(card)}')
        line_count += 1
    deck[card['Card Name']] = card
    card_name_list.append(card['Card Name'])
    line_count += 1

'''
# each card has a integer value, suit, and pile
card = 'The Fool'
card = 'King of Cups'
# card value
int(deck[card]['Value'])
# card suit
deck[card]['Suit']
# card pile
deck[card]['Pile']
# card number / pile position
deck[card]['Number']
'''

# place the cards into the draw pile and shuffle them
draw = card_name_list
random.shuffle(draw)
# the top card is draw[0]
# initialize empty tableau piles and empty discard pile
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
t6 = []
discard = []

# function to deal 6 cards from the draw pile to the top of each tableau pile. gives an error if the draw runs out of cards.
def deal():
    '''Deals cards from top of draw pile to top of each tableau pile. No arguments, no return.'''
    t1.insert(0, draw.pop(0))
    t2.insert(0, draw.pop(0))
    t3.insert(0, draw.pop(0))
    t4.insert(0, draw.pop(0))
    t5.insert(0, draw.pop(0))
    t6.insert(0, draw.pop(0))

# function to move card to discard pile
def move_to_discard(card_pile):
    '''Moves top card to discard pile. Argument is card pile.'''
    discard.insert(0, card_pile.pop(0))

# function to check if a tableau is empty and move a card there, otherwise return something
def move_to_empty(card_pile):
    '''Moves top card to first empty pile'''
    if len(t1) == 0:
        t1.insert(0, card_pile.pop(0))
    elif len(t2) == 0:
        t2.insert(0, card_pile.pop(0))
    elif len(t3) == 0:
        t3.insert(0, card_pile.pop(0))
    elif len(t4) == 0:
        t4.insert(0, card_pile.pop(0))
    elif len(t5) == 0:
        t5.insert(0, card_pile.pop(0))
    elif len(t6) == 0:
        t6.insert(0, card_pile.pop(0))

# find points, 78 is a win
def score():
    '''calculates score'''
    len(discard)
        
