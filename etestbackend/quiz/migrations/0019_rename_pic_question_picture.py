# Generated by Django 4.2.3 on 2023-07-20 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0018_question_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pic',
            new_name='picture',
        ),
    ]
