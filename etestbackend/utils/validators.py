from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import datetime


def validate_date_of_birth(value):
    """
        Define a utility custom validator class used to validate field date of birth of any models.
        usage contraints: make models accept only birthdate >= 18 years old
    usage:
        from django.db import models
        from utils.validators import validate_date_of_birth
        class myclass(models.Model):
            custom_field1 = models.DateField(..., validators=[validate_date_of_birth])
    """
    duration = datetime.date.today() - value
    years = divmod(duration.total_seconds(), 31536000)[0]
    print(years)
    if years < 18:
        raise ValidationError(_("user must be 18 years or older"))
