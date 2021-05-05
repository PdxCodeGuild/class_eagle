
######################## LAB 8 ########################
# PICK 6
# 

import random

# Randomly pick 6 numbers between 1 and 99
def pick6():
    nums = range(1,99)
    ticket = []
    for i in range(6):
        ticket.append(random.choice(nums))
    return ticket

# Given 2 lists of numbers return the number of matching numbers
def matches(winner,ticket):
    matching_nums = 0
    for i in range(len(winner)):
        if winner[i] == ticket[i]:
            matching_nums += 1
    return matching_nums


# Initialize Version 1: loop 100000 times and print the final balance.
winning_ticket = pick6() # These are the winning numbers for this instance
balance = 0
for i in range(100000):
    my_ticket = pick6() # for each iteration a new ticket is created
    balance -= 2 # Each ticket costs 2 dollars
    matching_nums = matches(winning_ticket,my_ticket) # New ticket is compared to winning ticket.

    # Balance increases depending on number of matches
    if matching_nums == 1:
        balance += 4
    elif matching_nums == 2:
        balance += 7
    elif matching_nums == 3:
        balance += 100
    elif matching_nums == 4:
        balance += 50000
    elif matching_nums == 5:
        balance += 1000000
    elif matching_nums == 6:
        balance += 25000000



#### Version 2 ####

# Simple arithmetic to figure out roi
roi = (balance - i)/i

# Output
print(f'For any given 100000 lottery tickets, you will earn {balance} and your ROI is {roi}')

