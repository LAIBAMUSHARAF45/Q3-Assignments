# Special Keywords 
# Keywords are the reserved words in Python. We cannot use a keyword as a variable name, function name or any other identifier. They are used to define the syntax and structure of the Python language. In Python, keywords are case sensitive. 
# async, await, if, elif, else, True, False, None, try, except, finally, 
# raise, global, nonlocal,import, from, for, while, break, continue,and, or, not

# async, await:

import asyncio

async def fetch_data():
    print("Starting data retrieval process...")
    await asyncio.sleep(2)
    print("Data has been successfully retrieved.")

async def main():
    await fetch_data()

asyncio.run(main())


age = 25

if age < 20:
    print("Underage")
elif age >= 18 and age < 60:
    print("Adult")
else:
    print("Senior Citizen")

# True, False, None:

x = True
y = False
z = None

#  check using booleans
if x:
    print("a is True")

if not y:
    print("b is False")

# Using None to represent an absence of value
if z is None:
    print("c has no value (None)")

# try, except, finally, raise:
# using raise

def check_value(value):
    if value < 0:
        raise ValueError("Value must be non-negative")
    return value

try:
    check_value(-5)
except ValueError as a:
    print(a)  

# for, while, break, continue:

fruits = ["apple", "grapes", "cherry"]

for fruit in fruits:
    if fruit == "apple":
        continue  # Skip "banana"
    print(fruit)

count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break  

# and, or, not:

y = True
x = False

print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False


# Here's the some examples of keywords are used in python.





