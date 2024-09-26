from django.urls import path
from . import views

urlpatterns = [
    path("display-all/", views.display_all),
    path("display-data/<str:menu_category>", views.display_by_category),
    path("menu-detail/<int:menu_id>/", views.menu_detail),
    path('filter-recipes/', views.filter_recipes_by_ingredients, name='filter_recipes'),
]