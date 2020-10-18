### Wymagania
Python 3.6+

### Przygotowanie środowiska
Zaleca się stworzyć wirtualne środowisko dla projektu:
```
python3 -m venv venv
```
Utworzone środowisko należy aktywować:

* Windows:
```
venv\Scripts\activate.bat
```
* Unix/Mac:
```
source venv/bin/activate
```
Oraz zainstalować zależności:
```
pip install -r requirements.txt
```

### Uruchamianie testów
Wszystkie testy można uruchomić przez wydanie polecenia `pytest` lub selektywnie przez `pytest <path/to/test>`