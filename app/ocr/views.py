from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from django.shortcuts import render
import pytesseract # type: ignore
from PIL import Image
import os
import time
def ocr_view(request):
    return render(request, 'ocr.html')


class ocrAPIView(APIView):
    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('image')
        if not file_obj:
            return Response({"message": "Image not sent!"}, status=status.HTTP_400_BAD_REQUEST)  # noqa

        script_dir = os.path.dirname(os.path.abspath(__file__))
        static_images_dir = os.path.join(script_dir, 'static', 'images')
        filepath = os.path.join(static_images_dir, 'input.png')

        os.makedirs(static_images_dir, exist_ok=True)
        removeImage("input.png")

        try:
            with open(filepath, 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)

            result = ocr_image(filepath)
            return Response({"filename": result}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"message": f"Error processing image: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # noqa


def ocr_image(filepath):


    print("Ścieżka do pliku:", filepath)
    print("Czy plik istnieje?", os.path.exists(filepath))

    print("Rozpoznany tekst:")
    try:
        if not os.path.exists(filepath):
            return "Plik nie istnieje!"

        img = Image.open(filepath)

        text = pytesseract.image_to_string(img)
        print(text)
        return text

    except Exception as e:
        return f"Wystąpił błąd: {str(e)}"

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
