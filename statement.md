Problem Statement

Problem Statement

The objective of this project is to develop a simple graphical Rock
Paper Scissors game using Python and Tkinter. A traditional command-line
version requires the user to enter choices through text, which can be
less convenient for a graphical application.

The proposed system provides buttons for selecting Rock, Paper, or
Scissors. After the player makes a selection, the computer randomly
chooses one of the three options. The program compares the two choices
according to the standard rules and displays the result. The application
also maintains the scores of the player and computer during the game.

Scope of the Project

The scope of this project is limited to a small desktop game that runs
locally on a computer.

The project includes: - A Tkinter-based graphical interface. - Three
choices: Rock, Paper, and Scissors. - Random computer selection. -
Result calculation. - Score tracking. - Multiple rounds in one
session. - Modular Python source files.

The project does not include: - Online multiplayer. - User accounts or
login. - Database storage. - Internet-based services. - Persistent match
history.

Target Users

The project is designed for: - Students learning Python programming. -
Beginners learning Tkinter GUI development. - Users who want to play a
simple desktop Rock Paper Scissors game. - Students demonstrating
modular and event-driven programming concepts.

High-Level Features

1. Graphical User Interface

The application provides a simple window containing buttons and labels
so that the player does not need to enter commands through a terminal.

2. Player Choice

The player can select Rock, Paper, or Scissors.

3. Computer Choice

The computer uses Python's random module to select one of the three
valid choices.

4. Result Calculation

The program compares both choices and determines whether the player
wins, the computer wins, or the round is a draw.

5. Score Tracking

The application maintains separate scores for the player and computer
and updates them after each winning round.

6. Multiple Rounds

The player can continue playing rounds without restarting the
application.

7. Modular Design

The project is divided into separate files so that the GUI, game logic,
score management, and settings are easier to maintain.

Project Modules

main.py
    ↓
gui.py
    ├── game_logic.py
    ├── score.py
    └── settings.py

This structure separates different responsibilities and makes the
project easier to understand and extend.
