from django import forms
from app_dommage.models import Other
from app_setting.models import Guaranttee, Type, Company


class DateInput(forms.DateInput):
    input_type = 'date'


class OtherForm(forms.ModelForm):
    required_css_class = 'required-field'

    class Meta:
        model = Other
        fields = ['description', 'comment']

    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Description")
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Commentaire",
                              required=False)

