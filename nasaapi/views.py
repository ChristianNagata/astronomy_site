from django.shortcuts import render
import requests


api_key = 'hKuFyqogFT5y2egU9TjUUdWrEd7PPc7vKmOB5PrY'


def index(request):
    return render(request, 'index.html')


def apod(request):
    info = requests.get(
        f'https://api.nasa.gov/planetary/apod?api_key={api_key}')
    info = info.json()

    context = {'apod': info}

    return render(request, 'apod.html', context)
