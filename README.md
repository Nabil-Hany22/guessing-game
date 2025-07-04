# 🎮 Guessing Game

A simple interactive Python game where the computer selects a random number between **1 and 10**, and the player tries to guess it.  
The game keeps track of the number of attempts and shows the **best score** so far (the lowest number of attempts).

## 👨‍💻 Features

- Random number generation
- Input validation (only numbers from 1 to 10)
- Tracks number of attempts per round
- Displays high score (minimum number of attempts)
- Option to play again without restarting the program
- Personalized with player’s name

## 📁 Files

- `guessing game.py`: Main version of the game.
- `guessing game_chatgpt.py`: Enhanced version with ChatGPT suggestions.
- `guessing-game-planning.jpg`: Initial planning or sketch for the game.

## 📁 Files Description

- `guessing game.py`:  
  A classic number guessing game where:
  - The number is between 1 and 10.
  - The player is asked whether they want to play.
  - The program keeps track of how many attempts the player takes.
  - It stores and displays the **best score across rounds**.
  - Simple logic with clear structure — great for learning Python basics and input validation.

- `guessing game_chatgpt.py`:  
  A more **feature-rich** version of the guessing game with:
  - 🎯 **Difficulty selection**: Easy (1–5), Medium (1–10), Hard (1–50)
  - 🎲 **Round counter** that displays the round number (e.g., `Round 2`)
  - 🏅 **High score saved per player name** instead of one global best
  - 💬 **Motivational feedback** based on performance (e.g., “Wow, you're a genius!” if guessed on first try)
  - Encourages better coding structure using functions and reusable logic

> Both versions serve different purposes:
> - `guessing game.py` is simpler and great for beginners.  
> - `guessing game_chatgpt.py` is more advanced, showing how to scale and improve features while keeping the code organized.


## 🚀 How to Run

Make sure you have Python installed, then open a terminal or command prompt and run:

```bash
python "guessing game.py"
Or for the enhanced version:
python "guessing game_chatgpt.py"
```
