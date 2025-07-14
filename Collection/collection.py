# Collection = single "variable" that holds multiple values
# Collection = list, tuple, set, dictionary
#   # List = [] ordered, mutable, allows duplicates
#   # Tuple = () ordered, immutable, allows duplicates
#   # Set = {} unordered, mutable, no duplicates
#   # Dictionary = key-value pairs, unordered, mutable



"""
### List !

fruits_list = ["apple", "banana", "cherry" , "coconut"]

print(dir(fruits_list))  # Show all methods and attributes of the list
print(help(fruits_list))  # Show help documentation for the list




print(len(fruits_list))  # Get the number of items in the list
for fruit in fruits_list:
    print(fruit)
print("apple" in fruits_list)  # Check if "apple" is in the list
fruits_list.append("orange")  # Add "orange" to the end of the list
fruits_list.insert(1, "kiwi")  # Insert "kiwi" at index
fruits_list.remove("banana")  # Remove "banana" from the list
fruits_list.pop()  # Remove the last item from the list
fruits_list.reverse()  # Reverse the order of the list
fruits_list.sort()  # Sort the list in ascending order
fruits_list.index("cherry")  # Get the index of "cherry" in the list
fruits_list.count("apple")  # Count how many times "apple" appears in the list
# fruits_list.clear()  # Remove all items from the list

# print(fruits)

"""









"""
### Set !
fruits_set = {"apple", "banana", "cherry", "coconut"}
fruits_set.add("orange")  # Add "orange" to the set
fruits_set.remove("banana")  # Remove "banana" from the set

fruits_set.clear()  # Remove all items from the set

print(fruits_set)

"""








#### Tuple !

fruits_tuple = ("apple", "apple", "banana", "cherry", "coconut")
print(fruits_tuple[0])  # Access the first item in the tuple
print(fruits_tuple[1:3])  # Access a slice of the tuple
print(fruits_tuple.index("cherry"))  # Get the index of "cherry" in the tuple
print(fruits_tuple.count("apple"))  # Count how many times "apple" appears in

for fruit in fruits_tuple:
    print(fruit)


# print(fruits_tuple)