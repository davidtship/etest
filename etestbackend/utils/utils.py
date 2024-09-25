from django.db import models


class UpdateCreateDate(models.Model):
    """
    An abstract utility class used in models to defined createdat and updatedat fields

    usage:
        from django.db import models
        from utils.utils import UpdateCreateDate
        class myclass(UpdateCreateDate):
            custom_field1 = models.CharField(...)
    """

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
