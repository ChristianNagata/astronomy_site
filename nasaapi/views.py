from django.shortcuts import render
from .apis import *
from django.core.paginator import Paginator


def index(request):
    """Página inicial"""

    info = NasaAPI()
    info = info.apod_api()

    news = NewsAPI()
    news = news.news_api()

    context = {'apod': info, 'news': news, 'page_name': 'Home'}
    return render(request, 'index.html', context)


def apod(request):
    """Fotos atronômicas do dia"""

    info = NasaAPI()
    info = info.apod_api()

    context = {'apod': info, 'page_name': 'APOD'}
    return render(request, 'apod.html', context)


def mars_rover_photos(request):
    """Fotos de Marte"""

    info = NasaAPI()
    info = info.mrp_api()

    # Paginação
    paginator = Paginator(info, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'mrp': page_obj, 'page_name': 'Mars Photos'}

    return render(request, 'mars_rover_photos.html', context)
