# Generated by Django 4.2.4 on 2023-10-03 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=50)),
                ('registration', models.CharField(max_length=20)),
                ('power', models.CharField(max_length=15)),
                ('seats', models.CharField(max_length=10)),
                ('model_year', models.PositiveIntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_setting.company')),
                ('guaranttee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_setting.guaranttee')),
                ('type_contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_setting.type')),
            ],
            options={
                'db_table': 'vehicles',
            },
        ),
    ]
