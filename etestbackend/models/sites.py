from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.utils import UpdateCreateDate


class Site(UpdateCreateDate):
    """
    Defines a Site model that is used to store users site informations.
    each user is and drivers is a assigned a site that idenfies in which centre he has been located

    usage:
        1. quiz.views SiteViewset
        1. quiz.url site/

    """

    class Meta:
        app_label = "accounts"

    name = models.CharField(
        _("Unique site name"), max_length=255, unique=True, null=True
    )

    province = models.CharField(_("Province"), null=True, max_length=255)
    city = models.CharField(_("City"), null=True, max_length=255)

    adress = models.CharField(_("Site adress"), max_length=500, null=True)

    def __str__(self) -> str:
        return f"{self.name}"
