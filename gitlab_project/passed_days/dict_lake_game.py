"""This is a third day challenge of 
100 days 100 projects python udemy course"""

#Initiate welcoming message
print("Welcome to Treasure Island\nYour mission is to find the treasure.")

outcomes_dict = {
      ("left", "wait", "red"): "You found the treasure!",
      ("left", "wait", "blue"): "The cave got flooded with water.\nGame over!",
      ("left", "wait", "green"): "An earthquake trapped you in the cave.\nSnakes appear!\nGame over!",
}

# Function to validate input and lower it
def valid_input_checker(user_input:str,valid_input:list):
    while True:
        user = input(user_input).lower()
        if user in valid_input:
            return user
        else:
            print("Invalid input!")
        

#Cross roads main body
cross_roads = valid_input_checker("You are at a crossroads, Please give direction either 'Left' or 'Right' ", ["left", "right"])
if cross_roads == "right":
    print(f"You fell in a trap by choosing {cross_roads}! Game Over.")
else:
    print(f"\nYou chose to go {cross_roads} which lead you to a lake. There is an island in the middle of the lake.")
    island_approach = valid_input_checker("How would you approach it?\nWait for a boat or swim across? ", ["wait", "swim"])
    if island_approach == "swim":
        print(f"You chose to {island_approach}!\nThe water was too cold and you swam back to safety.\nGame over!")    
    else:
        print(f"\nYou chose to {island_approach}. A boat appeared and you safely arrived at the island.")
        doors = valid_input_checker("On the island there are three caves marked with colour. Which one will you go into? \nRed, Green or Blue - ", ["red", "green", "blue"])
        if doors:
            result = outcomes_dict[(cross_roads, island_approach, doors)]
            print(result)
