from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

from models.sites import Site
from .siteSerializers import SiteSerializer


User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Define a serializer class that inherit from the jwt TokenObtainPairSerializer.

    return custom data imbedded in the urls /auth/jwt/create
    for now not used for this project
    """

    def validate(self, attrs):
        data = super().validate(attrs)

        data["email"] = self.user.email

        return data


class UserCreateSerializer(UserCreateSerializer):

    """
    Define a custom UserCreateSerializerclass that inherit
    from the djoser UsercreateSerilizer to define a custom registration
    This class is intended to override the default DJOSER serializers

    usage:
        settings:
        DJOSER {
            SERIALIZERS: {
                user_list: account.serializers.UserCreateSerializer
            }
        }
    """

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = "__all__"


class UserListSerializer(UserCreateSerializer):

    """
    Define a custom UserCreateSerializerclass that inherit
    from the djoser UsercreateSerilizer to define a custom registration
    This class is intended to override the default DJOSER serializers

    usage:
        settings:
        DJOSER {
            SERIALIZERS: {
                user_list: account.serializers.UserCreateSerializer
            }
        }
    """

    site = SiteSerializer()

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "middle_name",
            "last_name",
            "phone",
            "profile_pic",
            "date_of_birth",
            "sex",
            "is_active",
            "is_admin",
            "is_doctor",
            "is_receptionist",
            "is_siteManager",
            "date_joined",
            "site",
        ]
