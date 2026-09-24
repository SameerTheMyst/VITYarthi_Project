Rock Paper Scissors Game

Project Title

Rock Paper Scissors -- Python Tkinter GUI Game

Overview

This project is a simple desktop version of the Rock Paper Scissors game
developed using Python and Tkinter. The player selects Rock, Paper, or
Scissors using the graphical interface, while the computer generates its
choice randomly. The program compares both choices, displays the result,
and keeps track of the score.

The project is divided into multiple Python files to keep the code
organized and easier to understand.

Features

Graphical user interface using Tkinter

Rock, Paper, and Scissors buttons

Random computer choice

Automatic result calculation

Player and computer score tracking

Displays the choices made by both sides

Supports multiple rounds

Modular project structure using five Python files

Technologies / Tools Used

Programming Language: Python 3

GUI Library: Tkinter

Python Module: random

Development Tools: VS Code / IDLE / PyCharm

Version Control: Git and GitHub

Project Structure

RockPaperScissors/
├── main.py
├── gui.py
├── game_logic.py
├── score.py
└── settings.py

File Description

File                                Purpose

main.py                           Starts the Tkinter application and
main event loop.

gui.py                            Creates the GUI and handles button
interaction.

game_logic.py                     Generates the computer choice and
determines the result.

score.py                          Maintains and updates the scores.

Installation and Running

1. Install Python

Install Python 3 if it is not already installed.

2. Get the project

Clone the GitHub repository or download the project files.

3. Open the project folder

Make sure all five .py files are in the same folder.

4. Run the project

Open a terminal in the project folder and run:

python main.py

If required, use:

python3 main.py

How to Play

Start the application.

Click Rock, Paper, or Scissors.

The computer randomly selects its move.

The program displays both choices.

The winner of the round is displayed.

The score is updated automatically.

Continue clicking the buttons to play more rounds.

Game Rules

Rock beats Scissors.

Scissors beats Paper.

Paper beats Rock.

Equal choices result in a draw.

Testing Instructions

Player        Computer      Expected Result

Rock          Scissors      Player wins
Rock          Paper         Computer wins
Paper         Rock          Player wins
Paper         Scissors      Computer wins
Scissors      Paper         Player wins
Scissors      Rock          Computer wins
Same choice   Same choice   Draw

Also verify that the application opens correctly, all three buttons
work, the choices are displayed correctly, the score changes after a
win, the score remains unchanged after a draw, and multiple rounds can
be played.

Screenshots

Screenshots of the working application can be added here after running
the project.

Future Improvements

Add a Reset Score button.

Add images or icons for the three choices.

Add sound effects.

Add best-of-3 or best-of-5 mode.

Add match statistics.

Add a two-player mode.

Add a customized GUI theme.

Conclusion

This project demonstrates Python functions, modules, conditional
statements, random selection, and Tkinter event handling to create a
small interactive desktop application.
