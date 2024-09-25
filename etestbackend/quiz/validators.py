from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import datetime

def validate_date_of_birth(value):
    ## calculate difference in years
    duration = datetime.date.today() - value
    years = divmod(duration.total_seconds(), 31536000)[0]
    print(years)
    if years < 18:
        raise ValidationError(_("user must be 18 years or older"))