import requests
from pprint import pprint

import OS

from datetime import datetime


def main():

    key = os.environ.get('weather_key')

    query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}
    url = 'http://api.openweathermap.org/data/2.5/weather'
        
    data = requests.get(url, params=query).json()

    weather_description = data['weather'] [0]['description']

    temperature_f = data['main']['temp']

    pprint(f'The weather is {weather_description}, the temperature is {temperature_f:.2f}F.')

    #    for forecast in forecast_item:
    #    Timestamp = forecast['dt']
    #    date = datetime.fromtimestamp(Timestamp)
    #    temp = forecast['main']['temp']



if __name__ == '__main__':

    main()