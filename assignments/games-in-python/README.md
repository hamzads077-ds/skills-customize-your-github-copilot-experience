
# 📘 Assignment: Games in Python

## 🎯 Objective

Practice string manipulation, loops, conditionals, user input, and random
selection by building a playable Hangman game.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description

Create the initial game state for a Hangman game. The program should
randomly choose a secret word from a predefined list and prepare the
variables needed to track the player's progress.

#### Requirements

Completed program should:

- Store several possible words in a list.
- Randomly select one word using Python's `random` module.
- Track the letters the player has guessed.
- Set a maximum number of incorrect guesses.

### 🛠️ Build the Game Loop

#### Description

Add a game loop that accepts letter guesses, reveals the correctly guessed
letters, and ends with an appropriate result.

#### Requirements

Completed program should:

- Display the current progress using underscores for unguessed letters.
- Ask the player for one letter at a time and update the game state.
- Track and display the number of incorrect guesses remaining.
- End when the player reveals the whole word or runs out of attempts.
- Display an encouraging win message or a clear game-over message.
