from django.shortcuts import render
from .apis import *
from django.core.paginator import Paginator


def index(request):
    """Página inicial"""

    info = NasaAPI()
    info = info.apod_api()

    news = NewsAPI()
    news = news.news_api()

    context = {
        'apod': info,
        'news': news,
        'page_info': {
            'name': 'Home',
            'title': 'Stay informed about the Universe',
            'description': 'Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.'
        }
    }
    return render(request, 'index.html', context)


def apod(request):
    """Fotos atronômicas do dia"""

    info = NasaAPI()
    info = info.apod_api()

    context = {
        'apod': info,
        'page_info': {
            'name': 'APOD',
            'title': 'Astronomy Picture of the Day',
            'description': 'Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.'
        }
    }
    return render(request, 'apod.html', context)


def mars_rover_photos(request):
    """Fotos de Marte"""

    info = NasaAPI()
    info = info.mrp_api()

    # Paginação
    paginator = Paginator(info, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'mrp': page_obj,
        'page_info': {
            'name': 'Mars Rover Photos',
            'title': 'Mars Rover Photos',
            'description': 'Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.'
        }
    }
    return render(request, 'mars_rover_photos.html', context)


def mars_rover_photo(request, photo_id):
    """Foto de Marte"""

    info = NasaAPI()
    info = info.mrp_api()

    # Seleciona a foto de id = photo_id
    for photo in info:
        if photo['id'] == photo_id:
            info = photo
            break

    context = {
        'photo': info,
        'page_info': {
            'name': 'Mars Rover Photo',
            'title': 'Mars Rover Photo',
            'description': 'Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.'
        }
    }
    return render(request, 'mars_rover_photo.html', context)
