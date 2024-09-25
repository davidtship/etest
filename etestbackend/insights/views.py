from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets

# Create your views here.

from .tasks import get_results

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class AnalysisView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]

    def get_queryset(self):
        return super().get_queryset()

    CACHE_KEY = "question-view"

    @method_decorator(cache_page(60, key_prefix=CACHE_KEY))
    def list(self, request, *args, **kwargs):
        results = get_results.apply_async()
        return Response(results.get())
