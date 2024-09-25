# Generated by Django 4.2.3 on 2023-07-15 23:45

import utils.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "accounts",
            "0004_user_first_name_user_is_doctor_user_is_receptionist_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "address1",
                    models.CharField(max_length=1024, verbose_name="Numero et Rue"),
                ),
                (
                    "address2",
                    models.CharField(
                        max_length=1024, verbose_name="Quartier et commune"
                    ),
                ),
                (
                    "zip_code",
                    models.CharField(
                        blank=True,
                        max_length=12,
                        null=True,
                        verbose_name="ZIP / Postal code",
                    ),
                ),
                ("city", models.CharField(max_length=1024, verbose_name="City")),
                ("country", models.CharField(max_length=255, verbose_name="Country")),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresses",
            },
        ),
        migrations.AlterField(
            model_name="user",
            name="date_of_birth",
            field=models.DateField(
                validators=[utils.validators.validate_date_of_birth]
            ),
        ),
        migrations.CreateModel(
            name="drivers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "form_number",
                    models.CharField(
                        max_length=10,
                        unique=True,
                        verbose_name="Driving licence Form number",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=255, verbose_name="Driver Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=255, verbose_name="Driver Name"),
                ),
                (
                    "driver_nationality",
                    models.CharField(max_length=255, verbose_name="Driver Nationality"),
                ),
                (
                    "driver_identity_document_number",
                    models.CharField(
                        max_length=255, verbose_name="Driver Identity document number"
                    ),
                ),
                (
                    "address",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="driver_address",
                        to="accounts.address",
                    ),
                ),
            ],
        ),
    ]