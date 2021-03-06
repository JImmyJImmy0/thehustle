from os import name
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


TYPES = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    height = models.IntegerField('Height in inches')
    weight = models.IntegerField('Weight in lbs')
    goal_weight = models.IntegerField('Goal weight in lbs')


class Food(models.Model):
    name = models.CharField(max_length=100)
    protein = models.IntegerField('Protein in grams')
    carbs = models.IntegerField('Carbs in grams')
    fat = models.IntegerField('Fat in grams')
    sugar = models.IntegerField('Sugar in grams')
    calories = models.IntegerField()
    sodium = models.IntegerField('Sodium in milligrams')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(
        max_length=1,
        choices=TYPES,
        default=TYPES[0][0]
    )
    date = models.DateField()
    foods = models.ManyToManyField(Food)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meal_details', kwargs={'meal_id': self.id})

    # def lunch_count(self):
    #     return self.lunch_set.filter(name=TYPES[1][0]).count()

    @property
    def get_total_calories(self):
        return sum([food.calories for food in self.foods.all()])

    @property
    def get_total_protein(self):
        return sum([food.protein for food in self.foods.all()])

    @property
    def get_total_carbs(self):
        return sum([food.carbs for food in self.foods.all()])

    @property
    def get_total_fat(self):
        return sum([food.fat for food in self.foods.all()])

    @property
    def get_total_sugar(self):
        return sum([food.sugar for food in self.foods.all()])

    @property
    def get_total_sodium(self):
        return sum([food.sodium for food in self.foods.all()])
    



class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    duration = models.IntegerField('Duration in minutes')
    calories_burned = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name