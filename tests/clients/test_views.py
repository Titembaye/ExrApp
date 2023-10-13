# Importez les modules de test Django nécessaires
from django.test import TestCase, Client

from django.urls import reverse
from app_client.models import Client


class ClientTests(TestCase):
    def setUp(self):
        # Créez des clients de test pour une utilisation dans les tests
        self.client1 = Client.objects.create(full_name="John Doe", gender="M", phone1="98 55 42 62",
                                             phone2="73 41 55 12")
        self.client2 = Client.objects.create(full_name="Alice Smith", gender="F", phone1="65 55 42 62",
                                             phone2="73 48 55 12")

    def test_client_list_view(self):
        # Testez l'affichage de la liste des clients
        response = self.client.get(reverse('app_client:client_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['clients'], [repr(self.client1), repr(self.client2)], ordered=False)

    def test_client_detail_view(self):
        # Testez l'affichage des détails d'un client
        response = self.client.get(reverse('app_client:client_detail', args=[self.client1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['client'], self.client1)

    def test_client_add_view(self):
        # Testez l'ajout d'un client
        response = self.client.post(reverse('app_client:client_add'), {
            'full_name': 'Test Client',
            'gender': 'M',
            'phone1': '99 88 77 66',
            'phone2': '11 22 33 44'
        })
        self.assertEqual(response.status_code, 302)  # Redirection après ajout
        self.assertTrue(Client.objects.filter(full_name='Test Client').exists())

    def test_client_edit_view(self):
        # Testez la modification d'un client
        response = self.client.post(reverse('app_client:client_edit', args=[self.client1.id]), {
            'full_name': 'Updated Client Name',
            'gender': 'F',
            'phone1': '99 88 77 66',
            'phone2': '11 22 33 44'
        })
        self.assertEqual(response.status_code, 302)  # Redirection après modification
        self.client1.refresh_from_db()  # Rafraîchir l'instance du client depuis la base de données
        self.assertEqual(self.client1.full_name, 'Updated Client Name')

    def test_client_delete_view(self):
        # Testez la suppression d'un client
        response = self.client.post(reverse('app_client:client_delete', args=[self.client1.id]))
        self.assertEqual(response.status_code, 302)  # Redirection après suppression
        self.assertFalse(Client.objects.filter(full_name='John Doe').exists())

    def test_client_search_view(self):
        # Testez la recherche de clients
        response = self.client.get(reverse('app_client:client_list'), {'q': 'Alice'})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['clients'], [repr(self.client2)], ordered=False)

