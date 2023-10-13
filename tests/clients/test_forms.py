from django.test import TestCase
from app_client.forms import ClientForm


class ClientFormTest(TestCase):
    def test_valid_form(self):
        # Créez un dictionnaire de données valides pour le formulaire
        form_data = {
            'full_name': 'John Doe',
            'gender': 'M',
            'phone1': '98 55 42 62',
            'phone2': '73 41 55 12'
        }

        # Créez une instance du formulaire avec les données
        form = ClientForm(data=form_data)

        # Vérifiez si le formulaire est valide
        self.assertTrue(form.is_valid())

    def test_valid_form2(self):
        # Créez un dictionnaire de données valides pour le formulaire
        form_data = {
            'full_name': 'John Doe',
            'gender': 'M',
            'phone1': '98 55 42 62',
            'phone2': ''
        }

        # Créez une instance du formulaire avec les données
        form = ClientForm(data=form_data)

        # Vérifiez si le formulaire est valide
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Créez un dictionnaire de données invalides pour le formulaire (manque de champs requis)
        form_data = {
            'full_name': '',
            'gender': 'M',
            'phone1': '98 55 42 62',
            'phone2': '73 41 55 12'
        }

        # Créez une instance du formulaire avec les données invalides
        form = ClientForm(data=form_data)

        # Vérifiez si le formulaire est invalide
        self.assertFalse(form.is_valid())

    def test_gender_choices(self):
        # Vérifiez que les choix de genre sont corrects
        form = ClientForm()
        gender_choices = form.fields['gender'].choices

        # Les choix doivent correspondre aux valeurs définies dans votre modèle Client
        expected_choices = [
            ('M', 'Masculin'),
            ('F', 'Féminin'),
            ('A', 'Autre')
        ]

        self.assertEqual(list(gender_choices), expected_choices)
