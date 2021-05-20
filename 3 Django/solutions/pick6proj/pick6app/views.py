from django.shortcuts import render

from django.http import HttpResponse

import random


def pick6():
    nums = []
    for i in range(6):
        nums.append(random.randint(1, 99))
    return nums

def play_pick6(balance, tickets):
    winning_ticket = pick6()
    for i in range(tickets):
        balance -= 2
        purchased_ticket = pick6()
        num_matches = 0
        for j in range(len(winning_ticket)):
            if winning_ticket[j] == purchased_ticket[j]:
                num_matches += 1
        payouts = [0, 4, 7, 100, 50000, 1000000, 25000000]
        balance += payouts[num_matches]
    return balance




def index(request):
    print(request.method)
    print(request.POST)
    if request.method == 'GET':
        context = {
            'title': 'Pick 6'
        }
        return render(request, 'pick6app/index.html', context)
    else:
        # print(dict(request.POST))
        # print(dict(request.POST)['balance'][0])
        # print(request.POST['balance'])
        balance = request.POST['balance']
        tickets = request.POST['tickets']
        balance = float(balance)
        tickets = int(tickets)

        ending_balance = play_pick6(balance, tickets)

        context = {
            'title': 'Pick 6',
            'ending_balance': ending_balance,
            'money_lost': balance - ending_balance
        }
        return render(request, 'pick6app/index.html', context)

