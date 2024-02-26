from datetime import date
from django.db import models


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
    cover_image = models.TextField()
    created_at = models.DateField(default=date.today())
    ingredients = models.ManyToManyField(Ingredient, through="IngredientQuantity")

    def __str__(self):
        return self.name


class IngredientQuantity(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)


class Image(models.Model):
    url = models.TextField()
    recipe = models.ForeignKey(Recipe, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return self.url


class UploadedFile(models.Model):
    file = models.ImageField()
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uploaded_on.date()
