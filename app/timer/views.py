from django.http import JsonResponse
from django.shortcuts import render
from Utils.timer import timer

def timer_view(request):
    return render(request, 'timer/timer.html')

def timer_api_view(request):
    time = request.GET.get('length', 12)
    time = int(time)
    time = timer(time)
    return JsonResponse({'time': time})