# List comprehension = A concise way to create lists in python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]




# doubles = [x * 2 for x in range(1 , 11)]

# print(doubles)


# fruits = [fruit.upper() for fruit in ["apple" , "orange" , "banana"]]
# fruit_chars = [fruit[0] for fruit in ["apple" , "banana"]]

# print(fruit_chars)


numbers = [1 , -2 , -3 , -4 , 5 , 6]
positive_nums = [num for num in numbers if num >= 0]

print(positive_nums)