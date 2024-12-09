# Generated by Django 5.1.3 on 2024-12-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationSKU',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('medication_name', models.CharField(max_length=100)),
                ('formulation', models.CharField(max_length=100)),
                ('dosage', models.IntegerField()),
                ('unit', models.CharField(max_length=10)),
            ],
            options={
                'unique_together': {('medication_name', 'formulation', 'dosage', 'unit')},
            },
        ),
    ]
