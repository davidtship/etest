# Generated by Django 4.2.3 on 2023-08-05 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0025_alter_quizanswers_test_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizanswers',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Obtained score'),
        ),
        migrations.AlterField(
            model_name='quizanswers',
            name='test_type',
            field=models.CharField(choices=[('Th', 'Theory'), ('Pr', 'Practical')], default='Th', max_length=15, verbose_name='Quiz type'),
        ),
    ]