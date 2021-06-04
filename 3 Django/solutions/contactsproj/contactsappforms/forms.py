
from django import forms
from contactsapp.models import Contact

class DateInput(forms.DateInput):
    input_type = 'date'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['user']
        widgets = {
            'birthday': DateInput()
        }        


