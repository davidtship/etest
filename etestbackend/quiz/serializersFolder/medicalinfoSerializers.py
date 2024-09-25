from rest_framework import serializers
from models.medicalinfos import MedicalInfo


class DriverMedicalInfoSerializer(serializers.ModelSerializer):
    """
    A DriverMedicalInfoSerializer serializer used to serializes Drivers MedicalInfo Model data

    returned field:
        [all]

    Views:
        quiz.views.DriverMedicalInfoViewSet

    Embeded in:
    """

    class Meta:
        model = MedicalInfo
        fields = "__all__"
