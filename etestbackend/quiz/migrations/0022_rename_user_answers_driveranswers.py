# Generated by Django 4.2.3 on 2023-08-04 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0021_medicalinfo_remove_driver_address_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Answers',
            new_name='DriverAnswers',
        ),
    ]
