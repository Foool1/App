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
            removeImage('result.png')
            imageEncoder(url)
            return Response(url, status=status.HTTP_200_OK)
        return Response(url, status=status.HTTP_200_OK)


class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('image')
        if not file_obj:
            return Response({"message": "Image not sent!"}, status=status.HTTP_400_BAD_REQUEST)  # noqa

        script_dir = os.path.dirname(os.path.abspath(__file__))
        static_images_dir = os.path.join(script_dir, 'static', 'images')
        filepath = os.path.join(static_images_dir, 'uploaded_image.png')

        os.makedirs(static_images_dir, exist_ok=True)

        removeImage('uploaded_image.png')

        try:
            with open(filepath, 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)
            time.sleep(0.1)

            result = urlreturn(filepath)
            return Response({"filename": result}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": f"Error processing image: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # noqa


def urlreturn(filepath):
    try:
        with Image.open(filepath) as link:
            result = decode(link)
            if not result:
                return "No QR code found"
            decoded_object = result[0]
            link_bytes = decoded_object.data
            return link_bytes.decode('utf-8')
    except Exception as e:
        raise Exception(f"Error decoding QR code: {str(e)}")


def imageEncoder(link):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    static_images_dir = os.path.join(script_dir, 'static', 'images')

    os.makedirs(static_images_dir, exist_ok=True)

    img = qrcode.make(link)
    filepath = os.path.join(static_images_dir, 'result.png')
    img.save(filepath)
    return filepath


def removeImage(name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    static_images_dir = os.path.join(script_dir, 'static', 'images')
    filepath = os.path.join(static_images_dir, name)

    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            time.sleep(0.1)
            return True
        return False
    except Exception:
        return False
