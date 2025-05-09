"""This is a third day challenge of 
100 days 100 projects python udemy course"""

#Initiate welcoming message
print("Welcome to Treasure Island\nYour mission is to find the treasure.")

#Cross roads
cross_roads = str(input("You are at a crossroads, Please give direction either 'Left' or 'Right' ")).lower()

if cross_roads not in ["left", "right"]:
    print("Invalid input! Please provide either 'Left' or 'Right' - ")
elif cross_roads == "left":
        print(f"\nYou chose to go {cross_roads} which lead you to a lake. There is an island in the middle of the lake.")
        island_approach = str(input("How would you approach it?\nWait for a boat or swim across? ")).lower()
        if island_approach not in ['wait', 'swim']:
              print("Invalid input! Please provide either 'Wait' or 'Swim' - ")
        elif island_approach == 'wait':
              print(f"\nYou chose to go {island_approach}. A boat appeared and you safely arrived at the island.")
              doors = str(input("On the island there are three caves marked with colour. Which one will you go into? \nRed, Green or Blue - ")).lower()
              if doors not in ['red', 'green', 'blue']:
                    print("Invalid input! Please provide either 'Red', 'Green' or 'Blue' - ")
              elif doors in ['green', 'blue']:
                    print("\nYou fell in a hole neven to be seen again. Game over!")
              else:
                    print("\nFound the treasure!")
        elif island_approach == "swim":
            print("\nThe water was too cold and you backed out. Game over!")
else:
      print("\nYou went back to where you came from. Game over!")