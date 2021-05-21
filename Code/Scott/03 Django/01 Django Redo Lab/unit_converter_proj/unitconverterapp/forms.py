from django import forms

unit_tuples = [('mi', 'miles'), ('m', 'meters'), ('km', 'kilometers'), ('yd', 'yards'), ('in', 'inches'), ('ft', 'feet')]
# Create your models here.
class UnitForm(forms.Form):
    amount_in = forms.DecimalField(label="Amount")
    unit_in = forms.ChoiceField(label="Units", choices=unit_tuples)
