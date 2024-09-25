from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

import datetime

from accounts.managers import MyUserManager


from utils.validators import validate_date_of_birth
from utils.utils import UpdateCreateDate
from utils.choices import sex_choices

from models.sites import Site


class User(AbstractBaseUser, PermissionsMixin):

    """
    Defines a Custom User Model that inherits from the Abastract user and PermissionMixin
    PermissionMixin -> To use Django default permissions in admin site

    In Setting: AUTH_USER_MODEL= account.user

    Used to create a custom serializers in accounts.serialzers.UserCreateSerializer


    """

    class Meta:
        app_label = "accounts"

    objects = MyUserManager()
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(verbose_name="First Name", max_length=255, null=True)
    middle_name = models.CharField(
        verbose_name="Middle Name", max_length=255, null=True
    )

    last_name = models.CharField(verbose_name="Last Name", max_length=255, null=True)

    phone = PhoneNumberField(null=True)

    profile_pic = models.ImageField(upload_to="profile_pic", blank=True, null=True)

    date_of_birth = models.DateField(validators=[validate_date_of_birth])

    sex = models.CharField(
        _("sex"),
        choices=sex_choices.choices,
        default=sex_choices.MALE,
        max_length=10,
        null=True,
    )

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_receptionist = models.BooleanField(default=False)
    is_siteManager = models.BooleanField(default=False)

    site = models.ForeignKey(
        Site, on_delete=models.SET_NULL, null=True, blank=True, related_name="site"
    )

    date_joined = models.DateField(_("Date Joined"), default=datetime.date.today)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "middle_name",
        "last_name",
        "phone",
        "date_of_birth",
        "is_admin",
        "is_doctor",
        "is_receptionist",
        "is_siteManager",
        "site"
    ]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
