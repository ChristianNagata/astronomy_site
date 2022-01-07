from django.shortcuts import render
import requests


api_key = 'hKuFyqogFT5y2egU9TjUUdWrEd7PPc7vKmOB5PrY'


def index(request):
    """Página inicial"""

    return render(request, 'index.html')


def apod(request):
    """Fotos atronômicas do dia"""

    info = requests.get(
        f'https://api.nasa.gov/planetary/apod?api_key={api_key}')
    info = info.json()
    context = {'apod': info}

    return render(request, 'apod.html', context)


def mars_rover_photos(request):
    """Fotos de Marte"""

    info = requests.get(
        f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={api_key}')
    info = info.json()

    context = {'mrp': info}

    return render(request, 'mars_rover_photos.html', context)
