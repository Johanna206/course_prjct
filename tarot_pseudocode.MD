
https://en.wikipedia.org/wiki/Aces_Up
Aces up is, according to google, the easiest version of solitaire, and therefore, hopefully the easiest version to code. The original version of Aces up is played with a 4-suit 5-card deck in 4 tableau piles and winnable 1/43rd of the time. I hope to make a card game that is more winnable and that uses a 5-suit 78-card deck. I will do this by having 6 tableau piles.

visual of initial deal:
[72 draw] [1 tableau1] [1 tableau2] [1 tableau3] [1 tableau4] [1 tableau5] [1 tableau6] [0 discard] 

visual of winning state:
[0 draw] [0 tableau1] [0 tableau2] [0 tableau3] [0 tableau4] [0 tableau5] [0 tableau6] [78 discard] 

- each card will have the following properties:
    - integer value
    - suit
    - pile
- each pile will have an order with the 1st card being the 'top'

- to start the game:
- shuffle deck
- deal one card face up into each of 6 tableau piles
- place the rest of the deck face down into the draw pile
- display 0 cards in the empty discard pile 

- WHILE there are cards in the tableau or draw piles:
    - allow the user to click on cards

- IF the user clicks on the draw pile
    - one card is dealt from the draw pile on to each of the 6 tableau piles
    - these new cards are now the 'top' of each tableau pile

- IF the user clicks on the tops of the tableau piles AND there is another card of the same suit AND greater values on the 'top' of one of the tableau piles
    - AND there are empty tableau piles, 
        - THEN the card goes into an empty space in the tableau piles
        - AND the next card on the tableau pile becomes the 'top'
    - ELSE (when all the tableau piles are full)  
        - THEN the card will go into the discard pile
        - AND the next card on the tableau pile becomes the 'top'

- WHEN all the cards are in the discard pile
    - the game ends
    - the user wins! 