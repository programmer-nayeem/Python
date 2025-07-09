# Python compund interest calculator

principle = 0;
rate = 0;
time = 0;

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cannot be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("Rate cannot be less than or equal to zero")

while time <= 0:
    time = float(input("Enter the time (in years): "))
    if time <= 0:
        print("Time cannot be less than or equal to zero")

total_amount = principle * pow((1 + rate / 100), time)
print(f"The total amount after {time} years is: {total_amount:.2f}")