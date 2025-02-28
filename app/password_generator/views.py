from django.http import JsonResponse
from django.shortcuts import render
import random


def generate_password(length):
    chars = 'abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ!@£$%^&*()?01234356789'  # noqa
    password = ''
    if length < 4:
        return 'password to short'
    elif length > 32:
        return 'password to long'

    for y in range(length):
        password += random.choice(chars)
    return password

def password_generator_page_view(request):
    """Widok renderujący stronę HTML"""
    return render(request, 'generate_password.html')


def password_generator_view(request):
    length = request.GET.get('length', 12)
    length = int(length)
    password = generate_password(length)
    return JsonResponse({'password': password})
