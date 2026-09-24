# This file contains the core game logic for the Rock-Paper-Scissors game, including functions to determine the computer's choice and the result of each round.

# Importing required libraries
import random
from Settings import CHOICES

# For computer to generate a random choice
def get_computer_choice():
    return random.choice(CHOICES)

# The Core Game design logic to determine the result of the game based on the choices made by the player and the computer
def get_result(player, computer):
    if player == computer:
        return "It's a Draw!"
    elif player == "Rock" and computer == "Scissors":
        return "You Win!"
    elif player == "Paper" and computer == "Rock":
        return "You Win!"
    elif player == "Scissors" and computer == "Paper":
        return "You Win!"
    else:
        return "Computer Wins!"