# Membership operators = used to test weather a value or variable is found in a sequence
#                        (string , list , tuple , set or dictionary)
#                        1. in
#                        2. not in



# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")


# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")






# students = {"Nayeem" , "Lamim" , "Fahim"}

# student = input("Enter the name of a student: ")

# if student in students:
#     print(f"{student} founded !")
# else:
#     print(f"{student} not found !")







# gpa = {"Nayeem": 3.94 , "Lamim": 4.22 , "Fahim": 5.00}

# student = input("Enter the name of a student: ")

# if student in gpa:
#     print(f"{student}'s gpa is {gpa[student]}")
# else:
#     print(f"{student} was not found !")





email = input("Enter your email: ")

if "@" in email and "." in email:
    print("Valid email !")
else:
    print("Invalid email !")