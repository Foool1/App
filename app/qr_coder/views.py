from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from django.shortcuts import render
from pyzbar.pyzbar import decode
from PIL import Image
import qrcode
import os
import time


def qr_code_view(request):
    return render(request, 'qr_coder/qr_coder.html')


class encoderAPIView(APIView):

    def get(self, request):
        if 'url' in request.GET:
            url = request.GET.get('url')
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

class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('image')
        if not file_obj:
            return Response({"message": "Nie przesłano obrazu!"}, status=status.HTTP_400_BAD_REQUEST)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        static_images_dir = os.path.join(script_dir, 'static', 'images')
        filepath = os.path.join(static_images_dir, 'uploaded_image.png')
        print("chuj")

        if not os.path.exists(static_images_dir):
            os.makedirs(static_images_dir)

        with open(filepath, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        return Response({
            "message": "Obraz został zapisany!",
            "filename": file_obj.name
        }, status=status.HTTP_201_CREATED)
