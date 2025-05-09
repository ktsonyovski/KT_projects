"""This is a tip calculator for the second day challenge of 
100 days 100 projects python udemy course"""

#Initiate welcoming message
print("Welcome to the tip calculator!")

#Define variables as input provided by user
initial_bill = float(input("Total bill - $"))
tip_to_add = int(input("Tip to add - "))
split_people = int(input("People to contribute to the bill - "))

# Calculate total bill with tip
total_bill_with_tip = initial_bill + (initial_bill * (tip_to_add / 100))

# Split for each person
each_person_bill = round(total_bill_with_tip / split_people , 2)
print(f"Each person should pay: ${each_person_bill}")