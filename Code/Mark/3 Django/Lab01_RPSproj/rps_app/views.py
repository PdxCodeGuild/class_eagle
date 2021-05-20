from django.shortcuts import render
from django.http import HttpResponse
from random import *


def rock_paper_scissors(user, computer):
    if user == computer:
        return 'tie'
    elif user == "rock":
        if computer == "paper":
            return 'lose'
        elif computer == "scissors":
            return 'win'
        elif computer == "spock":
            return 'lose'
        elif computer == "lizard":
            return 'win'
    elif user == "scissors":
        if computer == "rock":
            return 'lose'
        elif computer == "paper":
            return 'win'
        elif computer == "spock":
            return 'lose'
        elif computer == "lizard":
            return 'win'
    elif user == "paper":
        if computer == "rock":
            return 'win'
        elif computer == "scissors":
            return 'lose'
        elif computer == "spock":
            return 'win'
        elif computer == "lizard":
            return 'lose'
    elif user == "spock":
        if computer == "rock":
            return 'win'
        elif computer == "scissors":
            return 'win'
        elif computer == "paper":
            return 'lose'
        elif computer == "lizard":
            return 'lose'
    elif user == 'lizard':
        if computer == "rock":
            return 'lose'
        elif computer == "scissors":
            return 'lose'
        elif computer == "paper":
            return 'win'
        elif computer == "spock":
            return 'win'




def index(request):
    if request.method == 'POST':
        rps = ['rock','paper','scissors','lizard','spock']
        computer = choice(rps)
        user_choice = request.POST['user_choice']
        result = rock_paper_scissors(user_choice, computer)
        context = {
            'title':'Rock Paper Scissors Lizard Spock',
            'result': result,
            'user_choice' : user_choice,
            'computer' : computer,
        }
        return render(request, 'rps_app/index.html', context) 
    else:    
        context = {
            'title':'Rock Paper Scissors Lizard Spock'
        }
        return render(request, 'rps_app/index.html', context) 