# Dictionary  = A collection of {key:value} pairs
#               order and changeable . No duplicates 

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"
}


# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))



# if capitals.get("Germany"):
#     print("Germany is in the dictionary.")
# else:
#     print("Germany is not in the dictionary.")

# capitals.update({"USA": "Dhaka"})
# capitals.pop("China")
# capitals.popitem()


keys = capitals.keys()
values = capitals.values()


# for key in capitals.keys():
#     print(key)

# for value in capitals.values():
#     print(value)


# items = capitals.items()
# for key , value in capitals.items():
#     print(f"{key} : {value}")