from rest_framework import permissions
from rest_framework import viewsets

from models.sites import Site
from ..serializers.siteSerializers import SiteSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from utils.caching.deleteCache import delete_cache


class SitesViewSet(viewsets.ModelViewSet):
    serializer_class = SiteSerializer
    queryset = Site.objects.all()

    filterset_fields = ["id", "name", "province", "city"]
    search_fields = ["name"]
    ordering_fields = ["id"]

    permission_classes = [permissions.IsAuthenticated]

    CACHE_KEY = "site-view"

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
