from django.db import models

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    images = models.CharField(max_length=255)


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
