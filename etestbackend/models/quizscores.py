from django.db import models
from django.utils.translation import gettext_lazy as _


from utils.utils import UpdateCreateDate
from utils.choices import TestType

from .drivers import Driver
from .sites import Site


class QuizScore(UpdateCreateDate):

    """
    Defines a QuizScore Models that stores Drivers Score information in the databases
    This models is used to store multiples test passed by the users

    fields:
        id: auto generated id
        test_type: it hold two options be (th: Theory), (pr: Pratical)
        ....
        registration_form: used to store used filled form bought from the bank
        driving_school_certificate: used to store the user driving school certificate
        schedule_on: datetime when the driver should take is test
        passed_on: datetime whem the driver has finished the test
        score: driver score of after taking the test

        foreign fields:
            driver: reference the driver model that is taking the tests


    """

    class Meta:
        app_label = "quiz"

    driver = models.ForeignKey(
        Driver, null=True, on_delete=models.PROTECT, related_name="driver_score"
    )

    test_type = models.CharField(
        _("Quiz type"),
        choices=TestType.choices,
        default=TestType.THEORY,
        max_length=15,
    )
    schedule_on = models.DateTimeField(_("Quiz Scheduled on"), null=True, blank=True)
    taken = models.BooleanField(_("taken"), default=False, null=True, blank=True)

    score = models.DecimalField(
        _("Obtained score"), max_digits=4, decimal_places=2, null=True, blank=True
    )

    site = models.ForeignKey(
        Site,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="score_site",
    )

    def __str__(self):
        return f"{self.id}"
