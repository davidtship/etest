# Generated by Django 4.2.4 on 2023-08-11 18:41

from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0037_alter_quizscore_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='date_of_birth',
            field=models.DateField(null=True, validators=[utils.validators.validate_date_of_birth]),
        ),
    ]
