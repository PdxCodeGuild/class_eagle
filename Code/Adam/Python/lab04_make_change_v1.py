

# Lab 4: Make Change
# Convert a dollar amount into a number of coins. The input will be the total 
# amount, the output will be the number of quarters, dimes, nickles, and 
# pennies. Always break the total into the highest coin value first, resulting 
# in the fewest amount of coins.

dollar_amount = float(input('Enter a dollar amount: '))
# dollar_amount = 4.35 # for testing

total_pennies = round(dollar_amount*100, 4)
# print(total_pennies)

quarters = int(total_pennies//25)
dimes = int(total_pennies%25//10)
nickels = int(total_pennies%25%10//5)
pennies = int(total_pennies%25%10%5/1)

print(f'The dollar amount was: {dollar_amount}')
print(f'Quarters: {quarters}')
print(f'Dimes: {dimes}')
print(f'Nickels: {nickels}')
print(f'Pennies: {pennies}')