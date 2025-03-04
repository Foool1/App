import requests, datetime

from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from django.shortcuts import render
from pprint import pprint


def weather_view(request):
    return render(request, 'api_weather/api_weather.html')


class weatherAPIView(APIView):

    def get(self, request):
        city = request.GET.get('weather')
        if not city:
            return Response ({'error': 'No city in request'}, status=status.HTTP_400_BAD_REQUEST)  # noqa
        weather_info = weatherGenerator(city)
        print('dupa123')
        print(weatherGenerator(city))
        return Response(weather_info, status=status.HTTP_200_OK)


def weatherGenerator(city):
    API = '2f42268437c101f743db3fefe02bfa4a'
    url = f"http://api.openweathermap.org/data/2.5/weather?appid={API}&q={city}&units=metric"  # noqa

    weather_data = requests.get(url).json()
    pprint(weather_data)
    sunrise = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise']+3600)
    sunset = datetime.datetime.fromtimestamp(weather_data['sys']['sunset']+3600)
    print(sunrise.strftime('%H:%M:%S'))
    print(sunset.strftime('%H:%M:%S'))
    if 'weather' in weather_data and 'main' in weather_data:
        return {
            'temperature': weather_data['main']['temp'],
            'perceived': weather_data['main']['feels_like'],
            'humidity': weather_data['main']['humidity'],
            'description': weather_data['weather'][0]['description'],
            'city': weather_data['name'],
            'wind': weather_data['wind']['speed'],
            'pressure': weather_data['main']['pressure'],
            'sunrise': sunrise.strftime('%H:%M:%S'),
            'sunset': sunset.strftime('%H:%M:%S'),
        }
    else:
        return {'error': 'City not found'}
