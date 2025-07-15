# Python Function = A block of reusable code 
#                   Place first bracket/() after the function name to invoke it


# def happy_birthday(name , age):
#     print(f"Happy birth day {name}!")
#     print(f"You are {age} years old !")
#     print(f"Happy birthday to you {name}!")
#     print()

# happy_birthday("Cloud" , 18)


# def display_invoice(user_name , amount , due_date):
#     print(f"Hello {user_name}" , end= " ")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Cloud Code", 42.50 ,"01/01" )







# Return = Statement used to end a function
#          and send a result back to the caller

# def add(x , y):
#     z = x + y
#     return z

# def subtract(x , y):
#     z = x - y
#     return z

# def multiply(x , y):
#     z = x * y
#     return z

# def devide(x , y):
#     z = x / y
#     return z

# print(add(5,10))
# print(subtract(5, 10))
# print(multiply(5 , 5))
# print(devide(10 , 5))



def create_name(frist , last):
    frist = frist.capitalize()
    last = last.capitalize()
    return frist + ' ' + last

full_name = create_name("cloud" , "code")
print(full_name)