from datetime import date
from django.db import models
from django.utils import timezone


class IngredientType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    ingredient_type = models.ForeignKey(
        IngredientType, on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    images = models.TextField()
    created_at = models.DateField(default=timezone.now())
    ingredients = models.ManyToManyField(Ingredient, through="IngredientQuantity")

    def __str__(self):
        return self.name


class IngredientQuantity(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
