from rest_framework import viewsets
from .models import Ingredient, IngredientType, Recipe
from .serializers import IngredientSerializer, IngredientTypeSerializer, RecipeSerializer

# Create your views here.


class RecipeViewSet(viewsets.ModelViewSet):
    """
    This class provide `list`, `create`, `update`, `retreive`
    and `delete` actions for recipe
    """
    queryset = Recipe.objects.prefetch_related('ingredients')
    serializer_class = RecipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientTypeViewSet(viewsets.ModelViewSet):
    queryset = IngredientType.objects.all()
    serializer_class = IngredientTypeSerializer
