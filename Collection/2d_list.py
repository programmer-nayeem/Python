# 2D List Example


"""
groceries_list = [
    ["apple", "banana", "cherry", "coconut"],
    ["carrot", "broccoli", "spinach"],
    ["chicken", "beef", "pork"]
]




groceries_tuple = (
    ("apple", "banana", "cherry", "coconut"),
    ("carrot", "broccoli", "spinach"),
    ("chicken", "beef", "pork")
)

for collection in groceries_tuple:  # Print each sublist
    for item in collection:
        print(item , end = ", ")
    print()  # New line after each sublist

"""





num_pad = (    (1, 2, 3),
               (4, 5, 6),
               (7, 8, 9),
               ("*", 0, "#")
)

for row in num_pad:  # Print each row of the num pad
    for num in row:
        print(num, end=" ")
    print()  # New line after each row
