from django.db import models
from app_client.models import Client
from app_setting.models import Type, Company, Guaranttee
from app_vehicle.models import Vehicle
from app_person.models import Person
from app_dommage.models import Other


class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    policy_num = models.CharField(max_length=255)
    assured = models.CharField(max_length=1500)
    prime_ttc = models.DecimalField(max_digits=10, decimal_places=2)
    prime_ht = models.DecimalField(max_digits=10, decimal_places=2)
    prime_net = models.DecimalField(max_digits=10, decimal_places=2)
    committee = models.DecimalField(max_digits=10, decimal_places=2)
    detention = models.DecimalField(max_digits=10, decimal_places=2)
    final_com = models.DecimalField(max_digits=10, decimal_places=2)
    register_date = models.DateField()
    effect = models.DateField()
    due_date = models.DateField()
    amendment = models.CharField(max_length=50)
    agent = models.CharField(max_length=300)
    accessory = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    other = models.ForeignKey(Other, on_delete=models.SET_NULL, null=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type_contract = models.ForeignKey(Type, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    guaranttee = models.ForeignKey(Guaranttee, on_delete=models.CASCADE)

    class Meta:
        db_table = 'contracts'

    def __str__(self):
        return self.policy_num

    def is_nouvelle_affaire(self):
        return self.type_contract.libelle == 'NOUVELLE AFFAIRE'

    def is_renouvellement(self):
        return self.type_contract.libelle == 'RENOUVELLEMENT'
