"""Rock paper scissors game with random computer"""

from random import choice

outcomes_dict = {
    ("rock","paper"): "lose",
    ("rock", "scissors"): "win",
    ("rock","rock"): "draw",
    ("paper","rock"): "win",
    ("paper","scissors"): "lose",
    ("paper","paper"): "draw",
    ("scissors","rock"): "lose",
    ("scissors","paper"): "win",
    ("scissors","scissors"): "draw"
}

options = ["rock", "paper", "scissors"]

print("This is a rock, paper, scissors game. What do you choose")
user_input = str(input()).lower()

if user_input not in options:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    computer_input = choice(options)
    print(f"\nYou chose: {user_input}\nComputer chose: {computer_input}")
    result = outcomes_dict[(user_input, computer_input)]
    print(f"You {result}!")

