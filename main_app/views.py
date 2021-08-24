from django.shortcuts import render
from .models import Food


# Create your views here.
def home(request):
    return render(request, 'home.html')


def foods_index(request):
    foods = Food.objects.all()
    return render(request, 'foods/index.html', { 'foods': foods })