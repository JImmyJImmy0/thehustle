from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    protein = models.IntegerField()
    carbs = models.IntegerField()
    fat = models.IntegerField()
    sugar = models.IntegerField()
    calories = models.IntegerField()
    sodium = models.IntegerField()