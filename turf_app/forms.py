from django import forms

FERTILISER_TYPE = [('granulate', 'Granulate'), ('liquid', 'Liquid')]


class FertiliserUserForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': True}))
    manufacturer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': True}))
    type = forms.CharField(label="Type of Fertiliser", widget=forms.Select(choices=FERTILISER_TYPE))
    N = forms.DecimalField()
    P = forms.DecimalField()
    K = forms.DecimalField()
    Mg = forms.DecimalField()
    price = forms.DecimalField()


