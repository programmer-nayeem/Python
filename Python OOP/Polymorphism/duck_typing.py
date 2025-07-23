# Duck Typing = Another way to achive polymorphism besides Inheritance
#               Object must have the minimum necessary attributes/methods
#               "If it looks like duck and puacks like a duck , it must be a duck"


class Animal :
    alive = True


class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

animals = [Dog() , Cat()]

for animal in animals:
    animal.speak()
    print(animal.alive)