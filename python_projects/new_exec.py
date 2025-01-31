# # Data types
# a = 10
# b = 3.14
# c = "Hello"
# d = [1,2,3]
# e = {"key":"value"}
# # print(type(a), type(b), type(c), type(d), type(e))

# # Type casting
# a = "123"
# # print(int(a) + 10)

# a_list = [1, 2, 3]
# string_list = str(a_list)
# # print(type(a_list))
# # print(type(string_list))

# # Shallow deep copies
# import copy
# original = [[1, 2], [3, 4]]
# shallow = copy.copy(original)
# deep = copy.deepcopy(original)

# deep[0][1] = 22
# original[0][1] = 4
# shallow[0][1] = 45
# # print(f"{original} - {shallow} - {deep}")


# # String slicing
# nice_slice = "Hello Python!"
# the_real = nice_slice[6:-1:3]
# # print(f"{nice_slice} - {the_real}")

# # List comprehension
# squares = [x**2 for x in range(10)]
# # print(squares)

# # List of even numbers from 1 to 20
# order_even_list = [x for x in range(21)]
# even_list = []
# for i in order_even_list:
#     if i % 2 == 0:
#         even_list.append(i)

# # print(order_even_list)
# # print(even_list)

# # Generate a list of tuples (x, x**2) for numbers from 1 to 5.
# list_of_typles = [(x, x**2) for x in range(1,6)]
# # print(list_of_typles)

# # Create a dictionary with keys as numbers from 1 to 5 and values as their squares.
# dict_list = {x:x**2 for x in range(1,6)}
# # print(dict_list[3])
# # print(dict_list)

# # Context Manager
# # with open("example.txt", "w") as file:
# #     file.write("HII\nNew HII")

# # Connection to database
# # import sqlite3
# # conn = sqlite3.connect('example.db')
# # c = conn.cursor()
# # c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
# # conn.commit()
# # conn.close()

# # fruits = ['apple', 'banana', 'cherry']
# # for fruit in enumerate(fruits):
#     # print(fruit)

# # F-strings 
# name = "Kayo"
# years = 27.77882
# # print(f"My name is {name} and I am {years:.1f} years old.")

# import math
# a = 16
# b = int(math.sqrt(a))
# # print(f"Square root of {a} is {b}")

# # import exec
# # result = exec.factorial()
# # print(result)


# # Reverse a string
# def string_reverser(string: str) -> str:
#     if not isinstance(string, str):
#         raise ValueError("Type is not a string")
#     reversed_string = string[::-1]
#     return reversed_string

# def isstringpalidrome(string: str) -> str:
#     if not isinstance(string, str):
#         raise ValueError("Type is not a string")
#     lastIndex = len(string)-1
#     line = len(string)//2
#     for index in range(0, line):
#         if string[index] == string[lastIndex-index]:
#             return True
#     return False

# def long_substring(string):

#     size = len(string)
#     head = 0
#     tail = 0
#     # Substrings are not explicitly stored but is kept by this head and tail pointer
#     chars = dict()      # HashMap in Python
 
#     max_len = 1
#     s = 0       # Starting index of the resultant substring
#     e = 0       # Ending Index of the resultant substring
#     # Both inclusive

#     for tail in range(size):
#         if string[tail] in chars:
#             # Current tail character already present inside HashMap
#             if chars[string[tail]] >= head:
#                 # All characters between head and tail is inside current substring
#                 # If the character inside HashMap is after head index, then it is inside this current substring
#                 # Hence, the current tail is a duplicate character, reduce the substring
#                 head = chars[string[tail]] + 1

#         chars[string[tail]] = max(chars.get(string[tail], 0), tail)

#         if max_len < (tail - head + 1):
#             s = head
#             e = tail
#             max_len = e - s + 1

#     result_string = string[s : e+1]
#     return result_string

# def palidrome(given_string: str):
#     last_index = len(given_string)-1
#     print(last_index)
#     line = len(given_string)//2
#     print(line)
#     for index in range(line):
#         if given_string[index] == given_string[last_index]:
#             return print("This is a palidrome")
#     return print("This is a NOT palidrome")

# pal = input("Give string: ")
# palidrome(pal)

# def isstringpalidrome(string: str) -> str:
#     if not isinstance(string, str):
#         raise ValueError("Type is not a string")
#     lastIndex = len(string)-1
#     line = len(string)//2
#     for index in range(0, line):
#         if string[index] == string[lastIndex-index]:
#             return True
#     return False


# def reversed_string(string):
#     rev_string = ''
#     for char in string:
#         rev_string = char + rev_string
#     return rev_string

# print(reversed_string("Hello World!"))

# def anagrams(s1, s2):
#     if sorted(s1.lower()) == sorted(s2.lower()):
#         return True
#     return False

# print(anagrams("listen", "silent"))