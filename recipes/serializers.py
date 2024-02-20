from rest_framework import serializers
from .models import Ingredient, IngredientQuantity, IngredientType, Recipe


class IngredientQuantitySerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source='ingredient.name')

    class Meta:
        model = IngredientQuantity
        fields = ('name', 'quantity')


class IngredientTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngredientType
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    # ingredient_type = IngredientTypeSerializer()

    class Meta:
        model = Ingredient
        fields = "__all__"


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientQuantitySerializer(
        source="ingredientquantity_set", many=True, read_only=True
    )

    class Meta:
        model = Recipe
        fields = "__all__"
