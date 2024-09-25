from rest_framework import permissions
from rest_framework import viewsets

from models.answers import Answer
from ..serializersFolder.answersSerializers import AnswersSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from utils.caching.deleteCache import delete_cache


class AnswersViewSet(viewsets.ModelViewSet):
    serializer_class = AnswersSerializer
    queryset = Answer.objects.all()

    filterset_fields = ["id", "answer_text", "is_right", "question"]
    search_fields = ["answer_text"]
    ordering_fields = ["id"]
    permission_classes = [permissions.IsAdminUser]

    CACHE_KEY = "answer-view"

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
