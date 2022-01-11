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

        today = datetime.today().strftime('%Y-%m-%d')
        start_date = today

        neows = requests.get(
            f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&api_key={self.api_key}')
        neows = neows.json()

        dates = neows['near_earth_objects']

        return dates


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
