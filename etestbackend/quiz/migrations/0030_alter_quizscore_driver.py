# Generated by Django 4.2.3 on 2023-08-05 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0029_rename_answer_option_quizanswers_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizscore',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='driver_score', to='quiz.driver'),
        ),
    ]
