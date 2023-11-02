# The Briscola Card Game
Briscola is a captivating Italian trick-taking card game that masterfully blends strategy, skill, and heart-pounding competition, offering an exhilarating and challenging gaming experience for those seeking an exciting pastime.


## **About**
Introducing a Python implementation of the classic Italian card game, Briscola, where you can now challenge your skills against a computer opponent. Immerse yourself in the world of strategy and excitement as you strive to secure valuable cards and execute winning moves, all while competing against a computer adversary that will put your gaming abilities to the test. Whether you're a seasoned player or new to the game, this Python Briscola experience offers engaging and entertaining gameplay for hours of fun and challenge.


## **Rules**
### Objective:
The objective of Briscola is to earn points by winning tricks and capturing specific cards.

### Setup:
The traditional Italian deck consists of four suits:
-Swords
-Cups
-Coins
-Sticks

Each suit has ten cards, given from highest to lowest:
Ace, three, king, queen, jack, 7, 6, 5, 4, 2.

Also, the cards have a point value:

| Name | Points |
| ----------- | ----------- |
| Ace 	| 11 points |
| Three 	| 10 points |
| King 	| 4 points |
| Queen 	| 3 points |
| Jack 	| 2 points |

A maximum of 120 can be achieved.

### Gameplay:

The cards are shuffled, and each player receives three cards.

The starting player is choosing a trump card.



![alt text](/flow-chart-briscola_v1.jpg)

The goal of each trick is to capture the highest-value card in the trick, as determined by a specific ranking of the cards. The ranking is as follows, from highest to lowest:
    3 points: The highest-ranked card is the "Briscola," which is the card of the same suit as the face-up card in the discard pile.
    10 points: The King.
    9 points: The Horse (Cavallo).
    8 points: The Jack (Fante).
    7 points: All other numbered cards.
    1 point: The lowest-ranked card is the 7.

Players must follow suit, playing a card of the same suit as the leading card if they have one. If they don't have a card of the same suit, they can play any other card.

The player who wins the trick leads the next trick.

After all the tricks have been played, players count the points they have captured in the tricks.

In addition to the card points, there are additional points available for "scoperte" (capturing specific combinations of cards, such as the highest-value card from each suit). These combinations vary by region and house rules.

Winning:
The game is typically played to a specific point total, such as 21 or 31 points. The first player or team to reach this total wins the game.

Variations:
There are many regional variations of Briscola, and the rules may differ slightly depending on where it is played. Some variations include different scoring systems, the use of wild cards, and different point thresholds for winning.

Briscola is a classic and strategic Italian card game that combines skill, strategy, and a bit of luck, making it a beloved pastime for players of all ages.
