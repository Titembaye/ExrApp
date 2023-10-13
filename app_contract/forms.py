from django import forms

from app_client.models import Client
from app_contract.models import Contract
from app_setting.models import Guaranttee, Type, Company
from app_vehicle.models import Vehicle
from app_person.models import Person
from app_dommage.models import Other


class DateInput(forms.DateInput):
    input_type = 'date'


class ContractForm(forms.ModelForm):
    required_css_class = 'required-field'

    class Meta:
        model = Contract
        fields = ['policy_num', 'register_date', 'prime_ttc', 'prime_ht', 'prime_net',
                  'committee', 'detention', 'final_com', 'effect', 'due_date', 'client', 'person', 'vehicle', 'other',
                  'rate', 'accessory', 'assured', 'agent', 'guaranttee', 'type_contract', 'company']

    policy_num = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Numéro de police")
    assured = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Description")
    register_date = forms.DateField(widget=DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                    label="Date d'enregistrement")

    prime_ttc = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Prime TTC")
    prime_ht = forms.DecimalField(widget=forms.HiddenInput(attrs={'class': 'form-control'}), label="Prime HT",
                                  required=False)
    prime_net = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Prime Nette")
    committee = forms.DecimalField(widget=forms.HiddenInput(attrs={'class': 'form-control'}), label="Commission",
                                   required=False)
    detention = forms.DecimalField(widget=forms.HiddenInput(attrs={'class': 'form-control'}), label="Rétenue",
                                   required=False)
    final_com = forms.DecimalField(widget=forms.HiddenInput(attrs={'class': 'form-control'}), label="Commission finale",
                                   required=False)
    effect = forms.DateField(widget=DateInput(attrs={'class': 'form-control', 'type': 'date'}), label="Date effective")
    due_date = forms.DateField(widget=DateInput(attrs={'class': 'form-control', 'type': 'date'}), label="Echéance")
    client = forms.ModelChoiceField(queryset=Client.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}),
                                    label="Client")

    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                     label="Véhicule",
                                     required=False)

    other = forms.ModelChoiceField(queryset=Other.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control'}),
                                   label="Autre",
                                   required=False)

    person = forms.ModelChoiceField(queryset=Person.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}),
                                    label="Personne",
                                    required=False)
    rate = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Taux")
    accessory = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Accessoires")
    agent = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Agent")
    guaranttee = forms.ModelChoiceField(queryset=Guaranttee.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}),
                                        label="Garantie")
    type_contract = forms.ModelChoiceField(queryset=Type.objects.all(),
                                           widget=forms.Select(attrs={'class': 'form-control'}),
                                           label="Type de contrat")
    company = forms.ModelChoiceField(queryset=Company.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                     label="Société")
