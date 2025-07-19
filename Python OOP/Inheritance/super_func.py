# super() = Function used in a child to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self , color , is_filled):
        self.color = color
        self.is_filled = is_filled


class Circle(Shape):
    def __init__(self , color , is_filled , radius):
        super().__init__(color , is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self , color , is_filled , width):
        super().__init__(color , is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self , color , is_filled , width , height):
        super().__init__(color , is_filled)
        self.width = width
        self.height = height


circle = Circle(color="red" , is_filled=True , radius=5)
square = Square(color="red" , is_filled= True , width=5)
triangle = Triangle(color="red" , is_filled= True , width= 7 , height= 8)


print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")