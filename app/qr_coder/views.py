from django.http import JsonResponse
from django.shortcuts import render

def qr_code_view(request):
    return render(request, 'qr_coder/qr_coder.html')