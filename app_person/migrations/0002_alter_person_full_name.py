# Generated by Django 4.2.4 on 2023-10-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
    ]
