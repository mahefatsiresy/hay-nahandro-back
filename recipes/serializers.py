from rest_framework import serializers
from .models import Image, Ingredient, IngredientQuantity, IngredientType, Recipe


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ["id", "url"]


class IngredientQuantitySerializer(serializers.ModelSerializer):

    # create a name field that is associated with the ingreient.name
    # name = serializers.ReadOnlyField(source="ingredient.name")
    name = serializers.CharField(source="ingredient.name")

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
        source="ingredientquantity_set", many=True
    )

    images = ImageSerializer(many=True)

    class Meta:
        model = Recipe
        fields = "__all__"

    def create(self, validated_data):
        # pop the images and ingredients from the validated_data
        images_data = validated_data.pop("images")
        ingredients_data = validated_data.pop("ingredientquantity_set")

        print(ingredients_data)

        recipe = Recipe.objects.create(**validated_data)

        # create ingredients
        for ingredient_data in ingredients_data:
            # get ingredient from OrdoredDict
            ingredient_d = list(ingredient_data.items())[0][1]

            # create ingredient
            ingredient = Ingredient.objects.create(**ingredient_d)

            # create IngredientQuantity
            IngredientQuantity.objects.create(
                ingredient=ingredient,
                recipe=recipe,
                quantity=list(ingredient_data.items())[1][1],
            )

        # create images
        for image_data in images_data:
            Image.objects.create(recipe=recipe, **image_data)
        return recipe

    # define a custom update method to create a recipe, an ingredient if it does not exist,
    # and a quantity for that ingredient.
    # def update(self, instance, validated_data):
    #     images_data = validated_data.pop("images")

    #     # update recipes
    #     recipe = Recipe.objects.update(**validated_data)

    #     # update images
    #     for image_data in images_data:
    #         Image.objects.update(**image_data)

    #     return recipe
