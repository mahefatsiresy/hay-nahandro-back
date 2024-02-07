from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


router = routers.DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("recipes/", include("recipes.urls")),
    path("admin/", admin.site.urls),
]
