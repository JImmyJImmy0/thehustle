from django.contrib import admin
from .models import Food, Exercise, Profile, Meal

# Register your models here.
admin.site.register(Food)
admin.site.register(Exercise)
admin.site.register(Profile)
admin.site.register(Meal)