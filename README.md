# shuffle_poker_game

This is a web application to play the poker shuffle game. It is a game played in solitaire (single player) with standard playing cards (52 cards). The game consists of drawing 25 cards one at a time and placing them in a 5 by 5 grid to form poker hands in 5 rows and 5 columns.

Each poker hand (one pair, two pair, full house, etc.) has a corresponding number of points. The player must try to maximize the total score, ie the sum of the points for the 5 rows and 5 columns. When the player places the 25th card, the game ends and the program displays the final score then restarts a new game. Before the end of the game the player can move the cards on the grid. He can also start a new game by clicking on a button.


A poker hand is a group of 5 cards. Here are the different poker hands and the associated score, in descending order of score:

(100 points) Royal Flush: The ace, king, queen, jack and 10 of the same suit (all clubs, all spades, all diamonds, or all hearts).
(75 points) Straight Flush: Five consecutive cards of the same suit (for example 7, 8, 9, 10 and jack, all clubs, all spades, all diamonds, or all hearts).
(50 points) Square: Four cards of the same value (for example four jacks).
(25 points) Full House: Three cards of the same value and a pair of cards of the same value (eg three aces and two 9s).
(20 points) Flush or Flush: All cards of the same suit (all clubs, all spades, all diamonds, or all hearts).
(15 points) Straight: Five consecutive cards (eg 8, 9, 10, Jack and Queen). It should be noted that the ace can be the beginning or the end of the sequence.
(10 points) Brelan: Three cards of the same value (for example three kings).
(5 points) Double Pair: A pair of cards of the same value and another pair of cards of the same value (eg two kings and two 7s).
(2 points) A Pair: A pair of cards of the same value (eg two aces).
