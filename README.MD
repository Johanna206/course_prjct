# Project Description

### tarot deck CSV 
Contains a list of 78 cards and their suits, file names, values, etc. Used to load the deck. There are 5 suits in tarot: wands, pentacles, swords, cups, and major arcana.

### three card spread py
Draws 3 cards 'randomly' from the deck. 

### three card spread display py
Draws 3 cards randomly from the deck. Contains an interface for displaying the cards and allowing the user to click on them in order. 

### font folder
Contains the two fonts used in the card spread display and in the solitaire display.

### processed folder
Contains 78 images of tarot cards plus 1 image of the back of the deck which were renamed and resized (200x 333px) for use with pygames displays.

### WS Tarot scans 
Contains unprocessed images of several decks, I'm using the oldest version.

### solitaire py
Contains the logic for a game similar to "Aces Up" solitaire. The goal of the game is to discard 73 cards (all the cards except for the highest of each suit). You start by dealing cards from the draw pile onto the 5 tableau piles. Any top card may be discarded when there is another card of the same suit but higher value available. Any top card may be moved to another pile if it is empty. Player may choose to deal another row of top cards at any time. The game is won when 73 cards have been discarded, leaving the king of each suit and 'the world' as the only remaining cards in the tableau. 

### solitaire display py
Contains the display for the game. According to wikipedia, "aces up" is only winnable 1/43 times so I also added a 'score' corresponding to the number of cards discarded. Even if you do not win, you can try for a high score. 

### matching display
Contains a matching game (aka memory) where you click to reveal cards and try to match up the pairs of cards in the fewest flips. The fewest number of flips possible is 10 (one for each card). This game was created using a class Cards which contains ten random object cards drawn from the tarot dect of 78 possible cards. 