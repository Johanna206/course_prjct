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
        # print(f'Column names are: {", ".join(card)}')
        line_count += 1
    deck[card['Card Name']] = card
    card_name_list.append(card['Card Name'])
    line_count += 1

# initialize empty tableau piles and empty discard pile
draw = []
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
discard = []

# place a full deck of cards into the draw pile and shuffle them
draw = card_name_list
random.shuffle(draw)

# function to deal 5 cards from the draw pile to the top of each tableau pile. gives an error if the draw runs out of cards.
def deal():
    '''Deals cards from top of draw pile to top of each tableau pile. No arguments, no return.'''
    for t in [t1, t2, t3, t4, t5]:
        if len(draw) > 0:
            t.insert(0, draw.pop(0))

# function to move card to discard pile
def mv_discard(card_pile):
    '''Moves top card to discard pile. Argument is card pile.'''
    if can_discard(card_pile) == True:
        discard.insert(0, card_pile.pop(0))
    else:
        print('error')

# function to check if a tableau is empty and move a card there
def mv_empty(card_pile):
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

# function to check if there is an empty tableau pile
def any_empty():
    if (len(t1) == 0 or
    len(t2) == 0 or
    len(t3) == 0 or
    len(t4) == 0 or
    len(t5) == 0):
        return True
    else:
        return False

# compare card values to see if a card can be moved to the discard pile. returns False if card pile is empty. 
def can_discard(card_pile):
    ''' argument is a card pile. checks each tableau pile to see if they have a card of the same suit and greater value. 
    indicates if a card can be discarded. returns True if it can, False if it can't.  '''
    if len(card_pile) == 0:
        return False
    elif (len(t1) > 0 and
        deck[card_pile[0]]['Suit'] == deck[t1[0]]['Suit'] and 
        int(deck[card_pile[0]]['Value']) < int(deck[t1[0]]['Value'])):
        return True
    elif (len(t2) > 0 and
        deck[card_pile[0]]['Suit'] == deck[t2[0]]['Suit'] and
        int(deck[card_pile[0]]['Value']) < int(deck[t2[0]]['Value'])):
        return True
    elif (len(t3) > 0 and
        deck[card_pile[0]]['Suit'] == deck[t3[0]]['Suit'] and
        int(deck[card_pile[0]]['Value']) < int(deck[t3[0]]['Value'])):
        return True
    elif (len(t4) > 0 and
        deck[card_pile[0]]['Suit'] == deck[t4[0]]['Suit'] and
        int(deck[card_pile[0]]['Value']) < int(deck[t4[0]]['Value'])):
        return True
    elif (len(t5) > 0 and
        deck[card_pile[0]]['Suit'] == deck[t5[0]]['Suit'] and
        int(deck[card_pile[0]]['Value']) < int(deck[t5[0]]['Value'])):
        return True
    else:
        return False

# The game ends in a loss when the draw pile is empty and none of the 5 top cards can be moved to the discard pile
def game_still_going():
    '''checks if the game is lost. returns True if so. error if no cards in tableau pile. '''
    if (len(draw) == 0 and 
        can_discard(t1) == False and 
        can_discard(t2) == False and 
        can_discard(t3) == False and 
        can_discard(t4) == False and 
        can_discard(t5) == False):
        return True
    else:
        return False

# calculate the score
def get_score():
    '''calculates score, no args, returns integer score'''
    return len(discard)

# The game is won when all the cards have been moved into the discard pile (except 1 highest card in each suit) 
def game_won():
    '''checks if the game is won. returns True if so, False if not.'''
    if get_score() == 73:
        return True
    else:
        return False



# can_discard(t1), can_discard(t2), can_discard(t3), can_discard(t4), can_discard(t5)
# print(t1, '\n', t2, '\n', t3, '\n', t4, '\n', t5)

