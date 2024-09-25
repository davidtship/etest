# Generated by Django 4.2.3 on 2023-07-15 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_drivers_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='licence_type',
            field=models.CharField(choices=[('Nat', 'National'), ('Inter', 'International')], default='Nat', max_length=10, verbose_name='Driving type'),
        ),
    ]
