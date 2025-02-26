from django.http import JsonResponse
from django.shortcuts import render


def timer_view(request):
    return render(request, 'timer/timer.html')
