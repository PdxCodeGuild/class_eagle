from django.http import HttpResponse
from django.shortcuts import render
from .forms import Conversion

# Create your views here.
# def index(request):
#     return render(request, 'unit_converter_app/index.html'

def index(request):
    submitbutton = request.POST.get("submit")
    valInput=None
    unitInput=None
    unitOutput=None

    ft_mult_dict = { # * = convert out of ft, / = converts into ft
        'mi' : 0.0001893939,
        'm' : 0.3048,
        'km' : 0.0003048,
        'yd' : 0.3333333333,
        'in' : 12,
        'ft' : 1
    }

    form= Conversion(request.POST or None)
    if form.is_valid():
        valInput= form.cleaned_data.get("valInput")
        unitInput= form.cleaned_data.get("unitInput")
        unitOutput= form.cleaned_data.get("unitOutput")

        valInput = float(valInput)
        inFt = valInput / ft_mult_dict[unitInput]
        inM = inFt * ft_mult_dict[unitOutput]
        inM = round(inM, 5)

    context= {'form': form, 'valInput': valInput, 'unitInput':unitInput, 'unitOutput': unitOutput, 'submitbutton': submitbutton, 'output': inM}
    return render(request, 'unit_converter_app/index.html', context)
