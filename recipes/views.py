from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Ingredient, IngredientType, Recipe
from .serializers import IngredientSerializer, IngredientTypeSerializer, RecipeSerializer

# Create your views here.


# recipe
class RecipeList(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


# ingredient
class IngredientList(ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetail(RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


# ingredient type
class IngredientTypeList(ListCreateAPIView):
    queryset = IngredientType.objects.all()
    serializer_class = IngredientTypeSerializer


class IngredientTypeDetail(RetrieveUpdateDestroyAPIView):
    queryset = IngredientType.objects.all()
    serializer_class = IngredientTypeSerializer
