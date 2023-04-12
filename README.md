# supla-virtual-device-weather
Skrypt pobierający informacje pogodowe z openweather do plików txt które można wykorzystać w supla-virtual-device i wyświetlić w supli.

# Instalacja supla-virtual-device-weather
1. Pobieramy skrypt weather.py do folderu /home/user/appdata/supla-virtual-device/weather/
2. Tworzymy podfolder data na nasze dane pogodowe.
3. Dodajemy uruchamianie co 10minut w: crontab -e
> */10 * * * * python3 /home/user/appdata/supla-virtual-device/weather/weather.py
