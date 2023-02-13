from django.db import models

# Create your models here.
class Recipedb(models.Model):
    recipe_name = models.CharField(max_length=10)
    recipe_image = models.ImageField(upload_to='Recipedb')
    ingredients = models.TextField(max_length=200)
    instructions = models.TextField(max_length=200)
