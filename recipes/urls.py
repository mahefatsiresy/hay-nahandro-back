from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'recipes', viewset=views.RecipeViewSet)
router.register(r'ingredients', viewset=views.IngredientViewSet)
router.register(r'ingredient-types', viewset=views.IngredientTypeViewSet)
router.register(r'images', viewset=views.ImageViewSet)

urlpatterns = [
    path("", include(router.urls))
]
