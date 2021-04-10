

# Lab 4: Make Change
# convert a dollar amount into a number of coins. The input will be the total 
# amount, the output will be the number of quarters, dimes, nickles, and 
# pennies. Always break the total into the highest coin value first, resulting
#  in the fewest amount of coins.

# Version 2 - Instead of hard-coding the coins, store them in a list of tuples. 
# This way you can make custom coins.


coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

print(coins)