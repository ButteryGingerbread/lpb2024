from django.shortcuts import render
from .forms import Login, RegisterForm
from datetime import datetime
from django.http import JsonResponse
from .models import UserProfile
from django.db.transaction import TransactionManagementError
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, transaction
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import json
import bcrypt

# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "POST":
        jsonBody = json.loads(request.body)
        form = RegisterForm({
            'username': jsonBody.get('username'),
            'email': jsonBody.get('email'),
            'password1': jsonBody.get('password1'),
            'password2': jsonBody.get('password2')
        })

        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save(commit=False)
                    user.set_password(jsonBody['password1'])
                    user.save()

                return JsonResponse({'status': 'true', 'message': "User registered successfully."}, status=200)
            except IntegrityError as e:
                return JsonResponse({'status': 'false', 'message': str(e)}, status=500)

        errors = form.errors.as_json()
        return JsonResponse({'status': 'false', 'message': "Form is not valid.", 'errors': errors}, status=500)

    return JsonResponse({'status': 'false', 'message': "Only POST method is allowed."}, status=500)


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            jsonBody = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'false', 'message': "invalid JSON"}, status=400)
        
        form = Login(jsonBody)
        UserModel = get_user_model()
        
        if form.is_valid():
            email = form.cleaned_data['email']
            passwordText = form.cleaned_data['password']
            
            try:
                user = UserModel.objects.get(email=email)
            except UserModel.DoesNotExist:
                return JsonResponse({'status': 'false', 'message': "user name or password invalid"}, status=400)
            
            userLogin = authenticate(username=user.username, password=passwordText)
            if userLogin is not None:
                return JsonResponse({'status':'true','message':"login success"}, status=200)
            
            return JsonResponse({'status': 'false', 'message': "user name or password invalid"}, status=400)
        
        return JsonResponse({'status':'false','message':"form not valid"}, status=400)
    
    return JsonResponse({'status':'false','message':"request method not valid"}, status=400)
    