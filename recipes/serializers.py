from rest_framework import serializers
from .models import Image, Ingredient, IngredientQuantity, IngredientType, Recipe


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"


class IngredientQuantitySerializer(serializers.ModelSerializer):

    # create a name field that is associated with the ingreient.name
    name = serializers.ReadOnlyField(source="ingredient.name")

    class Meta:
        model = IngredientQuantity
        fields = ("name", "quantity")


class IngredientTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngredientType
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = "__all__"


class RecipeSerializer(serializers.ModelSerializer):
    # return ingredient name with its quantity
    # the source is from recipes.models.IngredientQuantity model
    # read_only is set here for now to allow fast update during development
    ingredients = IngredientQuantitySerializer(
        source="ingredientquantity_set", many=True, read_only=True
    )

    images = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    )

    class Meta:
        model = Recipe
        fields = "__all__"
