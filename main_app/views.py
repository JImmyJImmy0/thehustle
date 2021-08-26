from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Exercise, Food


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
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('createprofile')
        else:
            error_message = 'Invalid sign up - try again'

    user_form = UserCreationForm()
    context = {'user_form': user_form, 'error_message': error_message}
    return render(request, 'signup.html', context)


def createprofile(request):
    error_message = ''
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('foods_index')
        else:
            error_message = 'Invalid - try again'

    profile_form = ProfileForm()
    context = {'profile_form': profile_form, 'error_message': error_message}
    return render(request, 'createprofile.html', context)
