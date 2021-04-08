

# Enter input 
amount = input('Enter a Dollar Amount for Change ')
amount = int(float(amount)*100)

# Calculate quarters 
quarters = amount // 25
quarters = str(quarters)
print(f'{quarters} Quarter(s)') 
quarters = float(quarters)

# Calculate dimes
amount -= quarters * 25
dimes = amount // 10
dimes = str(dimes)
print(f'{dimes} Dime(s)')
dimes = float(dimes)

# Calculate nickels
amount -= dimes * 10
nickels = amount // 5
nickels = str(nickels)
print(f'{nickels} Nickels(s)')
nickels = float(nickels)

# Calculate pennies
amount -= nickels * 5
pennies = amount // 1
pennies = str(pennies)
print(f'{pennies} Pennie(s)')
pennies = float(pennies)

    














