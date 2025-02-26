from django.http import JsonResponse
from django.shortcuts import render

def weather_view(request):
    return render(request, 'api_weather/api_weather.html')
