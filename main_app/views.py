from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

class Food:
    def __init__(self, name, protein, carbs, fat, sugar, calories, sodium):
        self.name = name
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.sugar = sugar
        self.calories = calories
        self.sodium = sodium
    
foods = [
    Food('Chip', 1, 10, 4, 2, 100, 300)
]

def foods_index(request):
    return render(request, 'foods/index.html', { 'foods': foods })