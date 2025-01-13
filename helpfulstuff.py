import numpy as np
from typing import List, Dict, Tuple, Any
import datetime

#this file will just be composed of helpful python things to help me learn/remember the syntax

print("Helo worl")



#String stuff
name = "Jacob"
string1 = f"he said his name is {name}"
length = len(string1)

#input from console, returns data as string
inputstring = input("Enter some data: ")

"yay!" if 0 > 1 else "nay!"

list = []
# .append, .pop, .insert, .index, .extend(other list)
# li[-1] to look at last, 
# list[1:3], list[2:], list[:3], list[::2], list[::-1], del list[1]

tuple = (1, 2)
#like lists but immutable, can do most of list operations on tuples as well
a, b, c = (1, 2, 3)

dict = {"one": 1, "two" : 2}
#basically maps from java
#keys must be immutable data types (cant be lists, can be tuples)
#.keys, .values, .get (use to check for existence of a key), .setdefault, .del, 

some_var = 5
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:    # This elif clause is optional.
    print("some_var is smaller than 10.")
else:                  # This is optional too.
    print("some_var is indeed 10.")

for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))

for i in range(4):
    print(i)

for i in range(4, 8):
    print(i)

animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)

x = 0
while x < 4:
    print(x)
    x += 1

# Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Refrain from this, provide a recovery (next example).
except (TypeError, NameError):
    pass                 # Multiple exceptions can be processed jointly.
else:                    # Optional clause to the try/except block. Must follow
                         # all except blocks.
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 # Execute under all circumstances
    print("We can clean up resources here")

# Instead of try/finally to cleanup resources you can use a with statement
with open("myfile.txt") as f:
    for line in f:
        print(line)

# Writing to a file
contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w") as file:
    file.write(str(contents))        # writes a string to a file

import json
with open("myfile2.txt", "w") as file:
    file.write(json.dumps(contents))  # writes an object to a file

# Reading from a file
with open("myfile1.txt") as file:
    contents = file.read()           # reads a string from a file
print(contents)
# print: {"aa": 12, "bb": 21}

with open("myfile2.txt", "r") as file:
    contents = json.load(file)       # reads a json object from a file
print(contents)
# print: {"aa": 12, "bb": 21}

# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement

# You can define functions that take a variable number of
# positional arguments
def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1, 2, 3)

# You can define functions that take a variable number of
# keyword arguments, as well
def keyword_args(**kwargs):
    return kwargs

# Let's call it to see what happens
keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}