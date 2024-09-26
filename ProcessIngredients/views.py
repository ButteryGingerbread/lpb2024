from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
from .models import Customer, Menu

@csrf_exempt
def filter_recipes(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            if not isinstance(data, dict):
                return JsonResponse({'error': 'Invalid data format'}, status=400)

            customer_name = data.get('customerName')
            scanned_ingredients = data.get('scannedIngredients', [])

            if not customer_name:
                return JsonResponse({'error': 'Customer name is required'}, status=400)
            
            try:
                customer = Customer.objects.get(name=customer_name)
            except Customer.DoesNotExist:
                return JsonResponse({'error': 'Customer not found'}, status=404)
            
            customer_condition = customer.condition

            ingredient_filter = Q()
            for ingredient in scanned_ingredients:
                ingredient_filter |= Q(menu_ingredients__icontains=ingredient)

            filtered_menus = Menu.objects.filter(ingredient_filter).filter(menu_category__icontains=customer_condition)

            if filtered_menus.exists():
                # menu_list = [menu.serialize() for menu in filtered_menus]
                menu_list = []
                for menu in filtered_menus:
                    menu_list.append(menu.serialize())
                return JsonResponse(menu_list, safe=False, status=200)
            else:
                return JsonResponse([], status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)
