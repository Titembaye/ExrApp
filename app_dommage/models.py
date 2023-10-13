from django.db import models

from app_setting.models import Type, Company, Guaranttee


class Other(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1500)
    comment = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        db_table = 'others'

    def __str__(self):
        return self.description
