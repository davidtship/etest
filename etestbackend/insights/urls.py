from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("summary", views.AnalysisView, basename="insights-1")

urlpatterns = [
    # path("summary/", views.AnalysisView.as_view(), name="data"),
    path("", include(router.urls)),
]
