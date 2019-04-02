from django import forms
from turf_app.models import Field
from django.contrib.auth.models import User


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


LIST_FIELDS = list(Field.objects.all())

class ApplicationUserForm(forms.Form):
    field = forms.CharField(max_length=100, widget=forms.Select(choices=LIST_FIELDS))



