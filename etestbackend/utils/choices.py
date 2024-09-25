from django.db import models


class sex_choices(models.TextChoices):

    """
    Define a custom choice class inheriting from django.db.models.TextChoices

    Usage:
        from utils.choices import sex_choices
        class customModel(models.Model):
            field2 = models.CharField(max_lenght=20, choices=sex_choices.choices)
    """

    FEMALE = "F", "Female"
    MALE = "M", "Male"


class licence_type_choices(models.TextChoices):
    """
    Define a custom licence_type choice class inheriting from django.db.models.TextChoices

    Usage:
        from utils.choices import licence_type_choices
        class customModel(models.Model):
            field2 = models.CharField(max_lenght=20, choices=licence_type_choices.choices)
    """

    NATIONAl = "Nat", "National"
    INTERNATIONAL = "Inter", "International"


class document_type(models.TextChoices):
    """
    Define a custom document_type choice class inheriting from django.db.models.TextChoices

    Usage:
        from utils.choices import document_type
        class customModel(models.Model):
            field2 = models.CharField(max_lenght=20, choices=document_type.choices)
    """

    PASSPORT = "PS", "Passport"
    CARTE_ELECTEUR = "Cart", "Carte D'electeur"


class TestType(models.TextChoices):

    """
    Define a custom TestType choice class inheriting from django.db.models.TextChoices

    Usage:
        from utils.choices import TestType
        class customModel(models.Model):
            field2 = models.CharField(max_lenght=20, choices=TestType.choices)
    """

    THEORY = "Th", "Theory"
    PRATICAL = "Pr", "Practical"
