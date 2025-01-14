# Generated by Django 4.2.4 on 2023-08-11 18:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='adress',
            field=models.CharField(max_length=500, null=True, verbose_name='Site location'),
        ),
        migrations.AddField(
            model_name='site',
            name='manager',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Unique site name'),
        ),
        migrations.AddField(
            model_name='site',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
