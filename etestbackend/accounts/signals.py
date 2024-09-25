from django.db.models.signals import pre_save
from django.core.exceptions import PermissionDenied
from .models import User
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


def updateUser(sender, instance, **kwargs):
    user = instance
    if user.email != "":
        user.username = user.email


pre_save.connect(updateUser, sender=User)


@receiver(pre_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    if instance.is_superuser:
        raise PermissionDenied
