#Using this youtube tutorial: https://www.youtube.com/watch?v=9P5MY_2i7K8  to get temperature at requested location

import datetime as dt
import requests

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "d8689764d384f4e0d91249bf557f48d0"
city = "Grimstad"

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()

#print(response)

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin -273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

temp_kelvin = response ['main']['temp']
print(temp_kelvin)
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
print(temp_celsius)


