from django.shortcuts import render
import requests
from django.core.paginator import Paginator
from newsapi import NewsApiClient


nasa_api_key = 'hKuFyqogFT5y2egU9TjUUdWrEd7PPc7vKmOB5PrY'
news_api_key = 'pub_34807a75f726f36d058d3cfe9af3f2201f82'


def index(request):
    """Página inicial"""

    # APOD API
    info = requests.get(
        f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}')
    info = info.json()

    # NEWS API
    language = 'en'
    q = 'astronomy%20OR%20nasa%20OR%20spacex%20-nazi'
    news = requests.get(
        f'https://newsdata.io/api/1/news?apikey={news_api_key}&language={language}&q={q}')
    news = news.json()
    news = news['results']

    context = {'apod': info, 'news': news}
    return render(request, 'index.html', context)


def apod(request):
    """Fotos atronômicas do dia"""

    info = requests.get(
        f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}')
    info = info.json()
    context = {'apod': info}

    return render(request, 'apod.html', context)


def mars_rover_photos(request):
    """Fotos de Marte"""

    info = requests.get(
        f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={nasa_api_key}')
    info = info.json()
    info = info['photos']

    # Paginação
    paginator = Paginator(info, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'mrp': page_obj}

    return render(request, 'mars_rover_photos.html', context)
