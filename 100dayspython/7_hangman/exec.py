import resources
import random

difficulty_setting = str(input("Choose difficulty: ")).lower()

if difficulty_setting in resources.words_dictionary:
    word_choice = random.choice(resources.words_dictionary[difficulty_setting])
    word_lenght = len(word_choice)
    placeholder = "_ " * word_lenght
    lives = word_lenght
    print(f"{placeholder} ;\n {word_lenght} letters in total ; {lives} tries total")

    end = False
    save_letters = []


    while not end:
        display = ""
        user_choice = str(input("Type letter: "))
        for char in word_choice:
            if char == user_choice:
                display += char
                save_letters.append(char)
            elif char in save_letters:
                display += char                
            else:
                display += "_ "
        
        print(display)

        if user_choice not in word_choice:
            lives -= 1
            print(f"{lives} lives remaining!")
            if lives == 0:
                print("\nLost! End.")
                end = True
        
        if "_" not in display:
            end = True
            print("\nWin! End.")
