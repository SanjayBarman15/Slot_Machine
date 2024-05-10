import random

# Slot machine game
MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Symbols and payouts
symbol_count = {
    "A": 2, 
    "B": 4,
    "C": 6,
    "D": 8,  
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,  
}

# Check for winning lines and calculate payout
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        
        # Check if symbol matches across all columns
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        
        # If all symbols match, it's a winner    
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    
    # Return total winnings and winning lines
    return winnings,winnings_lines        

# Generate slot machine columns with random symbols
def get_slot_machine(rows, cols,symbols):
    # Create list of all symbols
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    # Initialize empty columns
    columns = []
    # Populate each column with random symbols
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            # Get random symbol
            value = random.choice(current_symbols)
            # Remove symbol from list to avoid duplicates
            current_symbols.remove(value) 
            # Add symbol to column
            column.append(value)
        
        # Add column to columns
        columns.append(column)
      
    # Return the generated slot machine columns
    return columns


# Print the slot machine columns  
def print_slot_machine(columns):
# Loop through each row
    for row in range(len(columns[0])):
# Loop through each column
        for i, column in enumerate(columns):
# Print column value  
            if i != len(columns) - 1:
               print(column[row],end =" | ") 
            else:
                print(column[row], end ="")
# Print new line after each row                 
        print()


# Get deposit amount from player  
def deposit():
    while True:
        amount = input("What is the amount you want to deposit?$ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be grater than 0")
        else:
            print("please enter a number")
    return amount

# Get number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "):?  ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines") 
        else:
            print("please enter a number")
    return lines

# Get player's bet per line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a number")
    return amount

# Spin slot machine
def spin(balance):
    # Get number of lines from player
    lines = get_number_of_lines()
    
    # Get player's bet per line
    while True:
        bet = get_bet()
        
        # Calculate total bet
        total_bet = lines * bet
        
        # Check if total bet exceeds balance
        if total_bet > balance:
            print(f"you don't have enough to bet on that amount, your current balance is ${balance}")
        else:
            break
        
    # Print bet details  
    print(f"you are betting ${bet} on {lines} lines.Total bet is equal to ${total_bet}")

    # Generate slot machine
    slots = get_slot_machine(ROWS, COLS, symbol_count)
    
    # Print slot machine
    print_slot_machine(slots)
    
    # Check for winning lines
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    
    # Print winnings  
    print(f"you won ${winnings}.")
    print(f"you won on lines:",*winnings_lines)
    
    # Return net winnings
    return winnings - total_bet

# Main game loop
def main():
    balance = deposit()
    while True:
        print(f"your current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
       
    print(f"you left with ${balance}")

main()