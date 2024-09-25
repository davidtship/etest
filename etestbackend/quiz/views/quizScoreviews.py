from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import permissions
import json


### serializers
from ..serializersFolder.quizscoresSerializers import *


### models

from models.quizscores import QuizScore
from models.quizanswers import QuizAnswers

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from utils.caching.deleteCache import delete_cache


class QuizScoreViewSet(viewsets.ModelViewSet):
    serializer_class = QuizScoreSerializer
    queryset = QuizScore.objects.all()

    filterset_fields = ["id", "driver", "test_type", "schedule_on", "taken"]
    search_fields = ["test_type"]
    ordering_fields = ["schedule_on", "taken", "score"]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        """
        pass request attribute to serializer
        """
        context = super(QuizScoreViewSet, self).get_serializer_context()
        return context

    CACHE_KEY = "quiz-score-view"

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


class QuizScoreWithDriverEmbeddedViewSet(viewsets.ModelViewSet):
    serializer_class = QuizScoreWithDriverEmbeddedSerializer
    queryset = QuizScore.objects.all()

    http_method_names = ["get"]
    permission_classes = [permissions.IsAuthenticated]

    filterset_fields = ["id", "test_type", "schedule_on", "taken"]
    search_fields = ["test_type"]
    ordering_fields = ["schedule_on", "taken", "score"]

    def get_queryset(self):
        if self.request.user.is_admin:
            return QuizScore.objects.all()
        else:
            return QuizScore.objects.filter(site=self.request.user.site)

    CACHE_KEY = "QuizScoreWithDriverEmbeddedViewSet"

    @method_decorator(cache_page(5, key_prefix=CACHE_KEY))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DriverAnsweredQuizDetailViewSet(viewsets.ModelViewSet):
    serializer_class = QuizAnswersSerializer
    queryset = QuizAnswers.objects.all()
    http_method_names = ["get"]
    filterset_fields = ["question", "answer", "id"]
    permission_classes = [permissions.IsAuthenticated]

    CACHE_KEY = "DriverAnsweredQuizDetailViewSet"

    @method_decorator(cache_page(60, key_prefix=CACHE_KEY))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class QuizScoreWithAnswersEmbbededViewSet(viewsets.ModelViewSet):
    serializer_class = QuizScoreWithAnswersSerializer
    queryset = QuizScore.objects.all()

    filterset_fields = [
        "id",
        "driver",
        "test_type",
        "schedule_on",
        "taken",
        "site",
    ]
    search_fields = ["test_type"]
    ordering_fields = [
        "schedule_on",
        "taken",
    ]

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return QuizScore.objects.all()
        else:
            return QuizScore.objects.filter(site=self.request.user.site)

    def get_serializer_context(self):
        """
        pass request attribute to serializer
        """
        context = super(
            QuizScoreWithAnswersEmbbededViewSet, self
        ).get_serializer_context()
        return context

    CACHE_KEY = "QuizScoreWithAnswersEmbbededViewSet"

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

    permission_classes = [permissions.IsAuthenticated]
