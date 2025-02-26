from django.http import JsonResponse

from django.shortcuts import render
from .Utils.Password_generator import generate_password
# Create your views here.

def password_generator_page_view(request):
    """Widok renderujący stronę HTML"""
    return render(request, 'generate_password.html')

def password_generator_view(request):
    length = request.GET.get('length', 12)
    length = int(length)
    print(length)
    password = generate_password(length)  # Generowanie hasła
    print(password)
    return JsonResponse({'password': password})