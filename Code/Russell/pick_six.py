import random

def pick_6():
    count = 0
    my_nums = []
    while count < 6:
        my_nums.append(random.randint(1,99))
        count += 1
    return my_nums

def num_matches(ticket,winners):




    matches = 0
    for i in range(len(ticket)):
        if ticket[i] == winners[i]:
            matches += 1
    return matches


winner_list = pick_6()

def one_play(winner_list):
    payout = 0
    ticket_gen = pick_6()
    payout_level = num_matches(ticket_gen, winner_list)
    if payout_level == 6:
        payout += 25000000
    elif payout_level == 5:
        payout += 1000000
    elif payout_level == 4:
        payout += 50000
    elif payout_level == 3:
        payout += 100
    elif payout_level == 2:
        payout += 7
    elif payout_level == 1:
        payout += 4
    else:
        payout = 0
    return payout    


total = 0

for i in range(100000):
    total -= 2
    winnings = one_play(winner_list)
    total += winnings 


print(total)




