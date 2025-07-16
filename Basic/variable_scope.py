# Variable scope = where a variable is visible and accessable
# Scope Resulation = (LEGB) Local => Enclosed => Global => Built-in

# def func1():
#     x = 1
#     print(x)

# def func2():
#     x = 2
#     print(x)

# func1()
# func2()



x = 3
def func1():
    print(x)

def func2():
    print(x)

func1()
func2()