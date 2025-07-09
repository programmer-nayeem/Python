# Collection = single "variable" that holds multiple values
# Collection = list, tuple, set, dictionary
#   # List = [] ordered, mutable, allows duplicates
#   # Tuple = () ordered, immutable, allows duplicates
#   # Set = {} unordered, mutable, no duplicates
#   # Dictionary = key-value pairs, unordered, mutable




### List !

fruits = ["apple", "banana", "cherry" , "coconut"]

print(dir(fruits))  # Show all methods and attributes of the list
print(help(fruits))  # Show help documentation for the list




print(len(fruits))  # Get the number of items in the list
for fruit in fruits:
    print(fruit)
print("apple" in fruits)  # Check if "apple" is in the list
fruits.append("orange")  # Add "orange" to the end of the list
fruits.insert(1, "kiwi")  # Insert "kiwi" at index
fruits.remove("banana")  # Remove "banana" from the list
fruits.pop()  # Remove the last item from the list
fruits.reverse()  # Reverse the order of the list
fruits.sort()  # Sort the list in ascending order
fruits.index("cherry")  # Get the index of "cherry" in the list
fruits.count("apple")  # Count how many times "apple" appears in the list
# fruits.clear()  # Remove all items from the list

# print(fruits)






### Set !
