# Generated by Django 4.2.3 on 2023-07-17 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_address_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_answers',
            name='user',
        ),
        migrations.AddField(
            model_name='user_answers',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='quiz.driver'),
        ),
    ]
