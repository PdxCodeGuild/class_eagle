

# Lab 8: Pick 6
# Simulate playing this lottery game 100,000 times and compare cost to earnings.

import random


def pick6(): # function for choosing 6 random numbers
    six_numbers = []
    i = 0
    while i < 6:
        random_num = random.randint(1, 99)
        six_numbers.append(random_num)
        i += 1
    # returns a list of 6 random numbers between 1 and 99
    return six_numbers

# print(pick6()) # test

def num_of_matches(ticket_nums, winning_nums): # function for determing number of matches
    num_of_matches = 0
    for i in range(len(winning_nums)):
        if ticket_nums[i] == winning_nums[i]:
            num_of_matches += 1
    return num_of_matches

# test_winning_nums = [7, 60, 93, 92, 58, 66]
# test_tictet_nums = [30, 36, 21, 48, 58, 66]
# print(num_of_matches(test_tictet_nums, test_winning_nums)) # test

def matches_payout(matches):    # function that takes the number of matches and returns the payout.
    payout = 0
    list_of_payouts = [0, 4, 7, 100, 50000, 1000000, 25000000]
    payout = list_of_payouts[matches]
    return payout

# num_of_matches = 1
# print(payout(num_of_matches))

winning_nums = pick6()  # 1) pick 6 random numbers for the 'winning numbers'
balance = 0     # 2) start your balance at 0
payout = 0
matches = 0

for i in range(100000):     # 3) loop 100,000 times
    ticket_nums = pick6()   # 4) pick 6 random numbers for the ticket numssubtract 2 from your balance
    balance -= 2
    matches = num_of_matches(ticket_nums, winning_nums)     # 5) calculate how many matches there are between the ticket and the winning numbers
    payout += matches_payout(matches)    # 6) figure out the payout from the number of matches

# print(balance + payout)     # 7) add the payout to your balance


roi = round((payout + balance)/abs(balance)*100, 2)
expenses = "{:,}".format(abs(balance))
earnings = "{:,}".format(payout)

print('\nAfter playing Pick 6 100,000 times:')
print(f'\nTotal expenses: ${expenses}')
print(f'\nTotal earning: ${earnings}')
print(f'\nCalculated Return on Investment: {roi}%\n')

if roi > 0:
    print('You got real lucky!')
else:
    print("Moral: It's really not worth it.\n")