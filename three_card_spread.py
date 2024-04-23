""" Three card spread descriptions can be found:
https://www.alittlesparkofjoy.com/three-card-tarot-spread/
Past/Present/Future

 """
# used for reading csv file
import csv

# load the deck of cards into a nested dictionary from a csv where each row is a card
tarot_csv = open('tarot_deck.csv', mode='r')
csv_reader = csv.DictReader(tarot_csv)
line_count = 0
deck = {}
card_list = []
for card in csv_reader:
    if line_count == 0:
        # print(f'Column names are: {", ".join(card)}')
        line_count += 1
    # print(card)
    deck[card['Card Name']] = card
    card_list.append(card['Card Name'])
    line_count += 1
# deck is a nested dictionary where each entry is one of 78 cards
# deck.keys() gives the names of all the cards
# card_list is a list of the deck keys, in this case card names
# print(card_list)

cl = card_list.copy()
# Draw one card 'randomly' and remove it from the deck
int1 = int(input("Enter a random integer while thinking of the past: "))
draw1 = cl[int1%len(cl)]
cl.remove(draw1)

# Draw a second card and remove it from the deck
int2 = int(input("Enter a random integer while thinking of the present: "))
draw2= cl[int2%len(cl)]
cl.remove(draw2)

# Draw a third card and remove it from the deck
int3 = int(input("Enter a random integer while thinking of the future: "))
draw3 = cl[int3%len(cl)]
cl.remove(draw3)

print('Card representing the past: ', draw1)
print('card representing the present: ', draw2)
print('and card representing the future: ', draw3)

