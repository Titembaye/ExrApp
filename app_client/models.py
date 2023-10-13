from django.db import models


class Client(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('A', 'Autre')
    )
    full_name = models.CharField(max_length=300)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone1 = models.CharField(max_length=30)
    phone2 = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'clients'

    def __str__(self):
        return self.full_name

