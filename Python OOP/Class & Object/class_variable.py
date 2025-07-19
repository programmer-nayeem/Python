# class variables = shared among all instance of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created form that class

class Student:

    class_year = 2025
    num_students = 0


    def __init__(self , name , age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Cloud" , 18)
student2 = Student("Code" , 19)


print(f"My graduating class of {Student.class_year} has {Student.num_students} students !")
print(student1.name)
print(student2.name)