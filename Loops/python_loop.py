### Python all types of loops
# This code snippet demonstrates various types of loops in Python.


# name = input("Enter your name: ")

# while name == "":
#     print("Name cannot be empty. Please try again.")
#     name = input("Enter your name: ")

# print(f"Hello, {name}!")



# age = int(input("Enter your age: "))
# while age < 0:
#     print("Age cannot be negative. Please try again.")
#     age = int(input("Enter your age: "))
# print(f"Your age is {age} years old.")



# food = input("Enter your favorite food (q to quit): ")

# while not food == "q":
#     print(f"Your favorite food is {food}.")
#     food = input("Enter your favorite food (q to quit): ")# Python all types of loops
# print("Loop ended. Thank you!")




num = int(input("Enter a number (1-10): "))

while num < 1 or num > 10:
    print(f"{num} is not a valid number")
    num = int(input("Enter a number (1-10): "))
print(f"You entered a valid number: {num}")

















"""
# 1. For loop
for i in range(5):
    print(f"For loop iteration {i}")

# 2. While loop
count = 0
while count < 5:
    print(f"While loop iteration {count}")
    count += 1

# 3. Nested loop
for i in range(3):
    for j in range(2):
        print(f"Nested loop iteration {i}, {j}")
"""