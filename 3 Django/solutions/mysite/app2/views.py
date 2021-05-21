from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
    return HttpResponse('You are viewing app 2 - view 1')

def view2(request):
    return HttpResponse('You are viewing app 2 - view 2')

def view3(request):
    return HttpResponse('You are viewing app 2 - view 3')