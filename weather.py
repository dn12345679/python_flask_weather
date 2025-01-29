from dotenv import load_dotenv # used for load_dotenv function
from pprint import pprint # pretty print
import requests
import os

load_dotenv() # load the environment variables from .env

def get_current_weather(city = "New York"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions***')

    city = input("\nPlease enter a city name: ")

    # check for empty spring or string with spaces
    if not bool(city.strip()):
        city = "New York" # default if the string is empty
    
    weather_data = get_current_weather(city)
    

    print("\n")
    pprint(weather_data)