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
    path('breakfast/', views.BreakfastCreate.as_view(), name='breakfast_create'),
]
