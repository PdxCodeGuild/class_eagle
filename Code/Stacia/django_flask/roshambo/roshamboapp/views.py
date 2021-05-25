from django.http import HttpResponse
from django.shortcuts import render
import random

def index(request):
    
    if request.method =="GET":
        return render(request,"rpsapp/index.html",{})
    
weapons = ["sheild", "mace", "arrow"]

def roshambo(atack, comp):
 
    if atack == comp:
        match ="Draw"
    elif atack == "mace" and  "sheild" == comp:
        match = "Victory"
    elif atack == "sheild" and "arrow" == comp:
        match = "Victory"
    elif atack == "arrow" and "mace" == comp: 
        match = "Victory"
    else:
        match = "Defeat"
    return match

        
def index(request):
    print(request.POST)
    if request.method =="GET":
        return render(request,"roshamboapp/index.html",{})
    
    
    if request.method == "POST":
        atack = request.POST["attack"]
        comp =  random.choice(weapons)
        context = {
            "match":roshambo(atack,comp),
            "comp" : comp,
            "atack" : atack,
        } 
        
        print (context) 

        return render(request,"roshamboapp/index.html",context)  
    # context