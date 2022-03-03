
from sqlite3 import Timestamp
import requests
from pprint import pprint

import os


from datetime import datetime

key = os.environ.get('weather_key')

query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}

url = 'http://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()

pprint(data)


list_of_forecasts = data['list']

for forecast in list_of_forecasts:
    temp = forecast['main'] ['temp']
    timestamp = forecast['dt']
    forecast_date = datetime.fromtimestamp(timestamp)

    print(f'at {forecast_date} the temperature will be {temp}.F')


