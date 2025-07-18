# Python Slot Machine
import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row , bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0


def main():
    balane = 100

    print("************************")
    print("Welcome to python slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("************************")


    while balane > 0:
        print(f"Current balance : ${balane}")

        bet = input("Place your beat amount :")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balane:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must me greater than 0")
            continue

        balane -= bet

        row = spin_row()
        print("Spnning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0 :
            print(f"You won {payout}!")
        else:
            print("Sorry you lost this round!")

        balane += payout

        play_again = input("Do you want to spin again ? (y/n): ")
        
        if play_again != 'y':
            break
        
    print(f"Game over ! Your final balance is ${balane}")



if __name__ == '__main__':
    main()