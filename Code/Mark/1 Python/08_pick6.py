from random import *

# returns a list of 6 random numbers between 1 and 99
def pick6(num_list):
    num_list = []
    for i in range(6):
        num_list.append(randint(1,99))
    return num_list


# determines the amount of matches
def num_matches(win_nums,ticket):
    matches = 0
    for i in range(0,len(win_nums)):
        if win_nums[i] == ticket[i]:
            matches += 1
    return matches


# creating the blank variables and lists
user_balance = 0
total_earnings = 0
expense = 0
ticket = []
win_nums = []

# Loop to determine to amount won
for i in range(100000):
    # each loop user balance will go down 2 and expense up 2
    user_balance -=2
    expense += 2

    # calling and sending data to the function
    ticket = pick6(ticket)
    win_nums = pick6(win_nums)
    matches = num_matches(win_nums,ticket)

    # if's and elif's to determine the amount of money per match
    if matches == 0:
        continue
    elif matches == 1:
        user_balance += 4
        total_earnings += 4
    elif matches == 2:
        user_balance += 7
        total_earnings += 7
    elif matches == 3:
        user_balance += 100
        total_earnings += 100
    elif matches == 4:
        user_balance += 50000
        total_earnings += 50000
    elif matches == 5:
        user_balance += 1000000
        total_earnings += 1000000
    elif matches == 6:
        user_balance += 25000000
        total_earnings += 25000000

# determining the return on investment
roi = (total_earnings-expense)/expense

# displaying the results to the user
print(f'Total expense: $ {expense}')
print(f'Total earnings: $ {total_earnings}')
print(f'Current balance: $ {user_balance}')
print(f'Your return on investment is {roi}')




