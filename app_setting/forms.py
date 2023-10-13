from django import forms

from app_setting.models import Guaranttee, Company, Type


class GuarantteeForm(forms.ModelForm):
    required_css_class = 'required-field'

    class Meta:
        model = Guaranttee
        fields = ['libelle']

    libelle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Libellé")


class TypeForm(forms.ModelForm):
    required_css_class = 'required-field'

    class Meta:
        model = Type
        fields = '__all__'

    libelle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Libellé")


class CompanyForm(forms.ModelForm):
    required_css_class = 'required-field'

    class Meta:
        model = Company
        fields = ['name']

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nom")
