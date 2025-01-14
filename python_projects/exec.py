def factorial(fact=None):
    if fact is None:
        fact = int(input("Enter number: "))
    if fact == 0:
        return 1
    return fact * factorial(fact - 1)