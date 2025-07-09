### Python Logical Operators
# This code snippet demonstrates the use of logical operators in Python.

a = True
b = False

# Logical AND
if a and b:
    print("Both are True")
else:
    print("At least one is False")

# Logical OR
if a or b:
    print("At least one is True")
else:
    print("Both are False")

# Logical NOT
if not a:
    print("a is False")
else:
    print("a is True")







# temp = 25
# is_raining = False

# if temp > 30 or temp < 15 or is_raining:
#     print("It's either too hot, too cold, or raining.")

# if not (temp > 30 or temp < 15 or is_raining):
#     print("The weather is just fine.")

temp = -32
is_sunny = True
if temp >= 30 and is_sunny:
    print("It's a hot and sunny day 🥵")
    print("Is it sunny ☀️")
elif temp <= 0 and is_sunny:
    print("It is cold outside 🥶")
    print("Is it sunny ☀️")










"""

# Logical XOR (exclusive or)
if a != b:
    print("a and b are different")
else:
    print("a and b are the same")
# Logical NAND (not and)
if not (a and b):
    print("At least one is False (NAND)")
else:
    print("Both are True (NAND)")
# Logical NOR (not or)
if not (a or b):
    print("Both are False (NOR)")
else:
    print("At least one is True (NOR)")
# Logical XNOR (not exclusive or)
if not (a != b):
    print("a and b are the same (XNOR)")
else:
    print("a and b are different (XNOR)")
# Logical implication
if not a or b:
    print("Implication holds")
else:
    print("Implication does not hold")
# Logical biconditional
if a == b:
    print("Biconditional holds")
else:
    print("Biconditional does not hold")
# Short-circuit evaluation
if a and (b or True):
    print("Short-circuit evaluation: a is True, b is ignored")
# Short-circuit evaluation with OR
if a or (b and False):
    print("Short-circuit evaluation: a is True, b is ignored")
else:
    print("Short-circuit evaluation: a is False, b is ignored")


# Chained logical operators

"""