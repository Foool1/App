from django.shortcuts import render

def ocr_view(request):
    return render(request, 'ocr.html')