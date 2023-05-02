import requests
import json
import time
import math

# Zdefiniowanie stałych
API_KEY = '<api-key>'
CITY_NAME = '<city>'
LAT = '<lat'
LON = '<lon>'

# Ustawienie ścieżki do folderu dla danych
folder_path = '/home/user/appdata/supla-virtual-device/weather/data/'

# Pobranie danych POGODOWYCH z API
response = requests.get("https://api.openweathermap.org/data/2.5/weather", params={"lat": LAT, "lon": LON, "appid": API_KEY, "units": "metric"})

# Sprawdzenie, czy zapytanie się powiodło
if response.status_code != 200:
    print('Błąd: Nie udało się pobrać danych POGODOWYCH z API.')
    exit()

# Pobranie wartości temperatury, wilgotności, ciśnienia, prędkości wiatru, punktu rosy i widoczności z odpowiedzi API
data = json.loads(response.text)
temperature = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind_speed = data['wind']['speed']
clouds = data['clouds']['all']

# Obliczanie opadów deszczu w l/m
rain_data = data['rain']['1h'] if 'rain' in data else 0
rain = rain_data * 100

# Obliczanie opadów śniegu l/m
snow_data = data['snow']['1h'] if 'snow' in data else 0
snow = snow_data * 100

# Obliczenie punktu rosy
dew_point = round((237.7 * math.log(humidity / 100.0) + (17.27 * temperature)) / (17.27 - math.log(humidity / 100.0)), 2)

# Obliczenie widoczności w km
# visibility = round(data['visibility'] / 1000, 2)
# Obliczanie widoczności w m
visibility = round(data['visibility'])

# Pobieranie wskaznika UVI
response = requests.get("https://api.openweathermap.org/data/2.5/uvi", params={"lat": LAT, "lon": LON, "appid": API_KEY})

# Sprawdzenie, czy zapytanie się powiodło
if response.status_code != 200:
    print('Błąd: Nie udało się pobrać danych UVI z API.')
    exit()

# Pobranie wartości wskaźnika UV
data = response.json()
uv_index = data["value"]

# Zapisanie wartości do plików tekstowych
with open(folder_path + 'temperature.txt', 'w') as temp_file:
    temp_file.write('{:.2f}\n'.format(temperature))

with open(folder_path + 'humidity.txt', 'w') as hum_file:
    hum_file.write('{}\n'.format(humidity))

with open(folder_path + 'temp_hum.txt', 'w') as temp_hum_file:
    temp_hum_file.write('{}\n{}\n'.format(temperature, humidity))

with open(folder_path + 'pressure.txt', 'w') as press_file:
    press_file.write('{}\n'.format(pressure))

with open(folder_path + 'dew_point.txt', 'w') as dew_file:
    dew_file.write('{:.2f}\n'.format(dew_point))

with open(folder_path + 'wind_speed.txt', 'w') as wind_file:
    wind_file.write('{:.2f}\n'.format(wind_speed))

with open(folder_path + 'clouds.txt', 'w') as clouds_file:
    clouds_file.write('{:.2f}\n'.format(clouds))

with open(folder_path + 'visibility.txt', 'w') as vis_file:
    vis_file.write('{:.2f}\n'.format(visibility))

with open(folder_path + 'rain.txt', 'w') as rain_file:
    rain_file.write('{:.2f}\n'.format(rain))

with open(folder_path + 'snow.txt', 'w') as snow_file:
    snow_file.write('{:.2f}\n'.format(snow))

with open(folder_path + 'uv_index.txt', 'w') as uv_file:
    uv_file.write('{:.2f}\n'.format(uv_index))
