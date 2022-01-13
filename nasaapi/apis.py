from audioop import reverse
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
        near_objs = neows

        return near_objs

    def insight_api(self):
        """Mars Weather"""

        info = requests.get(
            'https://mars.nasa.gov/rss/api/?feed=weather&category=insight_temperature&feedtype=json&ver=1.0')
        info = info.json()

        sol_keys = info['sol_keys']
        sol_keys.sort(reverse=True)
        last_key = sol_keys[0]

        weather = info[last_key]
        return weather


class GeneralInfo:
    def __init__(self):
        self.info = NasaAPI()

    def all(self):
        info_newos = self.info.neows_api()
        info_api = info_newos['near_earth_objects']

        dates = info_api.keys()
        objects = []
        for date in dates:
            for obj in info_api[date]:
                objects.append(obj)
        return objects

    def count(self):
        """Total of near objects"""
        info_newos = self.info.neows_api()
        info_newos = info_newos['element_count']
        return info_newos

    def hazardous(self):
        """Total of hazardous objects"""
        objects = self.all()
        haz_count = 0
        for obj in objects:
            if obj['is_potentially_hazardous_asteroid']:
                haz_count += 1
        return haz_count

    def biggest(self):
        """The biggest object"""
        objects = self.all()

        def bySize(e):
            return e['estimated_diameter']['meters']['estimated_diameter_max']
        objects.sort(reverse=True, key=bySize)
        biggest = objects[0]
        return biggest

    def approach(self):
        """Close approach date"""
        objects = self.all()

        objects.sort(key=lambda x: datetime.strptime(
            x['close_approach_data'][0]['close_approach_date'], '%Y-%m-%d'))
        close = objects[0]
        return close['close_approach_data'][0]['close_approach_date_full']


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
