# Generated by Django 4.2.4 on 2023-08-07 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0036_alter_question_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizscore',
            name='score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Obtained score'),
        ),
    ]