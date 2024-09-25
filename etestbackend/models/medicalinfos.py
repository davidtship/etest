from django.db import models


from utils.utils import UpdateCreateDate
from .drivers import Driver


class MedicalInfo(UpdateCreateDate):
    """
    Defines a MedicalInfo Models that stores Drivers Medical information in the databases
    This models is used to let doctor used to have access and upload needed informations

    fields:
        id: auto generated id
        medical_test: a file uploaded by the doctor after the aptitude test
        foreign fields:
            driver: a onetone reference to the driver model


    """

    class Meta:
        app_label = "quiz"

    driver = models.OneToOneField(
        Driver,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="Driver_medical",
    )

    medical_test = models.FileField(
        null=True, blank=True, upload_to="medical_test", verbose_name="Medical Test"
    )

    def __str__(self):
        return f"{self.driver}"
