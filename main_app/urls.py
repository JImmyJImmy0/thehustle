from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('food/', views.foods_index, name='foods_index'),
    path('foodlog/', views.food_log, name='food_log'),
    path('food/create/', views.FoodCreate.as_view(), name='foods_create'),
    path('food/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'),
    path('exercise/', views.exercise_index, name='exercise_index'),
]
