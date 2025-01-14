# Data types
a = 10
b = 3.14
c = "Hello"
d = [1,2,3]
e = {"key":"value"}
# print(type(a), type(b), type(c), type(d), type(e))

# Type casting
a = "123"
# print(int(a) + 10)

a_list = [1, 2, 3]
string_list = str(a_list)
# print(type(a_list))
# print(type(string_list))

# Shallow deep copies
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

deep[0][1] = 22
original[0][1] = 4
shallow[0][1] = 45
# print(f"{original} - {shallow} - {deep}")


# String slicing
nice_slice = "Hello Python!"
the_real = nice_slice[6:-1:3]
# print(f"{nice_slice} - {the_real}")

# List comprehension
squares = [x**2 for x in range(10)]
# print(squares)

# List of even numbers from 1 to 20
order_even_list = [x for x in range(21)]
even_list = []
for i in order_even_list:
    if i % 2 == 0:
        even_list.append(i)

# print(order_even_list)
# print(even_list)

# Generate a list of tuples (x, x**2) for numbers from 1 to 5.
list_of_typles = [(x, x**2) for x in range(1,6)]
# print(list_of_typles)

# Create a dictionary with keys as numbers from 1 to 5 and values as their squares.
dict_list = {x:x**2 for x in range(1,6)}
# print(dict_list[3])
# print(dict_list)

# Context Manager
# with open("example.txt", "w") as file:
#     file.write("HII\nNew HII")

# Connection to database
# import sqlite3
# conn = sqlite3.connect('example.db')
# c = conn.cursor()
# c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
# conn.commit()
# conn.close()

# fruits = ['apple', 'banana', 'cherry']
# for fruit in enumerate(fruits):
    # print(fruit)

# F-strings 
name = "Kayo"
years = 27.77882
# print(f"My name is {name} and I am {years:.1f} years old.")

import math
a = 16
b = int(math.sqrt(a))
# print(f"Square root of {a} is {b}")

import exec
result = exec.factorial()
print(result)
