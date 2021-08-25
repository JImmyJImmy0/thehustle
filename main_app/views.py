from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Exercise, Food


# Create your views here.
def home(request):
    return render(request, 'home.html')


def foods_index(request):
    foods = Food.objects.all()
    return render(request, 'foods/index.html', { 'foods': foods })

def food_log(request):
    foods = Food.objects.all()
    return render(request, 'foods/log.html', { 'foods': foods })

def exercises_index(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises/index.html', { 'exercises': exercises })

class FoodCreate(CreateView):
    model = Food
    fields = '__all__'
    success_url = '/food/'

class FoodDelete(DeleteView):
    model = Food
    success_url = '/food/'

class ExerciseCreate(CreateView):
    model = Exercise
    fields = '__all__'
    success_url = '/exercise/'