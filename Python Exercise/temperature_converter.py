### Python Temperature Converter
# This code snippet converts temperature between Celsius and Fahrenheit.

temp = float(input("Enter temperature: "))
unit = input("Celsius (C) or Fahrenheit (F)? ").strip().upper()

if unit == "C":
    converted = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {converted:.2f}°F")
elif unit == "F":
    converted = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {converted:.2f}°C")
else:
    print("Invalid unit")
