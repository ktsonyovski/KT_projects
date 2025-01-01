print("Welcome to the Band Name Generator.")
pet_name = input("What's your pet's name?\n")
city_name = input("What's the name of the city you grew up in?\n")
print(f"Your band name could be {city_name} {pet_name}")

sum = len(city_name) + len(pet_name)
# print(f"The lenght of the characters is: {sum}")
print("The lenght of the characters is: " + str(len(city_name) + len(pet_name)))