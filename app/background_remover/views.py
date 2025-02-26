from django.shortcuts import render
from django.http import JsonResponse

def background_remover_view(request):
    return render(request, 'background_remover/background_remover.html')