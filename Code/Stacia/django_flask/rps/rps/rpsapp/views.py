from django.http import HttpResponse
from django.shortcuts import render
import random

comp_list = ["Rock", "Paper", "Scissors"]
def choose_winner(users_choice, comp_choice):
    output = ''
    if users_choice == comp_choice:
        output='It\'s a Draw! \n'
    elif users_choice == 'Rock' and comp_choice != 'Paper':
        output='You Win! \n'
    elif users_choice == 'Paper' and comp_choice != 'Scissors':
        output='You Win! \n'
    elif users_choice == 'Scissors' and comp_choice != 'Rock':
        output='You Win! \n'
    else:
        output='You Lose! \n'
    return output

# Create your views here
def index(request):
    print(request.POST)
    if request.method =="GET":
        return render(request,"rpsapp/index.html",{})
    # print (rpsapp/index.html)
    
    if request.method == "POST":
        users_choice = request.POST["choice"]
        comp_choice =  random.choice(comp_list)
        context= {
            "winner":choose_winner(users_choice, comp_choice),
            "comp_choice" : comp_choice,
            "users_choice" : users_choice,

        }  
        return render(request,"rpsapp/index.html",context)  
    # context
    
        
     

