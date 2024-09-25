from rest_framework import permissions
from rest_framework import viewsets

from models.categories import Category
from ..serializersFolder.categorySerializers import CategorySerializer

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from utils.caching.deleteCache import delete_cache


class CategoryDetailViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving categories.
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAdminUser]

    CACHE_KEY = "category-view"

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
