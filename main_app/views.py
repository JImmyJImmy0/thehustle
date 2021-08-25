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

def exercise_index(request):
    exercise = Exercise.objects.all()
    return render(request, 'exercises/index.html', { 'exercise': exercise })

class FoodCreate(CreateView):
    model = Food
    fields = '__all__'
    success_url = '/food/'

class FoodDelete(DeleteView):
    model = Food
    success_url = '/food/'