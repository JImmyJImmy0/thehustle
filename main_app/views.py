from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Food


# Create your views here.
def home(request):
    return render(request, 'home.html')


def foods_index(request):
    foods = Food.objects.all()
    return render(request, 'foods/index.html', { 'foods': foods })

class FoodCreate(CreateView):
    model = Food
    fields = '__all__'
    success_url = '/food/'

class FoodDelete(DeleteView):
    model = Food
    success_url = '/food/'