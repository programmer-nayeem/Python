# keyword argument = an argument preceded by a identifier
#                    helps with readability
#                    order of argument dosen't matter
#                    1. Positional , 2. Default , 3. KYEWORD , 4. Arbitrary


# def hello(greeting , title , first , last):
#     print(f"{greeting} {title} {first} {last}")

# hello("Hello," , title="Mr." , last="Code" , first="Cloud")



def get_phone(country_code , area , fist , last):
    return f"{country_code}-{area}-{fist}-{last}"

phone_num = get_phone(country_code="+880", area="17" , fist="8293" , last="7584")
print(phone_num)