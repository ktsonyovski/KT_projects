print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? : "))
tip = int(input("How much tip would you like to add? : "))
people = int(input("How many people to split the bill? : "))
bill_with_tip = total_bill + ((total_bill * tip) /100)
split_bill = round((bill_with_tip / people), 2)
print(f"Bill with tip is: ${bill_with_tip}")
print(f"Each person should pay: ${split_bill}")