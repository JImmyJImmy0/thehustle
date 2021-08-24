from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('food/', views.foods_index, name='foods_index'),
]