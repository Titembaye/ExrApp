from django.db import models


class Guaranttee(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=300)

    class Meta:
        db_table = 'guarantties'

    def __str__(self):
        return self.libelle


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50)

    class Meta:
        db_table = 'types'

    def __str__(self):
        return self.libelle


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(100)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.libelle
