from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Menu
from.models import Customer
import json

# Create your views here.

#@login_required
def display_all(request):
    if request.method == 'GET':
        menus = Menu.objects.all()
        menu_list = [menu.serialize() for menu in menus]
        return JsonResponse({'menus': menu_list})
    return JsonResponse({'status': 'false', 'message': "request method not valid"}, status=500)


#@login_required
@csrf_exempt
def display_by_category(request, menu_category):
    if request.method == 'GET':
        menu_items = Menu.objects.filter(menu_category=menu_category)
        return JsonResponse([menu.serialize() for menu in menu_items], safe=False)
    return JsonResponse({'status':'false','message':"request method not valid"}, status=500)

#@login_required
@csrf_exempt
def menu_detail(request, menu_id):
    try:
        menu = Menu.objects.get(id=menu_id)
        return JsonResponse(menu.serialize(), safe=False)
    except Menu.DoesNotExist:
        return JsonResponse({'status': 'false', 'message': "menu not found"}, status=404)

@csrf_exempt
def filter_recipes_by_ingredients(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        customer_name = data.get('customerName', '')
        scanned_ingredients = data.get('scannedIngredients', [])
        
        if not scanned_ingredients:
            return JsonResponse({'error': 'No ingredients provided'}, status=400)
        
        # Fetch the customer to get their condition
        try:
            customer = Customer.objects.get(name=customer_name)
            condition = customer.condition
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)
        
        # Filter menus based on ingredients and condition
        query = Menu.objects.filter(
            menu_ingredients__iregex=r'(' + '|'.join(scanned_ingredients) + ')',
            menu_category__icontains=condition  # Assuming menu_category represents condition here
        )
        
        # Serialize the query results
        results = [menu.serialize() for menu in query]
        
        return JsonResponse({'status': 'success', 'recipes': results}, status=200)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)

