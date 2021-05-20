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
    print(password)



        
    return render(request,'lab1_app/index.html')


