# Generated by Django 4.2.4 on 2023-08-13 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_alter_user_site'),
        ('quiz', '0041_alter_driver_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizscore',
            name='site',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='score_site', to='accounts.site'),
        ),
    ]