import random
options_computer = ["rock", "paper", "scissors"]
computer_choice = random.choice(options_computer)
user_choice = str(input("Welcome to the rock, paper, scissors game. \nPlease provide your choice: ")).lower()

if user_choice == computer_choice:
    print(f"You chose {user_choice}.\nThe computer chose {computer_choice}\nIt's a draw!")
elif (user_choice == "rock" and computer_choice == "paper") or (user_choice == "scissors" and computer_choice == "rock") or (user_choice == "paper" and computer_choice == "scissors"):
    print(f"You chose {user_choice}.\nThe computer chose {computer_choice}\nYou lose!")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
    print(f"You chose {user_choice}.\nThe computer chose {computer_choice}\nYou win!")        
else:
    print("Incorrect input, try again!")  