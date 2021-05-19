from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request.method)
    print(request.POST) # print out form data
    if request.method == 'POST':
        adjective = request.POST['adjective'].title()
        noun = request.POST['noun'].title()
        animal = request.POST['animal'].title()
        noise = request.POST['noise'].title()
        madlib = f'''{adjective} Macdonald had a {noun}, E-I-E-I-O\nand on that {noun} he had an {animal}, E-I-E-I-O\nwith a {noise} {noise} here\nand a {noise} {noise} there,\nhere a {noise}, there a {noise},\neverywhere a {noise} {noise},\n{adjective} Macdonald had a {noun}, E-I-E-I-O.'''
        context = {
            'title': 'Mad Libs!',
            'madlib': madlib
        }
        return render(request, 'madlibapp/index.html', context)
    else:
        context = {
            'title': 'Mad Libs!',
            'madlib': ''
        }
        return render(request, 'madlibapp/index.html', context)

