# Generated by Django 4.2.4 on 2023-10-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('A', 'Autre')], max_length=1)),
                ('phone1', models.CharField(max_length=30)),
                ('phone2', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
    ]
