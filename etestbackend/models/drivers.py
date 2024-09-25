from django.db import models
from django.utils.translation import gettext_lazy as _


from phonenumber_field.modelfields import PhoneNumberField

from utils.validators import validate_date_of_birth
from utils.choices import sex_choices, document_type, licence_type_choices

from .sites import Site


class Driver(models.Model):
    """
    Defines a Driver Models that stores Drivers information in the databases

    fields:
        id: auto generated id
        ....
        registration_form: used to store used filled form bought from the bank
        driving_school_certificate: used to store the user driving school certificate

        foreign fields:

    """

    class Meta:
        app_label = "quiz"

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    form_number = models.CharField(
        _("Driving licence Form number"), unique=True, max_length=10
    )

    # model field

    licence_type = models.CharField(
        _("Driving license type"),
        choices=licence_type_choices.choices,
        default=licence_type_choices.NATIONAl,
        max_length=10,
    )

    phone = PhoneNumberField(null=True)
    email = models.EmailField(
        verbose_name="email address", max_length=255, unique=True, null=True
    )

    first_name = models.CharField(
        verbose_name="Driver Names",
        max_length=255,
    )

    middle_name = models.CharField(
        verbose_name="Driver Middle Name",
        max_length=255,
        null=True,
    )

    last_name = models.CharField(
        verbose_name="Driver Last Names",
        max_length=255,
    )
    driver_nationality = models.CharField(
        verbose_name="Driver Nationality",
        max_length=255,
    )

    driver_identity_document = models.CharField(
        _("Identity document type"),
        max_length=40,
        choices=document_type.choices,
        default=document_type.CARTE_ELECTEUR,
    )

    driver_identity_document_number = models.CharField(
        verbose_name="Driver Identity document number",
        max_length=255,
    )

    place_birth = models.CharField(
        verbose_name="Driver place birth", max_length=255, null=True
    )

    date_of_birth = models.DateField(null=True, validators=[validate_date_of_birth])

    sex = models.CharField(
        _("sex"),
        choices=sex_choices.choices,
        default=sex_choices.MALE,
        max_length=10,
        null=True,
    )

    adress_number = models.CharField(
        _("Adress Number"), max_length=100, null=True, blank=True
    )

    adress_street = models.CharField(
        "Adress street",
        max_length=255,
        null=True,
    )

    adress_area = models.CharField(
        "Area Name",
        max_length=255,
        null=True,
    )

    adress_township = models.CharField(
        "Adress Township",
        max_length=255,
        null=True,
    )

    city = models.CharField(
        "City",
        max_length=1024,
        null=True,
    )

    state = models.CharField(
        "Province",
        max_length=1024,
        null=True,
    )

    country = models.CharField("Country", max_length=255, null=True)

    profile_pic = models.ImageField(
        upload_to="divers_photo", blank=True, null=True, verbose_name="Driver Photo"
    )

    registration_form = models.FileField(
        null=True,
        blank=True,
        upload_to="formulaire",
        verbose_name="Formulaire d'enregistrement",
    )

    driving_school_certificate = models.FileField(
        null=True,
        blank=True,
        upload_to="driving_school_certificate",
        verbose_name="Driving School Certificate",
    )

    site = models.ForeignKey(
        Site,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="driver_site",
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
