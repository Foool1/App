from django.shortcuts import render  # noqa
from django.http import JsonResponse  # noqa


def background_remover_view(request):
    return render(request, 'background_remover/background_remover.html')
