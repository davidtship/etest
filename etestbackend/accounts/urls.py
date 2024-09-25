from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views.siteViews import SitesViewSet

router = DefaultRouter()

"""Sites Urls"""
router.register("sites", SitesViewSet, basename="sites")

urlpatterns = [
    path("", include(router.urls)),
]
