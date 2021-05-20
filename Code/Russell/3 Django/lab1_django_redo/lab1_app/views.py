from django.http import HttpResponse
from django.shortcuts import render
import string 
import random

def index(request):
    print(request.POST)
    if request.method == "POST":
        length = request.POST['length']
        length = int(length)
        password = ''
        for i in range(length):
            password += random.choice(string.ascii_letters)
        context={
            'password': password         
            }
    # print(password)
    # print(context)
        return render(request,'lab1_app/index.html',context)

    else:
        context={
            'password': ''         
            }
        return render(request,'lab1_app/index.html',context)


