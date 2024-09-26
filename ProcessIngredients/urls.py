from django.urls import path
from . import views

urlpatterns = [
    path('record/', views.record_ingredients, name='record_ingredients'),
    path('filter-recipes/', views.filter_recipes, name='filter_recipes')
]
