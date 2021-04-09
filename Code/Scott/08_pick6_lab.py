import random as rand
import math

user_bal = 0

def PickSix():
    output = [rand.randint(1, 99) for x in range(6)]
    return output

def Gamble():
    output = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1000000):
        matches = 0

        user_tick = PickSix()
        win_tick = PickSix()

        for j in range(len(user_tick)):
            if user_tick[j] == win_tick[j]:
                matches += 1

        if matches == 1:
            output[1] += 1
            output[7] += 4
        elif matches == 2:
            output[2] += 1 
            output[7] += 7 
        elif matches == 3:
            output[3] += 1
            output[7] += 100
        elif matches == 4:
            output[4] += 1
            output[7] += 50000
        elif matches == 5:
            output[5] += 1
            output[7] += 1000000
        elif matches == 6:
            output[6] += 1
            output[7] += 25000000
        else:
            output[0] += 1
        output[7] -= 2
        if matches >=0 :
            print(f'Your Ticket: {user_tick} | Winning Ticket: {win_tick} | Your profits: {output} | Rounds played: {i+1}')
        

    return output

# profit = Gamble()[7] - 2
# for i in range(100000):
#     profit += Gamble()[7] - 2
#    # print(f'Profit: {profit} | Rounds Played: {i+1}')
# print(profit)
Gamble()