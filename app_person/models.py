from django.db import models
from app_setting.models import Type, Guaranttee, Company, Category


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=300)
    birthday = models.DateField('Date de naissance', help_text="jj/mm/aaaa")
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=2)


    class Meta:
        db_table = 'persons'

    def __str__(self):
        return f"{self.full_name}"

