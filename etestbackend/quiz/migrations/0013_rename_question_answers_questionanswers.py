# Generated by Django 4.2.3 on 2023-07-16 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_alter_question_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question_Answers',
            new_name='QuestionAnswers',
        ),
    ]
