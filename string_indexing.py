### Indexing strings in Python
# This code snippet demonstrates how to index strings in Python.

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # First character

print(credit_number[0:4])  # First four characters

print(credit_number[5:9])  # Second group of four characters

print(credit_number[5:]) # From the sixth character to the end

print(credit_number[-1])  # Last character

print(credit_number[::3]) # Every second character


last_four_digits = credit_number[-4:]  # Last four characters
print(f"Last four digits: {last_four_digits}")


credit_number = credit_number[::-1]  # Reverse the string
print(f"Reversed credit number: {credit_number}")