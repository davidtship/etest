# Generated by Django 4.2.4 on 2023-08-13 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_site_adress_alter_site_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='manager',
        ),
        migrations.AddField(
            model_name='user',
            name='is_siteManager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='site',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='site', to='accounts.site'),
        ),
    ]
