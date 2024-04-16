from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import User
import json

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        User.objects.create(username=username, password=password)
        return JsonResponse({'message': 'User registered successfully'}, status=201)
    return JsonResponse({'error': 'This method is not allowed'}, status=405)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            return JsonResponse({'message': 'Login successful'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return JsonResponse({'error': 'This method is not allowed'}, status=405)

