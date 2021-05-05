


def make_change():
    # Enter input 
    amount = input('Enter a Dollar Amount for Change ')
    amount = int(float(amount)*100)

    # Calculate quarters 
    quarters = amount // 25
    print(f'{quarters} Quarter(s)') 
    quarters = float(quarters)

    # Calculate dimes
    amount -= quarters * 25
    dimes = amount // 10
    print(f'{dimes} Dime(s)')
    dimes = float(dimes)

    # Calculate nickels
    amount -= dimes * 10
    nickels = amount // 5
    print(f'{nickels} Nickels(s)')
    nickels = float(nickels)

    # Calculate pennies
    amount -= nickels * 5
    pennies = amount // 1
    print(f'{pennies} Pennie(s)')
    pennies = float(pennies)

#REPL
     
run_again = 'y'
while run_again == 'y':
    make_change()
    run_again = input('Would you like to make some more change? y/n ')
    if run_again != 'y':
        print('Goodbye!')















