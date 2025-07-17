def say_hello():
    print("Hello from greetings.py!")

print("This line is always printed.")

if __name__ == "__main__":
    print("greetings.py is being run directly")
    say_hello()
else:
    print("greetings.py is being imported")
