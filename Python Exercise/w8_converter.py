# Python Weight Converter
# This code snippet converts weight from pounds to kilograms and vice versa.

weight = float(input("Enter weight: "))
unit = input("Kilograms (K) or Pounds (P)? ").strip().upper()

if unit == "K":
    converted = weight * 2.20462
    print(f"{weight} kg is equal to {converted:.2f} lbs")
elif unit == "P":
    converted = weight / 2.20462
    print(f"{weight} lbs is equal to {converted:.2f} kg")
else:
    print("Invalid unit")