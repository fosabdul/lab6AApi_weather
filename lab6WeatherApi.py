from datetime import datetime
# import logging
# logging.basicConfig(filename='sample.log' , format='%(asctime)s | %(levelname)s: %(message)s', level=logging.NOTSET)
# logging.debug('Here you have some information for debugging.')

import requests
from key import my_key

from prettytable import PrettyTable
import os

key = os.environ.get('my_key')  # keeping the key code


url = 'https://api.openweathermap.org/data/2.5/forecast'
query = {'q': 'minneapolis,us' , 'units':'imperial', 'appid': key}  

data = requests.get(url, params=query).json()

def main():
    try:
        location = get_location()
        weather_data, error = get_current_weather(location, key)

        if error:
            print('Sorry, could not get weather')

        else:

            get_temp(weather_data)

    except Exception as error:
        print('Recheck errors')
        print(error)

def get_location():

    try:

        city, country = '', ''
        while len(city) == 0:
            city = input('Enter the name of the city: ').strip()

        while len(country) != 2 or not country.isalpha():
            country = input('Enter the 2-leter country code: ').strip()

        location = f'{city}, {country}'
        return location  # return both

    except Exception as e:
        print(e)

def get_current_weather(location , key):
    try:
        query = {'q': location, 'units':'imperial', 'appid': key}
        response = requests.get(url, params=query)
        response.raise_for_status()
        data = response.json()
        return data, None
    except Exception as ex:
        print(ex)
        print(response.text)
        return None, ex

def get_temp(weather_data):
    try:
        list_of_forecast = weather_data['list']
       
        for forecast in list_of_forecast:
            temp = forecast['main']['temp']
            timestamp = forecast['dt']
            desc = forecast['weather'][0]['description'] 
            wind = forecast['wind']['speed']
    
            forecast_date = datetime.fromtimestamp(timestamp)  # forecast for day and time 

           #  create a Table for my 

            table = PrettyTable()  #  I used https://zetcode.com/python/prettytable/ to create my table

            table.title = 'Weather Forecast next 5 days' # title to for the next 5 days I wanted to loop the count the days but didn't work for me 

            table.field_names = ['Date', forecast_date]   # date next 5 days 
            
            table.add_row(['Temparature F', temp]) # temperatue 

            table.add_row(['wind is = ', wind])  # wind 

            table.add_row(['Description', desc]) # desc of the weather 

            print(table) # print the whole table 
            
    except KeyError:
        print('This data is not in the formart expected')
        return 'Unknown'

if __name__ == '__main__':
    main()

"""Part 3:
I'd say printing on console is a primitive way of logging. 
Certainly it helps in some situations but it is not very flexible and for sure is not suitable for servers. 
Logging is when you're writing to files for future analysis. """