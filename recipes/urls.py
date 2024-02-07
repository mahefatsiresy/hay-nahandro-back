from django.urls import path
from rest_framework.routers import format_suffix_patterns

from . import views


urlpatterns = [
    path("", views.RecipeList.as_view()),
    path("<int:pk>/", views.RecipeDetail.as_view()),
    path("ingredients/", views.IngredientList.as_view()),
    path("ingredients/<int:pk>/", views.IngredientDetail.as_view()),
    path("ingredient-types/", views.IngredientTypeList.as_view()),
    path("ingredient-types/<int:pk>", views.IngredientTypeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
