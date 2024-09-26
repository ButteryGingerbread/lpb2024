from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Customer
from .forms import CustomerForm
import json

# View to list all customers
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        customer_list = [
            {
                'name': customer.name,
                'condition': customer.condition
            }
            for customer in customers
        ]
        return JsonResponse(customer_list, safe=False)

# View to create a new customer
@csrf_exempt
def create_customer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = CustomerForm(data)

            if form.is_valid():
                customer = form.save()  # Save the customer if the form is valid
                response = {
                    'message': 'Customer created successfully',
                    'customer': {
                        'name': customer.name,
                        'condition': customer.condition
                    }
                }
                return JsonResponse(response, status=201)
            else:
                return JsonResponse({'errors': form.errors}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)