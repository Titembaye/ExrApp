# Generated by Django 4.2.4 on 2023-10-03 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_person', '0001_initial'),
        ('app_dommage', '0001_initial'),
        ('app_vehicle', '0001_initial'),
        ('app_client', '0001_initial'),
        ('app_setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('policy_num', models.CharField(max_length=255)),
                ('assured', models.CharField(max_length=1500)),
                ('prime_ttc', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prime_ht', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prime_net', models.DecimalField(decimal_places=2, max_digits=10)),
                ('committee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('detention', models.DecimalField(decimal_places=2, max_digits=10)),
                ('final_com', models.DecimalField(decimal_places=2, max_digits=10)),
                ('register_date', models.DateField()),
                ('effect', models.DateField()),
                ('due_date', models.DateField()),
                ('amendment', models.CharField(max_length=50)),
                ('agent', models.CharField(max_length=100)),
                ('accessory', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_client.client')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_setting.company')),
                ('guaranttee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_setting.guaranttee')),
                ('other', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_dommage.other')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_person.person')),
                ('type_contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_setting.type')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_vehicle.vehicle')),
            ],
            options={
                'db_table': 'contracts',
            },
        ),
    ]