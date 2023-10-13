# myapp/tests/test_models.py
import pytest
from app_client.models import Client


@pytest.mark.django_db
def test_create_client_with_optional_fields():
    # Créez une instance de Client avec des champs optionnels
    client = Client.objects.create(
        full_name="Alice Smith",
        gender="F",
        phone1="65 55 42 62",
        phone2="69 55 43 62",
    )

    # Vérifiez si les attributs sont corrects
    assert client.full_name == "Alice Smith"
    assert client.gender == "F"
    assert client.phone1 == "65 55 42 62"
    assert client.email == "69 55 43 62"


@pytest.mark.django_db
def test_create_client_with_required_fields():
    # Créez une instance de Client avec les champs obligatoires uniquement
    client = Client.objects.create(
        full_name="Bob Johnson",
        gender="M",
        phone1 = "65 55 42 62",
    )

    # Vérifiez si les attributs sont corrects
    assert client.full_name == "Bob Johnson"
    assert client.gender == "M"
    assert client.phone1 == "65 55 42 62"


@pytest.mark.django_db
def test_client_str_method():
    # Créez une instance de Client
    client = Client.objects.create(full_name="Alice Smith", gender="F")

    # Vérifiez si la méthode __str__ renvoie le nom complet du client
    assert str(client) == "Alice Smith"
