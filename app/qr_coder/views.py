from django.http import JsonResponse  # noqa
from django.shortcuts import render  # noqa


def qr_code_view(request):
    return render(request, 'qr_coder/qr_coder.html')
