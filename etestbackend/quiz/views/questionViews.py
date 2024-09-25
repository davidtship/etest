from rest_framework import permissions
from rest_framework import viewsets

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from utils.caching.deleteCache import delete_cache

from models.questions import Question
from ..serializersFolder.questionsSerializers import (
    QuestionSerializer,
    QuestionWithOptionSerializer,
)


class QuestionsViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    filterset_fields = ["id", "title", "is_active"]
    search_fields = ["title"]
    ordering_fields = ["is_active", "id"]

    CACHE_KEY = "question-view"

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

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """

        if self.action == "list":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class QuestionsWithOptionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionWithOptionSerializer
    queryset = Question.objects.all()
    http_method_names = ["get"]

    permission_classes = [permissions.IsAuthenticated]

    filterset_fields = ["id", "title", "is_active"]
    search_fields = ["title"]
    ordering_fields = ["is_active", "id"]

    CACHE_KEY = "question-with-options-view"

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
