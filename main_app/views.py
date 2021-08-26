from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Exercise, Food, Profile


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'


def foods_index(request):
    foods = Food.objects.all()
    return render(request, 'foods/index.html', { 'foods': foods })

def food_log(request):
    foods = Food.objects.all()
    return render(request, 'foods/log.html', { 'foods': foods })

def exercises_index(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises/index.html', { 'exercises': exercises })

def exercise_log(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises/log.html', { 'exercises': exercises })


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

class ExerciseDelete(DeleteView):
    model = Exercise
    success_url = '/exercise/'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile(user_id = user.id).save()
            login(request, user)
            return redirect('foods_index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)