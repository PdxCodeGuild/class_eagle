from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    print(request.POST)
    return render(request,'lab1_app/index.html')


