# Generated by Django 5.0.1 on 2024-02-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_ingredientquantity_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='images',
            field=models.TextField(),
        ),
    ]
