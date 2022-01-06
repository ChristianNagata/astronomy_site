from django.shortcuts import render
import requests


def index(request):
    api_key = 'hKuFyqogFT5y2egU9TjUUdWrEd7PPc7vKmOB5PrY'

    info = requests.get(
        f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={api_key}')

    info = info.json()

    context = {'photos': info['photos'][0]}

    return render(request, 'index.html', context)
