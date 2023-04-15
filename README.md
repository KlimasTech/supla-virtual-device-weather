# supla-virtual-device-weather
Skrypt pobierający informacje pogodowe z openweathermap ( https://openweathermap.org/ ) do plików txt które można wykorzystać w supla-virtual-device i wyświetlić w supli.

# Instalacja supla-virtual-device
1. Tworzymy folder appdata w swoim folderze użytkownika: mkdir /home/user/appdata/
> sudo apt-get update;

> git clone https://github.com/lukbek/supla-virtual-device.git

> cd supla-virtual-device

## !!! UWAGA !!!
W razie problemów z uruchomieniem supla-virtual-device należy edytować plik:  Należy dopisać w 36 lini pliku /home/user/appdata/supla-virtual-device/src/supla-dev/src/pi_2_mmio.h słowo „extern tak ma potem wyglądać ta linia
extern volatile uint32_t* pi_2_mmio_gpio;”

> ./install.sh
2. Edytujemy plik: supla-virtual-device.cfg i wklejamy zawartość z repozytorium
3. Dodajemy wpis w crontab -e
> @reboot /home/user/appdata/supla-virtual-device/supla-virtual-device/svd.sh
4. Nadajemy uprawnienia do uruchamiania
> chmod +x /home/user/appdata/supla-virtual-device/supla-virtual-device/svd.sh

# Instalacja supla-virtual-device-weather
1. Pobieramy skrypt weather.py do folderu /home/user/appdata/supla-virtual-device/weather/
2. Tworzymy podfolder data na nasze dane pogodowe.
3. Dodajemy uruchamianie co 10minut w: crontab -e
> */10 * * * * python3 /home/user/appdata/supla-virtual-device/weather/weather.py
