from django import forms
from app_person.models import Person
from app_setting.models import Guaranttee, Type, Company


class DateInput(forms.DateInput):
    input_type = 'date'


class PersonForm(forms.ModelForm):
    required_css_class = 'required-field'

    class Meta:
        model = Person
        fields = ['full_name', 'birthday', 'gender','phone']

    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nom et Prénoms")
    birthday = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), label="Date de naissance")
    gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Genre")
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Téléphone")

