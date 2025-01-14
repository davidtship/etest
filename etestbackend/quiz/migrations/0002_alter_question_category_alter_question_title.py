# Generated by Django 4.2.3 on 2023-07-09 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='quiz.category'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Question'),
        ),
    ]
