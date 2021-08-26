from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    height = models.IntegerField('Height in inches')
    weight = models.IntegerField('Weight in lbs')
    goal_weight = models.IntegerField('Goal weight in lbs')


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    protein = models.IntegerField('Protein in grams')
    carbs = models.IntegerField('Carbs in grams')
    fat = models.IntegerField('Fat in grams')
    sugar = models.IntegerField('Sugar in grams')
    calories = models.IntegerField()
    sodium = models.IntegerField('Sodium in milligrams')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('foods_index', kwargs={'food_id': self.id})


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    duration = models.IntegerField('Duration in minutes')
    calories_burned = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name