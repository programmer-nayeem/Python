# Args      = allows you to pass multiple non-key arguments
# Key args  = allows you to pass multiple keyword-arguments
#           * unpacking operator
#           1. postional , 2. default , 3. keyword , 4. ARBITRARY



# def add(*args):
#     total = 0 
#     for arg in args:
#         total += arg
#     return total
# print(add(2 , 4 , 5))



# def display_name(*args):
#     for arg in args:
#         print(arg , end=" ")
# display_name("Cloud" , "Code")






# def print_address(**keyargs):
#     for key , value in keyargs.items():
#         print(f"{key}: {value}")

# print_address(
#     capital="Dhaka" , 
#     zila="Faridpur" , 
#     Upazila = "Saltha" , 
#     Zip = "7801"
# )



def shipping_label(*args , **keyargs):
    for name in args:
        print(name , end=" ")
    print()
    for address in keyargs.values():
        print(address)

shipping_label(
    "Cloud" , "Code",
    Capital= "Dhaka",
    City = "Faridpur"
)