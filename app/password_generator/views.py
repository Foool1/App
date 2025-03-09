from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from django.shortcuts import render
import random



def password_generator_page_view(request):
    return render(request, 'generate_password.html')


class PasswordGeneratorAPIView(APIView):
    def generate_password(self, length):
        chars = 'abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ!@£$%^&*()?01234356789'  # noqa
        password = ''
        if length < 4:
            return 'password to short'
        elif length > 32:
            return 'password to long'

        for y in range(length):
            password += random.choice(chars)
        return password

    def get(self, request):
        try:
            length = int(request.GET.get('length', 12))
        except ValueError:
            return Response({'error': 'Invalid length parameter'}, status=status.HTTP_400_BAD_REQUEST)  # noqa

        password = self.generate_password(length)
        return Response({'password': password}, status=status.HTTP_200_OK)
