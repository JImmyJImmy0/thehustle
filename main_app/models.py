from django.db import models
from django.urls import reverse

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    protein = models.IntegerField()
    carbs = models.IntegerField()
    fat = models.IntegerField()
    sugar = models.IntegerField()
    calories = models.IntegerField()
    sodium = models.IntegerField()

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('foods_index', kwargs={'food_id': self.id})


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    duration = models.IntegerField()
    calories_burned = models.IntegerField()

    def __str__(self):
        return self.name