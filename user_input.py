### User Input in python 
# This code snippet demonstrates how to take user input in Python
# using the input() function and then print a message incorporating that input.
"""
name = input("what is your name? : ")
age = input("How old are you? : ")
print(f"Hello {name}! Are you really {age} years old?")

"""

"""
length = input("Enter the length of the rectangle: ")
width = input("Enter the width of the rectangle: ")
area = float(length) * float(width)
print(f"The area of the rectangle is: {area}cm²")
"""

item = input("What item would you like to buy? ")
price = float(input(f"What is the price of {item}? "))
quantity = int(input(f"How many {item}s would you like to buy? "))
total_cost = price * quantity
print(f"The total cost for {quantity} {item}s is: {total_cost} currency units.")
