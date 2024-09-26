from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.customer_list, name='customer_list'),
    path('create/', views.create_customer, name='create_customer')
]
