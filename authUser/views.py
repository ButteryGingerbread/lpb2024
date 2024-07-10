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
        form = RegisterForm(jsonBody)
        
        if form.is_valid():
            birth_date = jsonBody.get('birth_date')
            gender = jsonBody.get('gender')
            condition = jsonBody.get('condition')
            
            try:
                dateTime = datetime.strptime(birth_date, '%d-%m-%Y')
            except ValueError:
                return JsonResponse({'status': 'false', 'message': "Invalid date format. Use dd-mm-yyyy."}, status=500)

            try:
                with transaction.atomic():
                    user = form.save(commit=False)
                    user.set_password(jsonBody['password1'])
                    user.save()
                    
                    userProfile = UserProfile.objects.create(
                        user_id=user.id,
                        birth_date=dateTime,
                        gender=gender,
                        condition=condition
                    )

                return JsonResponse({'status': 'true', 'message': "User registered successfully."}, status=200)
            except IntegrityError as e:
                return JsonResponse({'status': 'false', 'message': str(e)}, status=500)

        errors = form.errors.as_json()
        return JsonResponse({'status': 'false', 'message': "Form is not valid.", 'errors': errors}, status=500)

    return JsonResponse({'status': 'false', 'message': "Only POST method is allowed."}, status=500)

@csrf_exempt 
def login_view(request):
    if request.method == 'POST':
        jsonBody = json.loads(request.body)
        form = Login(jsonBody)
        UserModel = get_user_model()
        # check if the form is valid, IF NOT RETURN ERROR
        if form.is_valid():
            email = jsonBody['email']
            passwordText = jsonBody['password']
            try:
                user = UserModel.objects.get(email=email)
            except ObjectDoesNotExist as e:
                return JsonResponse({'status': 'false', 'message': "user name or password invalid"}, status = 500)
            
            userLogin = authenticate(username=user.__dict__['username'], password=jsonBody['password'])
            if user is not None:
                return JsonResponse({'status':'true','message':"login success"}, status=200)
            
            return JsonResponse({'status': 'false', 'message': "failed login"}, status = 500)
        return JsonResponse({'status':'false','message':"form not valid"}, status=500)
    return JsonResponse({'status':'false','message':"request method not valid"}, status=500)
    