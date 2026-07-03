import random

MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): # looping in every row
        symbol = columns[0][lines] # check the first symbol in the first column of the current row
        for column in columns: # now loop through every column
            symbol_to_check = column[line] # symbol to check is equal to check at the current row
            if symbol != symbol_to_check: # if not the same, we break line then go check the next line
                break
            else: 
                winnings += values[symbol] * bet # bet on each line, not the total bet
                winning_lines.append(line + 1)

    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols): # What symbols are going to be on each column based on the frequancy of symbols that we have above 
    # number of rows inside each column
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # symbol = "A", symbol_count = 2
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols): # If cols = 3, then this loop will run 3 times
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols) # once we pick a value, we need to remove it from the list of available symbols so that we don't pick it again
            current_symbols.remove(value) # find the first instant of this value from the list and get rid of it 
            column.append(value) #  add "value" to "column"

        columns.append(column)


    return columns

# transposing = matrix
def print_slot_machine(columns):
    for row in range(len(columns[0])): # determine number of rows(elements = verticle spaces) that we have based on our colums
        for i, column in enumerate (columns): # looping through all items that are inside "columns"
            if i != len(columns) - 1: # if we are not on the last column, then we want to print a "|" after the 
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")


        print() 


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")        
        else:
            print("Please enter a number greater than 0.")
    return amount


def get_number_of_lines():
     while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")        
        else:
            print("Please enter a number.")
     return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")        
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet




def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer =="q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()