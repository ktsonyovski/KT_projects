import random
import resources

difficulty_setting = input("Choose difficulty: ")
if difficulty_setting in resources.words_dictionary:
    words_difficulty = random.choice(resources.words_dictionary[difficulty_setting])
    print(f"Word to guess is {len(words_difficulty)} # of letters.)\n {len(words_difficulty)* " _ "}")

    letter_to_guess = input("Guess a letter: ")
    if letter_to_guess in words_difficulty:
        print(words_difficulty)