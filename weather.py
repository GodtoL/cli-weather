import requests
import api_key
import argparse
import csv
import json

parser = argparse.ArgumentParser(description= "Obtén el clima del lugar que quieras")
parser.add_argument('--lugar', type=str, required=True, help="Escriba aquí el lugar del de que deseas saber los datos")
parser.add_argument('--formato', type=str, default='json', help= "Ingrese el formato en el que desee (json, text, csv)")

args = parser.parse_args()

location = args.lugar
format_data = args.formato

params_format = {
    "q": location,
    "units": "metric",
    "appid": api_key.api_key,
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather", params=params_format
)
data = response.json()

if format_data == 'json':
    
    with open("clima.json", "w") as j:
        json.dump(data, j)

elif format_data == 'txt':
    t = open("clima.txt", "a")
    temp = data['main']['temp']
    t.write(f"En {location} la temperatura es de {temp} C°")
    t.close()

elif format_data == 'csv':

    # Escribir los datos en un archivo CSV
    with open('CLIMACSV','a') as csvfile:
        fieldnames = ['Ciudad', 'Temperatura', 'Descripción']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        writer.writerow(
            {'Ciudad': location, 'Temperatura': temp, 'Descripción': description}
        )

    print("csv generado con éxito")
else:
    print(f"Error{data['cod']}. Algo ha salido mal")