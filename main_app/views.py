from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm
from .models import Exercise, Food


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

@login_required
def foods_index(request):
    foods = Food.objects.filter(user=request.user)
    return render(request, 'foods/index.html', { 'foods': foods })


@login_required
def food_log(request):
    foods = Food.objects.filter(user=request.user)
    return render(request, 'foods/log.html', { 'foods': foods })


@login_required
def exercises_index(request):
    exercises = Exercise.objects.filter(user=request.user)
    return render(request, 'exercises/index.html', { 'exercises': exercises })


@login_required
def exercise_log(request):
    exercises = Exercise.objects.filter(user=request.user)
    return render(request, 'exercises/log.html', { 'exercises': exercises })


class FoodCreate(LoginRequiredMixin, CreateView):
    model = Food
    fields = ['name', 'calories', 'protein', 'carbs', 'fat', 'sugar', 'sodium']
    success_url = '/food/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FoodDelete(LoginRequiredMixin, DeleteView):
    model = Food
    success_url = '/food/'


class ExerciseCreate(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ['name', 'description', 'duration', 'calories_burned']
    success_url = '/exercise/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExerciseDelete(LoginRequiredMixin, DeleteView):
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
