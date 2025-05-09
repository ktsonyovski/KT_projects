"""This file is to contain all the functions
defined during training exercises"""

def greet(name="World", upper=False):
    """A simple greeting function"""
    greetings = print(f"Hello, {name}")
    if upper:
        print(greetings).upper()
    else:
        print(greetings)

def factorial(x):
    """Factorial function"""
    if x == 0:
        x = 1
    else :
        x = x * factorial(x-1)
