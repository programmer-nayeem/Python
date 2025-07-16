# Module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# import math
# import math as cloud
# from math import pi
# from math import e


# a , b , c , d  = 1 , 2 , 3 , 4

# print(e ** a)
# print(e ** b)
# print(e ** c)
# print(e ** d)



import own_module 

result = own_module.pi
result = own_module.square(3)
result = own_module.cube(3)
result = own_module.circumference(3)
result = own_module.area(3)

print(result)