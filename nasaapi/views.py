from django.shortcuts import render
import requests
from django.core.paginator import Paginator


api_key = 'hKuFyqogFT5y2egU9TjUUdWrEd7PPc7vKmOB5PrY'


def index(request):
    """Página inicial"""

    info = requests.get(
        f'https://api.nasa.gov/planetary/apod?api_key={api_key}')
    info = info.json()
    context = {'apod': info}

    return render(request, 'index.html', context)


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
    info = info['photos']

    # Paginação
    paginator = Paginator(info, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'mrp': page_obj}

    return render(request, 'mars_rover_photos.html', context)
