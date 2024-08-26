import requests
import api_key

city = input("Escriba la ciudad: ")

params_format = {"q" : city,
                 "units" : "metric",
                 "appid" : api_key.api_key}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params= params_format)

data = response.json()
print(data)