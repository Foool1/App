import requests
from pprint import pprint

API = '2f42268437c101f743db3fefe02bfa4a'

print("Input city: ")
city = str(input())

url = f"http://api.openweathermap.org/data/2.5/weather?appid={API}&q={city}"

weather_data = requests.get(url).json()

pprint(weather_data)