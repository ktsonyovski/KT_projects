fact = int(input("Enter number: "))
def factorial(fact):
    if fact == 0:
        return 1
    return fact * factorial(fact - 1)

print(factorial(fact))