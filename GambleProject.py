#Project Begin
#Git Test
import random
MAX_LINES = 3
MAX_COLUMNS = 3
MAX_BALANCE = 200

symbols = {
    "A":5,
    "B":4,
    "C":3,
    "D":2,
    "E":1
}

def get_deposit():
    while True:
        balance = input("How much money do you want place on your account ?: $")

        if balance.isdigit():
            balance = int(balance)
            if balance <= 0 or balance > MAX_BALANCE:
                print(f"Your deposit must be between 1$ - {MAX_BALANCE}$.")
            else:
                print(f"Your balance is {balance}$")
                return balance
        else:
            print("Your entry is not valid!")

def get_lines():
    while True:
        lines = input("How many lines do you want to bet on? ")
        if lines.isdigit():
            lines = int(lines)
            if lines <= 0 or lines > MAX_LINES:
                print(f"the number of lines must between 1 - {MAX_LINES}.")
            else:
                return lines
        else:
            print("Your entry is not valid !")

def get_bet(balance, lines):
    while True:
        bet =input("How much do you want to bet on each line ?: $ ")
        if bet.isdigit():
            bet = int(bet)
            if bet <= 0:
                print("You must bet at least 1$.")
            elif bet * lines > balance:
                print("You don't have enough money on your account.")
            else:
                total_bet = lines * bet
                return bet ,balance - total_bet #return the new balance
        else:
            print("Your entry is not valid")


def picker(lines):
    #get all the columns symbols
    all_symbols = []
    for symbol, value in symbols.items():
        for _ in range(value):
            all_symbols.append(symbol)


    #for each column pick {lines} symbols
    picked_symbols = []
    for _ in range(MAX_COLUMNS):
        current_symbols = all_symbols[:]
        column_picked_symbol_list = []
        for _ in range(lines):
            column_picked_symbol_list.append(random.choice(current_symbols))
        picked_symbols.append(column_picked_symbol_list)

    for i in range(lines):
        for j in range(MAX_COLUMNS):
            if j < MAX_COLUMNS -1:
                print(f"{picked_symbols[j][i]}  ", end="|")
            else:
                print(f"{picked_symbols[j][i]} ")
    return picked_symbols

def check_winnings(balance,lines,bet,picked_symbols):
    winnings = 0
    for i in range(lines):
        picked_symbol = picked_symbols[0][i]
        for j in range(MAX_COLUMNS):
            if picked_symbols[j][i] != picked_symbol:
                break
        else:
            winnings += bet
    print(f"You won {winnings}$")
    return balance + winnings #return the new balance


def main():
    input("Press a Enter to play..")
    balance = get_deposit()
    while True:
        lines = get_lines()
        bet, balance = get_bet(balance, lines)
        check_winnings(balance,lines,bet,picker(lines))
        print(f"Your new balance is {balance}$")
        answer = input("Do you want to continue ? Y/n: ")
        if answer.lower() != "y" :
            if balance <= 0:
                print("Please, recharge your account!")
                balance = get_deposit()
            break

main()