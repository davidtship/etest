# Generated by Django 4.2.3 on 2023-07-16 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_driver_licence_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profile',
            new_name='profile_pic',
        ),
        migrations.AlterField(
            model_name='driver',
            name='licence_type',
            field=models.CharField(choices=[('Nat', 'National'), ('Inter', 'International')], default='Nat', max_length=10, verbose_name='Driving license type'),
        ),
    ]