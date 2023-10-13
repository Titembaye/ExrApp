from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'gender', 'phone1', 'phone2']

    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nom et Prénoms")
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'form-check-input form-check-inline'}),
        choices=Client.GENDER_CHOICES
    )
    phone1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Téléphone 1")
    phone2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Téléphone 2")
