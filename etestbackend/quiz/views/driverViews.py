from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from models.drivers import Driver
from models.medicalinfos import MedicalInfo

from ..serializersFolder.driversSerializers import DriverSerializer
from ..serializersFolder.quizscoresSerializers import DriverDetailsSerializers
from ..serializersFolder.medicalinfoSerializers import DriverMedicalInfoSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from utils.caching.deleteCache import delete_cache


class DriverInfoViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

    filterset_fields = ["id", "phone", "email"]
    search_fields = ["email"]
    ordering_fields = ["id"]
    permission_classes = [permissions.IsAuthenticated]

    CACHE_KEY = "driver-info-views"

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY)
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response


class DriverMedicalInfoViewSet(viewsets.ModelViewSet):
    serializer_class = DriverMedicalInfoSerializer
    queryset = MedicalInfo.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    CACHE_KEY = "driver-medical-info"

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY)
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response


class DriverDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = DriverDetailsSerializers
    queryset = Driver.objects.all()
    http_method_names = ["get"]
    permission_classes = [permissions.IsAuthenticated]

    CACHE_KEY = "driver-details"

    @method_decorator(cache_page(60, key_prefix=CACHE_KEY))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
