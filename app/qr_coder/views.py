from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from django.shortcuts import render

import qrcode, os, time

def qr_code_view(request):
    return render(request, 'qr_coder/qr_coder.html')


class encoderAPIView(APIView):

    def get(self, request):
        if 'url' in request.GET:
            url = request.GET.get('url')
            print(url)
            removeImage()
            imageEncoder(url)
            return Response(url, status=status.HTTP_200_OK)
        return Response(url, status=status.HTTP_200_OK)

def imageEncoder(link):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    static_images_dir = os.path.join(script_dir, 'static', 'images')

    if not os.path.exists(static_images_dir):
        os.makedirs(static_images_dir)

    img = qrcode.make(link)
    filepath = os.path.join(static_images_dir, 'result.png')
    img.save(filepath)

def removeImage():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    static_images_dir = os.path.join(script_dir, 'static', 'images')
    filepath = os.path.join(static_images_dir, 'result.png')

    if os.path.exists(filepath):
        os.remove(filepath)
        time.sleep(1)
        return True
    else:
        return False