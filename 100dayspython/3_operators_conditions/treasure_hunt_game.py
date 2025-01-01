print("Welcome to Treasure Island.\n Your mission is to find the treasure!")
cross_road = str(input("You're at a crossroad. Where do you want to go? 'left' or 'right'?: "))
if cross_road == "left":
    way_to_island = str(input(("You come to  a lake. There is an island in the middle of the lake. Will you 'wait' for the boat or try and 'swim'?: ")))
    if way_to_island == "wait":
        house_with_doors = str(input("You arrive at the island unharmed. There is a house with 3 doors - 'red', 'yellow' and 'blue'. Which one you choose?: "))
        if house_with_doors == "red":
            print("It's a room full of fire. Game over!")
        elif house_with_doors == 'yellow':
            print("It's a room full of sand. No treasure in sight. Game over!")
        else:
            print("Treasure box found but it is empty. Game Over!")
    else:
        house_with_doors = str(input("You arrive at the island with minor injuries. There is a house with 3 doors - 'red', 'yellow' and 'blue'. Which one you choose?: "))
        if house_with_doors == "red":
            print("It's a room full of fire. Game over!")
        elif house_with_doors == 'yellow':
            print("It's a room full of sand. No treasure in sight. Game over!")
        else:
            print("Treasure box found! You found the treasure!")
else:
    castle_door = str(input(("You come to  a Castle. There is a lock on the doors. Will you try the 'lock' or find 'another way' inside?: ")))
    if castle_door == "lock":
        print("You trigger the alarm and security arrives. Game over!")
    else:
        another_way = str(input("There is a 'window' and a ladder to climb to it. You can also use the ladder to climb the 'wall'. What do you choose?: "))
        if another_way == "window":
            print("There is an alarm on the window and security came. Game over!")
        else:
            print("You got to the castle and found the treasure box on top of the wall. You found the treasure!")