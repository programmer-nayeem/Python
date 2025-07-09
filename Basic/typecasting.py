### Typecasting in Python
# Typecasting allows you to convert one data type to another.
# This is useful when you need to perform operations that require specific data types.
## Example of typecasting from string to integer
age_str = "18"
age = int(age_str)
print(age)

# Example of typecasting from integer to string
number = 42
number_str = str(number)
print(number_str)

# Example of typecasting from string to float
height_str = "1.75"
height = float(height_str)
print(height)

# Example of typecasting from float to string
height_str = str(height)
print(height_str)

# Example of typecasting from string to boolean
is_student_str = "True"
is_student = bool(is_student_str)
print(is_student)

# Example of typecasting from boolean to string
is_student_str = str(is_student)
print(is_student_str)

# Example of typecasting from list to string
hobbies = ["reading", "gaming", "cooking"]
hobbies_str = ", ".join(hobbies)
print(hobbies_str)

# Example of typecasting from string to list
hobbies_str = "reading, gaming, cooking"
hobbies = hobbies_str.split(", ")
print(hobbies)
