from os import error
from django.db.models import query
from django.db.models.aggregates import Sum
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm, UpdateProfileForm
from .models import Exercise, Food, Meal, Profile




# Create your views here.
class Home(LoginView):
    template_name = 'home.html'


@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'profile.html', { 'profile': profile })


@login_required
def foods_index(request):
    foods = Food.objects.filter(user=request.user)
    return render(request, 'foods/index.html', { 'foods': foods })


@login_required
def food_log(request):
    foods = Food.objects.filter(user=request.user)
    meals = Meal.objects.filter(user=request.user)
    profile = Profile.objects.filter(user=request.user)
    # total_calories = Sum([foods.calories for foods in meals.food.all])
    return render(request, 'foods/log.html', { 'foods': foods, 'meals': meals, 'profile': profile })


@login_required
def exercises_index(request):
    exercises = Exercise.objects.filter(user=request.user)
    return render(request, 'exercises/index.html', { 'exercises': exercises })


@login_required
def exercise_log(request):
    exercises = Exercise.objects.filter(user=request.user)
    return render(request, 'exercises/log.html', { 'exercises': exercises })


@login_required
def meal_details(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    profile = Profile.objects.filter(user=request.user)
    unadded_foods = Food.objects.exclude(id__in = meal.foods.all().values_list('id'))
    return render(request, 'meals/meal_details.html', {'meal': meal, 'foods': unadded_foods, 'profile': profile })


class MealCreate(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ['name', 'date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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


@login_required
def assoc_food(request,  meal_id, food_id):
    Meal.objects.get(id=meal_id).foods.add(food_id)
    return redirect('meal_details', meal_id=meal_id)


@login_required
def disassoc_food(request, meal_id, food_id):
    Meal.objects.get(id=meal_id).foods.remove(food_id)
    return redirect('meal_details', meal_id=meal_id)


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
            user_profile = profile_form.save()
            Profile(user_id = user_profile.id).save()
            return redirect('foods_index')
        else:
            error_message = 'Invalid - try again'

    profile_form = ProfileForm()
    context = {'profile_form': profile_form, 'error_message': error_message}
    return render(request, 'createprofile.html', context)


def updateprofile(request):
    error_message = ''
    if request.method == 'POST':
        update_profile_form = UpdateProfileForm(request.POST)
        if update_profile_form.is_valid():
            update_profile_form.save()
            return redirect('profile')
        else:
            error_message = 'Invalid - try again'

    update_profile_form = UpdateProfileForm()
    context = {'update_profile_form': update_profile_form, 'error_message': error_message}
    return render(request, 'updateprofile.html', context)

