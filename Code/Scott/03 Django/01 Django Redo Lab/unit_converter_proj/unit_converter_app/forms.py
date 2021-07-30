from django import forms

class Conversion(forms.Form):
    valInput = forms.DecimalField(
        max_digits=50, 
        decimal_places=20,
        label="Value")

    unit_choices = [
        ('mi', 'Miles'),
        ('m', 'Meters'),
        ('km', 'Kilometers'),
        ('yd', 'Yards'),
        ('in', 'Inches'), 
        ('ft', 'Feet'),
    ]
    unitInput = forms.ChoiceField(
        choices=unit_choices,
        label="Input Units"
    )
    unitOutput = forms.ChoiceField(
        choices=unit_choices,
        label="Desired Units"
    )