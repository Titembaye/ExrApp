# Generated by Django 4.2.4 on 2023-10-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_person', '0002_alter_person_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='full_name',
            field=models.CharField(max_length=150),
        ),
    ]
