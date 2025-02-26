from django.http import JsonResponse
from django.shortcuts import render

def tictactoe_view(request):
    return render(request, 'tictactoe/tictactoe.html')
