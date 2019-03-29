from django import forms


class FertiliserUserForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': True}))
    manufacturer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': True}))
    type = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    units = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': True}))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'required': True}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={'required': True}))
    N = forms.DecimalField(widget=forms.TextInput(attrs={'readonly': True}))
    P = forms.DecimalField(widget=forms.TextInput(attrs={'readonly': True}))
    K = forms.DecimalField(widget=forms.TextInput(attrs={'readonly': True}))
    Mg = forms.DecimalField(widget=forms.TextInput(attrs={'readonly': True}))



