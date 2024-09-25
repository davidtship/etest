from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User
from models.sites import Site


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "phone",
            "sex",
            "date_of_birth",
            "site",
        ]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs["readonly"] = True
        self.fields["date_joined"].widget.attrs["readonly"] = True

    password = ReadOnlyPasswordHashField()
    readonly_fields = ["email", "date_joined"]

    class Meta:
        model = User
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "phone",
            "profile_pic",
            "sex",
            "date_of_birth",
            "is_active",
            "is_admin",
            "is_doctor",
            "is_receptionist",
            "is_superuser",
            "date_joined",
            "site",
        ]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = [
        "email",
        "first_name",
        "last_name",
        "phone",
        "sex",
        "date_of_birth",
        "is_active",
        "is_admin",
        "is_doctor",
        "is_receptionist",
        "site",
    ]
    list_filter = ["is_admin"]

    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        (
            "Personal info",
            {
                "fields": [
                    "profile_pic",
                    "first_name",
                    "middle_name",
                    "last_name",
                    "phone",
                    "sex",
                    "date_of_birth",
                    "site",
                ]
            },
        ),
        (
            "Permissions",
            {
                "fields": [
                    "is_admin",
                    "is_active",
                    "is_doctor",
                    "is_receptionist",
                    "is_superuser",
                    "groups",
                ]
            },
        ),
        ("Important Dates", {"fields": ["date_joined"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "date_of_birth", "password1", "password2"],
            },
        ),
    ]

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets

        if request.user.is_superuser:
            perm_fields = (
                "is_active",
                "is_admin",
                "is_doctor",
                "is_receptionist",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        else:
            # modify these to suit the fields you want your
            # staff user to be able to edit
            perm_fields = ("is_active", "is_doctor", "is_receptionist")

        return [
            (None, {"fields": ("email", "password")}),
            (
                ("Personal info"),
                {
                    "fields": (
                        "profile_pic",
                        "first_name",
                        "middle_name",
                        "last_name",
                        "phone",
                        "date_of_birth",
                        "site",
                    )
                },
            ),
            (("Permissions"), {"fields": perm_fields}),
            ("Important Dates", {"fields": ["date_joined"]}),
        ]

    search_fields = ["email", "first_name", "last_name"]
    ordering = ["email"]
    filter_horizontal = []


class SiteAdmin(admin.ModelAdmin):
    list_display = ["name", "province", "city", "created"]

    class Meta:
        model = Site


# Now register the new UserAdmin...
admin.site.register(Site, SiteAdmin)
admin.site.register(User, UserAdmin)
