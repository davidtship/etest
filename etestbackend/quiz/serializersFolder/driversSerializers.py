from rest_framework import serializers
from models.drivers import Driver


class DriverSerializer(serializers.ModelSerializer):
    """
    A DriverSerializer serializer used to serializes serialize Driver model data

    returned field:
        [all]

    Views:
        quiz.views.DriverInfoViewSet

    Embeded in:
        quiz.serializers.QuizScoreDriverSerializer
    """

    class Meta:
        model = Driver
        fields = "__all__"
