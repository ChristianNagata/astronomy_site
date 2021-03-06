from django.shortcuts import render
from .apis import *
from django.core.paginator import Paginator


def index(request):
    """Página inicial"""

    info = NasaAPI()
    news = NewsAPI()
    general = GeneralInfo()

    apod = info.apod_api()
    news = news.news_api()
    weather = info.insight_api()
    general_info = general.count()

    context = {
        'apod': apod,
        'objs_count': general_info,
        'news': news,
        'weather': weather['AT'],
        'page_info': {
            'name': 'Home',
            'title': 'Welcome to The Astronomy.',
            'description': 'The objective of this site is to make NASA APIs, including imagery, eminently accessible to educators, and citizen scientists.'
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
            'description': 'One of the most popular websites at NASA is the Astronomy Picture of the Day. In fact, this website is one of the most popular websites across all federal agencies. It has the popular appeal of a Justin Bieber video.'
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
            'description': "This API is designed to collect image data gathered by NASA's Curiosity, Opportunity, and Spirit rovers on Mars and make it more easily available to other developers, educators, and citizen scientists."
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
            'description': "This API is designed to collect image data gathered by NASA's Curiosity, Opportunity, and Spirit rovers on Mars and make it more easily available to other developers, educators, and citizen scientists."
        }
    }
    return render(request, 'mars_rover_photo.html', context)


def neows(request):
    """NeoWs (Near Earth Object Web Service)"""

    info = NasaAPI()
    general = GeneralInfo()

    info_api = info.neows_api()
    info_api = info_api['near_earth_objects']

    objects = general.all()

    # Ordenando a lista por periculosidade
    def byHazardous(e):
        return e['is_potentially_hazardous_asteroid']
    objects.sort(reverse=True, key=byHazardous)

    # Objects informations
    count = general.count()
    haz_count = general.hazardous()
    biggest = general.biggest()
    approach = general.approach()

    context = {
        'objects': objects,
        'count': count,
        'haz_count': haz_count,
        'approach': approach,
        'biggest': biggest['name'],
        'page_info': {
            'name': 'NeoWs',
            'title': 'Near Earth Objects Web Service',
            'description': 'Multiple lines of text that form the lede, informing new readers quickly and efficiently about what’s most interesting in this post’s contents.'
        }
    }
    return render(request, 'neows.html', context)
