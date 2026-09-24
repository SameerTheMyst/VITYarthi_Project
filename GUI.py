# Importing every required library from the pre-existing files
import tkinter as tk
from Settings import TITLE, WINDOW_SIZE
from Game_Logic import get_computer_choice, get_result
from Score import update_score, get_score

# Writing the function for the game logic
def play(player_choice):
    computer_choice = get_computer_choice()
    result = get_result(player_choice, computer_choice)

    player_label.config(text="You: " + player_choice)
    computer_label.config(text="Computer: " + computer_choice)
    result_label.config(text=result)

    update_score(result)
    score_label.config(text=get_score())

# Creating the main window for the game
root = tk.Tk()
root.title(TITLE)
root.geometry(WINDOW_SIZE)
root.resizable(False, False)

title = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Bahnschrift", 24, "bold")
)
title.pack(pady=25)

# To show the choices of player and computer
player_label = tk.Label(root, text="You: ", font=("Bahnschrift", 16))
player_label.pack(pady=10)

computer_label = tk.Label(root, text="Computer: ", font=("Bahnschrift", 16))
computer_label.pack(pady=10)

# Displaying the result of the current game
result_label = tk.Label(
    root,
    text="Choose your move!",
    font=("Bahnschrift", 20, "bold")
)
result_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=40)

# Creating Buttons for user interaction
tk.Button(
    button_frame,
    text="Rock",
    font=("Bahnschrift", 16),
    width=10,
    command=lambda: play("Rock")
).grid(row=0, column=0, padx=8)

tk.Button(
    button_frame,
    text="Paper",
    font=("Bahnschrift", 16),
    width=10,
    command=lambda: play("Paper")
).grid(row=0, column=1, padx=8)

tk.Button(
    button_frame,
    text="Scissors",
    font=("Bahnschrift", 16),
    width=10,
    command=lambda: play("Scissors")
).grid(row=0, column=2, padx=8)

# Showing the total score till a certain number of games
score_label = tk.Label(
    root,
    text=get_score(),
    font=("Bahnschrift", 16, "bold")
)
score_label.pack(pady=30)