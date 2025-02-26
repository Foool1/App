from django.http import JsonResponse
from django.shortcuts import render

def hangman_view(request):
    return render(request, 'hangman/hangman.html')