import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    coloumns = [[], [], []]
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
            bet = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Bet must be between $", MIN_BET, "and $", MAX_BET)
        else:
            print("Bet must be a number.")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print("You don't have enough money to place that bet., you only have $", balance)
        else:
            break
        
    print(
        f"You have bet $", bet, "on", lines, "lines. Your total bet is $",
    )
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    
main()