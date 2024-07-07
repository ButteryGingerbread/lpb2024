from django.urls import path
from . import views

urlpatterns = [
    path("display-all", views.display_all),
    path("display-data/<str:menu_category>", views.display_by_category)
]