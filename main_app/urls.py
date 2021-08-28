from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('food/', views.foods_index, name='foods_index'),
    path('foodlog/', views.food_log, name='food_log'),
    path('food/create/', views.FoodCreate.as_view(), name='foods_create'),
    path('food/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'),
    path('exercise/', views.exercises_index, name='exercises_index'),
    path('exerciselog/', views.exercise_log, name='exercise_log'),
    path('exercise/create/', views.ExerciseCreate.as_view(), name='exercises_create'),
    path('exercise/<int:pk>/delete', views.ExerciseDelete.as_view(), name='exercises_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/createprofile/', views.createprofile, name='createprofile'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.updateprofile, name='updateprofile'),
    path('meal/create', views.MealCreate.as_view(), name='meal_create'),
    path('meal/<int:meal_id>/', views.meal_details, name='meal_details'),
    path('meal/<int:meal_id>/assoc_food/<int:food_id>', views.assoc_food, name='assoc_food')
]
