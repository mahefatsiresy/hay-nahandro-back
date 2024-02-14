from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("", include("recipes.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
