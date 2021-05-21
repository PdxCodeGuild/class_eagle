from django.shortcuts import render
from django.http import HttpResponse


def unit_converter(convert_to, convert_from , distance):
    conversions = {

    "ft" : 3.048,
    "mi" : 16093.4,
    "m" : 10,
    "km" : 10000,
    "yard" : 9.144,
    "inch" : 0.254,

    }

    # Asking for user inputs
    input_unit = convert_from
    distance = float(distance)
    output_unit = convert_to


    #output_name is for better readibility on output
    output_name = output_unit 
    input_name = input_unit

    # math : converts user inputs to meters, then converts meters to final output
    input_unit = conversions.get(input_unit)
    meters = distance * input_unit
    output_unit = conversions.get(output_unit)
    final = meters / output_unit

    #output
    return final

def index(request):
    if request.method == "POST":
        a = request.POST['to']
        b = request.POST['from']
        c = float(request.POST['distance'])

        converted = unit_converter(a,b,c)

        context = {
            'converted' : converted,
            'a' : a
        }
        return render(request, 'UnitConverter/index.html', context)
    else:
        context = {}
        return render(request, 'UnitConverter/index.html', context)
