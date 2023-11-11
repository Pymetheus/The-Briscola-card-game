# The Briscola Card Game

![Briscola Card Game](briscola.png)

Introducing a Python implementation of the classic Italian trick-taking card game, Briscola, where you can now challenge your skills against a computer opponent. Immerse yourself in the world of strategy and excitement as you strive to secure valuable cards and execute winning moves, all while competing against a computer adversary that will put your gaming abilities to the test. Whether you're a seasoned player or new to the game, this Python Briscola experience offers engaging and entertaining game play for hours of fun and challenge.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [How to Play](#how-to-play)
- [Game Rules](#game-rules)
  - [Setup](#setup)
  - [Gameplay](#gameplay)
- [Contributing](#contributing)
- [License](#license)

## Features

- Implements the Briscola card game in Python.
- Supports an intelligent computer-controlled opponent.
- Simple command-line interface for playing the game.

## Requirements

- Python 3.x

## Getting Started

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/briscola-card-game.git
    ```

2. Change into the project directory:

    ```bash
    cd briscola-card-game
    ```

### How to Play

1. Start the game by running `main.py`:

    ```bash
    python main.py
    ```

2. Follow the on-screen instructions to select the trump card and play the game.

3. Enjoy playing Briscola!

## Game Rules

### Setup

- The game is played with a standard Italian deck of 40 cards.
- The traditional Italian deck consists of four suits: Swords, Cups, Coins, and Sticks.
- Each suit has ten cards, given from highest to lowest: Ace, three, king, queen, jack, 7, 6, 5, 4, 2.

  | Name   | Points   |
  | ------ | -------- |
  | Ace    | 11 points |
  | Three  | 10 points |
  | King   | 4 points  |
  | Queen  | 3 points  |
  | Jack   | 2 points  |

### Gameplay

- Each player is dealt a hand of three cards.
- The starting player selects one suit as the "trump" suit, which ranks higher than other suits for the rest of the game.
- Players take turns playing a card, and the player with the higher-ranking card in the same suit wins the trick.
- If a player plays a trump card, it beats all other suits.
- The player who wins the trick leads the next trick.
- After all tricks have been played, players count the points they have captured in the tricks.
- A maximum of 120 points can be achieved.


![Flow Chart](res\flow-chart-gameplay.jpeg)


## Contributing

Contributions to this project are welcome! If you would like to contribute, please open an issue to discuss potential changes or submit a pull request.

## License

This project is licensed under the [MIT License](https://github.com/Pymetheus/The-Briscola-card-game/blob/update-main/src/LICENSE.md). You are free to use, modify, and distribute this code as permitted by the license.
