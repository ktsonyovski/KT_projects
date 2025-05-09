import random

list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_of_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+','[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/','~','`']

num_of_letters = int(input("Letters: "))
num_of_numbers = int(input("Numbers: "))
num_of_symbols = int(input("Symbols: "))


pw_list = []

for letter in range(0, num_of_letters):
    random_letter = random.choice(list_of_letters)
    pw_list += random_letter

for number in range(0, num_of_numbers):
    random_number = random.choice(list_of_numbers)
    pw_list += random_number

for symbol in range(0, num_of_symbols):
    random_symbol = random.choice(list_of_symbols)
    pw_list += random_symbol

random.shuffle(pw_list)
formatted_list = ''.join(pw_list)

print(f"Password with {num_of_letters} letters, {num_of_numbers} numbers and {num_of_symbols} symbols!\n{formatted_list}")