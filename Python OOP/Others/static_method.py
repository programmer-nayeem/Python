# Static Methods = A method that belong to be a class rather than any object from that class(Instance)
#                  Usually used for general utlity function


class Employee:
    def __init__(self , name , positon):
        self.name = name
        self.position = positon

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager" , "Cashier" , "Cook" , "Janitor"]
        return position in valid_positions
    
employee1 = Employee("Cloud" , "Programmer")
    

print(Employee.is_valid_position("Cook"))
print(employee1.get_info())