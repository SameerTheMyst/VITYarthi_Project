# This file is responsible for keeping track of the scores of the player and the computer in the game.

# Initializing the scores for both player and computer
player_score = 0
computer_score = 0

# Writing the function to update the score after every win or loss
def update_score(result):
    global player_score, computer_score

    if result == "You Win!":
        player_score += 1
    elif result == "Computer Wins!":
        computer_score += 1

# Writing the function for the total score till a certain number of games
def get_score():
    return f"Score: You {player_score} - {computer_score} Computer"