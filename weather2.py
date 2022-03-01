from sqlite3 import Timestamp
from urllib import response
import requests
from pprint import pprint

from datetime import datetime

import os

key = os.environ.get('weather_key')

url = 'http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,mn,us&unit=imperail&appid=6cf37af777f011473a5a8a47cb157798'

# url = 'http://api.openweathermap.org/data/2.5/weather'




def main():

    location = get_location()
    weather_data, error = get_current_weather(location, key)

    if error:
        print('Sorry, could not get weather')

    else:
        current_temp = get_temp(weather_data)
        print(f'The current temperature is {current_temp}')



def get_location():
    city, country = '', ''

    while len(city) == 0:
        city = input('Enter the name of the city:').strip()

    while len(country) != 2 or not country.isalpha():
        country = input('Enter the 2-letter country code: ').strip()


    location = f'{city}, {country}'

    return location

def get_current_weather(location, key):
    try:
        query = {'q': location, 'units': 'metric', 'appid': key}
        response = requests.get(url, params=query)
        response.raise_for_status()

        data = response.json()
        return data , None

    except Exception as ex:
        print(ex)
        print(response.text) # where is this file

        return None, ex


    # print(f'The weather at {date}, the temperature is {temp}F.')

def get_temp(weather_data):

    try:
        temp = weather_data['main'] ['temp']
        return temp

    except KeyError:
        print('This data is not in the fromate expected')

        return 'Unknown'


if __name__ == '__main__':

    main()