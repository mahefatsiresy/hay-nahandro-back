from django.contrib import admin

from .models import Ingredient, IngredientType, Recipe

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(IngredientType)
admin.site.register(Recipe)
