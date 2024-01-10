# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"

# STRATEGY
# Map out what beats what (dict? Or switch case? Or if/elif chain?)
# Return the result based on values p1 and p2 according to the map


def rps(p1, p2):
    winner_combos = {"scissors": "paper", "paper": "rock", "rock": "scissors"}
    if winner_combos.get(p1) == p2:
        return "Player 1 won!"
    elif winner_combos.get(p2) == p1:
        return "Player 2 won!"
    else:
        return "Draw!"


print(rps("scissors", "paper"))
print(rps("scissors", "rock"))
print(rps("paper", "paper"))
