import requests
from django.shortcuts import render
from .models import City

def index(request):
    city = 'Las Vegas'

#    cities = City.object.all()

    weather_data = []

#    for city in cities:
    #    url = None
    #    r = requests.get(url).json()

    #    city_weather = {
    #        'city': city.name,
    #        'temperature': r['main']['temp'],
    #        'description': r['weather'][0]['description'],
    #        'icon': r['weather'][0]['icon']
    #    }
#        weather_data.append(city_weather)

#    context = {'weather_data': weather_data}
#    return render(request, 'weather_app/weather_app.html', context)
    return render(request, 'weather_app/weather_app.html')
