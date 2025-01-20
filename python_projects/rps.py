def game_rsp():
    from random import choice
    outcomes_dictionary = { "rock": {"rock": "draw",
                "paper": "lose",
                "scissors": "win" },
            "paper": {"rock": "win",
                "paper": "draw",
                "scissors": "lose" },
            "scissors": {"rock": "lose",
                "paper": "win",
                "scissors": "draw" }                  
                }
    possible_choices = ["rock", "paper", "scissors"]
    game_continue = input("Type 'yes' to start! ")
    while game_continue in ["y", "yes"]:
        user_choice = str(input("What do you choose?: ")).lower()
        if not isinstance(user_choice, str):
            raise ValueError("Incorrect type of input.")
        elif user_choice not in possible_choices:
            print("Invalid choice, please choose rock/paper/scissors. ")
            continue
        
        computer_choice = choice(possible_choices)
        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        result = outcomes_dictionary[user_choice][computer_choice]
        
        if result == "win":
            print("You win!")
        elif result == "lose":
            print("You lost!")
        else:
            print("It's a draw!")       
        game_continue = str(input("Continue? ")).lower()
game_rsp()
