from django.shortcuts import render
from .apis import *
from django.core.paginator import Paginator


def index(request):
    """Página inicial"""

    info = NasaAPI()
    apod = info.apod_api()
    newos_general = info.neows_general()

    news = NewsAPI()
    news = news.news_api()

    context = {
        'apod': apod,
        'objs_count': newos_general['count'],
        'news': news,
        'page_info': {
            'name': 'Home',
            'title': 'Stay informed about the Universe',
            'description': 'Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.'
        }
    }
    return render(request, 'index.html', context)


def apod(request):
    """Foto atronômica do dia"""

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


def neows(request):
    """NeoWs (Near Earth Object Web Service)"""

    info = NasaAPI()
    info_api = info.neows_api()
    dates = info_api.keys()

    objects = []
    for date in dates:
        for obj in info_api[date]:
            objects.append(obj)

    # Ordenando a lista por periculosidade
    def byHazardous(e):
        return e['is_potentially_hazardous_asteroid']
    objects.sort(reverse=True, key=byHazardous)

    # Objects count
    newos_general = info.neows_general()

    context = {
        'objects': objects,
        'count': newos_general['count'],
        'haz_count': newos_general['haz_count'],
        'page_info': {
            'name': 'NeoWs',
            'title': 'Near Earth Objects Web Service',
            'description': 'Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.'
        }
    }
    return render(request, 'neows.html', context)
