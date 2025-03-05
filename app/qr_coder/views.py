from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from django.shortcuts import render

import qrcode, os

def qr_code_view(request):
    return render(request, 'qr_coder/qr_coder.html')


class encoderAPIView(APIView):

    def get(self, request):
        if 'url' in request.GET:
            url = request.GET.get('url')
            print(url)
            imageEncoder(url)
            return Response(url, status=status.HTTP_200_OK)
        return Response(url, status=status.HTTP_200_OK)

def imageEncoder(link):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pictures_dir = os.path.join(script_dir, 'pictures')
    if not os.path.exists('pictures'):
        os.makedirs('pictures')

    img = qrcode.make(link)
    filepath = os.path.join(pictures_dir, 'result.png')
    img.save(filepath)