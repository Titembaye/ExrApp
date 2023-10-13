from django import forms

from app_setting.models import Guaranttee, Type, Company
from .models import Vehicle
from app_client.models import Client


class VehicleForm(forms.ModelForm):
    required_css_class = 'required-field'

    class Meta:
        model = Vehicle
        fields = ['brand', 'registration', 'power', 'seats', 'model_year']

    brand = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Marque")
    registration = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Immatriculation")
    power = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Puissance")
    seats = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Sièges")
    model_year = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Année")
