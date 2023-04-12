# Supla-Virtual-Device-Weather
import requests
import json
import time
import math

# Zdefiniowanie stałych
API_KEY = '<openweathermapapi>'
CITY_NAME = '<your-city>'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'

# Ustawienie ścieżki do folderu dla danych
folder_path = '/home/user/appdata/supla-virtual-device/weather/data/'

# Pobranie danych z API
url = BASE_URL.format(city=CITY_NAME, key=API_KEY)
response = requests.get(url)

# Sprawdzenie, czy zapytanie się powiodło
if response.status_code != 200:
    print('Błąd: Nie udało się pobrać danych z API.')
    exit()

# Pobranie wartości temperatury, wilgotności, ciśnienia, prędkości wiatru, punktu rosy i widoczności z odpowiedzi API
data = json.loads(response.text)
temperature = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind_speed = data['wind']['speed']
clouds = data['clouds']['all']
rain = data['rain']['1h'] if 'rain' in data else 0
snow = data['snow']['1h'] if 'snow' in data else 0
# uv_index = data['current']['uvi']

# Obliczenie punktu rosy
dew_point = round((237.7 * math.log(humidity / 100.0) + (17.27 * temperature)) / (17.27 - math.log(humidity / 100.0)), 2)

# Obliczenie widoczności w km
visibility = round(data['visibility'] / 1000, 2)

# Zapisanie wartości do plików tekstowych
with open(os.path.join(folder_path, 'temperature.txt', 'w') as temp_file:
    temp_file.write('{:.2f}\n'.format(temperature))

with open(os.path.join(folder_path, 'humidity.txt', 'w') as hum_file:
    hum_file.write('{}\n'.format(humidity))

with open(os.path.join(folder_path, 'temp_hum.txt', 'w') as file:
    file.write('{}\n{}\n'.format(temperature, humidity))

with open(os.path.join(folder_path, 'pressure.txt', 'w') as press_file:
    press_file.write('{}\n'.format(pressure))

with open(os.path.join(folder_path, 'wind_speed.txt', 'w') as wind_file:
    wind_file.write('{:.2f}\n'.format(wind_speed))

with open(os.path.join(folder_path, 'dew_point.txt', 'w') as dew_file:
    dew_file.write('{:.2f}\n'.format(dew_point))

with open(os.path.join(folder_path, 'visibility.txt', 'w') as vis_file:
    vis_file.write('{:.2f}\n'.format(visibility))

with open(os.path.join(folder_path, 'clouds.txt', 'w') as vis_file:
    vis_file.write('{:.2f}\n'.format(clouds))

with open(os.path.join(folder_path, 'rain.txt', 'w') as vis_file:
    vis_file.write('{:.2f}\n'.format(rain))

with open(os.path.join(folder_path, 'snow.txt', 'w') as vis_file:
    vis_file.write('{:.2f}\n'.format(snow))

#with open('/home/user/appdata/supla-virtual-device/weather/data/uv_index.txt', 'w') as vis_file:
#    vis_file.write('{:.2f}\n'.format(uv_index))
