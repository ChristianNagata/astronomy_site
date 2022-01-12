import requests
from datetime import datetime


class NasaAPI:
    """Retora as APIs da NASA"""

    def __init__(self):
        self.api_key = 'hKuFyqogFT5y2egU9TjUUdWrEd7PPc7vKmOB5PrY'

    def apod_api(self):
        """APOD - Astronomy Photos of the Day"""

        apod = requests.get(
            f'https://api.nasa.gov/planetary/apod?api_key={self.api_key}')
        apod = apod.json()
        return apod

    def mrp_api(self):
        """Mars Rover Photos"""

        mrp = requests.get(
            f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={self.api_key}')
        mrp = mrp.json()
        mrp = mrp['photos']
        return mrp

    def neows_api(self):
        """Near Earth Objects"""

        neows = requests.get(
            f'https://api.nasa.gov/neo/rest/v1/feed?detailed=true&api_key={self.api_key}')
        neows = neows.json()
        near_objs = neows['near_earth_objects']

        return near_objs

    def neows_general(self):
        """Near Earth Objects count"""

        info = self.neows_api()
        dates = info.keys()

        objects = []
        for date in dates:
            for obj in info[date]:
                objects.append(obj)
        objs_count = len(objects)

        def byHazardous(e):
            return e['is_potentially_hazardous_asteroid']
        objects.sort(reverse=True, key=byHazardous)
        haz_count = 0
        for obj in objects:
            if obj['is_potentially_hazardous_asteroid']:
                haz_count += 1

        return {'count': objs_count, 'haz_count': haz_count}


class NewsAPI:
    """Retorna a API de notícias"""

    def __init__(self):
        self.api_key = 'pub_34807a75f726f36d058d3cfe9af3f2201f82'

    def news_api(self):
        language = 'en'
        q = 'astronomy%20OR%20nasa%20OR%20spacex%20-nazi'
        news = requests.get(
            f'https://newsdata.io/api/1/news?apikey={self.api_key}&language={language}&q={q}')
        news = news.json()
        news = news['results']
        return news
