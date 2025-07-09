import math

### Arithmetic Operators in Python
# This code snippet demonstrates the use of arithmetic operators in Python.
# Arithmetic operators are used to perform mathematical operations on numbers.

"""
a = 10
b = 5
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
print(f"Addition: {c}, Subtraction: {d}, Multiplication: {e}, Division: {f}, Modulus: {g}")
# Output: Addition: 15, Subtraction: 5, Multiplication: 50, Division: 2.0, Modulus: 0

"""

"""
x = 3.14
y = -4
z = 5

# result = round(x)
# result = abs(y)
# result = pow(z , 2)
# result = max(x, y, z)
# result = min(x, y, z)
result = int(math.sqrt(z))
print(result)

"""

# Calculate the area of a circle using user input
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * 2
print(f"The area of the circle is: {area}")