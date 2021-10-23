from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests
load_dotenv()


def index(request):

    if request.method == 'POST':
        city = request.POST['city']
        weatherKey = os.getenv('WEATHER_API_KEY')

        print(city)
        weatherUrl = 'http://api.openweathermap.org/data/2.5/weather?q=' + \
            city + '&units=metric&appid='+weatherKey

        weatherResponse = requests.get(weatherUrl).json()

        data = {
            "country_name": str(weatherResponse['name']),
            "country_code": str(weatherResponse['sys']['country']),
            "coordinate": str(weatherResponse['coord']['lon']) + ', '
            + str(weatherResponse['coord']['lat']),

            "temp": str(weatherResponse['main']['temp']) + ' °C',
            "pressure": str(weatherResponse['main']['pressure']),
            "humidity": str(weatherResponse['main']['humidity']),
            'main': str(weatherResponse['weather'][0]['main']),
            'description': str(weatherResponse['weather'][0]['description']),
            'icon': weatherResponse['weather'][0]['icon'],
            #    "https://api.openweathermap.org/data/2.5/weather?q=India&appid=34f1c45eaa110091273e7ed0e38cc698"
        }
        print(data)
        print()
    else:
        return(HttpResponse('Api Crash'))

    return render(request, "index.html", data)


def insta(request):
    return render(request, 'index.html')
# Create your views here.
