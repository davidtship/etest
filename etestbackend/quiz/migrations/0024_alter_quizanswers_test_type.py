# Generated by Django 4.2.3 on 2023-08-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0023_quizanswers_delete_driveranswers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizanswers',
            name='test_type',
            field=models.CharField(choices=[('Th', 'Théorie'), ('Pr', 'Practical')], default='Th', max_length=15, verbose_name='Test type'),
        ),
    ]
