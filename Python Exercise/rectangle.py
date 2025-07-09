### Rectangle using nested loops

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):
    for y in range(cols):
        print(symbol, end=" ")
    print()