from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UnitForm

ft_mult_dict = { # * = convert out of ft, / = converts into ft
    'mi' : 0.0001893939,
    'm' : 0.3048,
    'km' : 0.0003048,
    'yd' : 0.3333333333,
    'in' : 12,
    'ft' : 1
}
unit_in = ''
amount_in = 0
output = None

def index(request):
    if request.method == 'POST': # receiving a form submission
        # create an instance of our form from the form data
        form = UnitForm(request.POST)
        if form.is_valid():
            # get the data out of the form
            amount_in = form.cleaned_data['amount_in']
            unit_in = form.cleaned_data['unit_in']
            amount_in = float(amount_in)

            # output calculations
            input_in_ft = amount_in / ft_mult_dict[unit_in]
            output = input_in_ft * ft_mult_dict['m'] # Always returns meters
            
            # format output
            output = round(output, 5)
            output = str(output)

            form = UnitForm()
        # if the form is invalid, we just send it back to the template
    else: # receiving a GET request
        form = UnitForm() # create a new blank form
    print(output)
    return render(request, 'unitconverterapp/index.html', {'form': form}) # pass the form to the template
# TODO: output result onto new page (stil completely untested)
def result(request):
    return render(request, 'unitconverterapp/result.html', {'output': output})