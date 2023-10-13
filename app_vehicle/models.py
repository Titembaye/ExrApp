from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from app_setting.models import Type, Company, Guaranttee


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    registration = models.CharField(max_length=20)
    power = models.CharField(max_length=15)
    seats = models.CharField(max_length=10)
    model_year = models.PositiveIntegerField()

    class Meta:
        db_table = 'vehicles'

    def __str__(self):
        return f"{self.brand} ({self.registration})"


