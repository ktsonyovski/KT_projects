# print(2**3)
# print(5//3)
# print(round(5/3))
# print(round((5/3), 2))
# print("Number of letters in your name: " + str(len(input("Enter your name: "))))
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = round((weight / height ** 2), 2)
print(f"Your BMI is: {bmi}")