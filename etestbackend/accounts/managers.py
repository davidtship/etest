from django.db import models
from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(
        self,
        email,
        first_name,
        middle_name,
        last_name,
        phone,
        date_of_birth,
        site,
        is_admin,
        is_doctor,
        is_receptionist,
        is_siteManager,
        password=None,
    ):
        """
        Creates and saves a User with the given email, first_name, middle_name, last_name, phone date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            phone=phone,
            date_of_birth=date_of_birth,
            site=site,
            is_admin=is_admin,
            is_doctor=is_doctor,
            is_receptionist=is_receptionist,
            is_siteManager=is_siteManager,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        first_name,
        middle_name,
        last_name,
        phone,
        date_of_birth,
        site,
            is_admin,
            is_doctor,
            is_receptionist,
            is_siteManager,
        password=None,
    ):
        """
        Creates and saves a superuser with the given email, first_name, middle_name, last_name, phone date of
        birth and password.
        """
        user = self.create_user(
            email,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            phone=phone,
            date_of_birth=date_of_birth,
            site=None,
            is_admin=True,
            is_doctor=False,
            is_receptionist=False,
            is_siteManager=False,
            password=password,
        )
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
