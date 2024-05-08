import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(coloumns, lines, bets, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = coloumns[0][line]
        for coloumn in coloumns:
            symbol_to_check = coloumn[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bets
            winning_lines.append(line+1)
            
    return winnings, winning_lines
            
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    coloumns = []
    for _ in range(cols):
        coloumn = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbol.remove(value)
            coloumn.append(value)
        coloumns.append(coloumn)
    return coloumns

def print_slot_machine(coloumns):
    for row in range(len(coloumns[0])):
        for i, coloumn in enumerate(coloumns):
            if i != len(coloumns) - 1:
                print(coloumn[row], end=" | ")
            else:
                print(coloumn[row], end=" ")
                
        print()
    
def deposit():
    while True:
        amount = input("Enter the amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
                
        else:
            print("Amount must be a number")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be between 1 and", MAX_LINES)
        else:
            print("Amount must be a number.")
    return lines

def get_bet():
    while True:
        amount = input("Enter the amount to bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet must be between $ {MIN_BET}, and $ {MAX_BET}")
        else:
            print("Bet must be a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print("You don't have enough money to place that bet., you only have $", balance)
        else:
            break
        
    print(
        f"You are betting $ {bet}  on, {lines} lines. Your total bet is ${total_bet}.")
    
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_count)
    print (f"You won ${winnings}!")
    print(f"You won the following lines: ", *winning_lines)
    return winnings - total_bet
    
def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        answer = input("Press enter key to spin the slot machine, or q to quit: ")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"Your final balance is ${balance}")
    
main()