import requests
import api_key

location = input("Escriba el lugar: ")

params_format = {"q" : location,
                 "units" : "metric",
                 "appid" : api_key.api_key}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params= params_format)

data = response.json()
print(data)