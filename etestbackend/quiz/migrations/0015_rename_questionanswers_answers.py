# Generated by Django 4.2.3 on 2023-07-16 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_remove_questionanswers_title_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionAnswers',
            new_name='Answers',
        ),
    ]