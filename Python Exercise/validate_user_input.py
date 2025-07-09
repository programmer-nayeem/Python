### Validate User Input
# This script validates user input to ensure it meets specific criteria.
# username is no more than 12 characters long and contains only alphanumeric characters.
# password is at least 8 characters long and contains at least one uppercase letter, one lowercase
# letter, one digit, and one special character.
# If the input is valid, it prints a success message; otherwise, it prints an error message.


username = input("Enter a username : ")

if len(username) > 12 : 
    print("Username must be no more than 12 characters long.")
elif not username.find(" ") == -1:
    print("Username must not contain spaces.")
elif not username.isalnum():
    print("Username must contain numbers")
else:
    print(f"Wlcome {username}!")