# Object = A 'bundle' of realted attributes (variables) and methods (functions)
#         Ex. phone , cup , book
#         You need a "class" to create many objects



# class = (blueprint) useed to design the staructure and layout of an object
from car import Car

car1 = Car("BMW" , 2024 , "red" , False)
car2 = Car("Corvette" , 2025 , "blue" , False)

print(car1.model)
print(car2.color)

car1.describe()