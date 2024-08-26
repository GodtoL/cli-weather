import requests
import api_key
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--location', type=str, required=True)

args = parser.parse_args()

location = args.location

params_format = {"q" : location,
                 "units" : "metric",
                 "appid" : api_key.api_key}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params= params_format)

data = response.json()
print(data)