from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Menu
import json

# Create your views here.

@csrf_exempt
def display_all(request):
    if request.method == 'GET':
        menus = Menu.objects.all()
        return JsonResponse([menu.serialize() for menu in menus], safe=False)
    return JsonResponse({'status':'false','message':"request method not valid"}, status=500)

@csrf_exempt
def display_by_category(request, menu_category):
    if request.method == 'GET':
        menu_items = Menu.objects.filter(menu_category=menu_category)
        return JsonResponse([menu.serialize() for menu in menu_items], safe=False)
    return JsonResponse({'status':'false','message':"request method not valid"}, status=500)