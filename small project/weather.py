
from requests import get as rg
city=input("Enter city name: ")
get = rg(f"https://wttr.in/{city}?format=j2")
data = get.json()
try:
    print(f"current {city} Temperature :-{(data['current_condition'][0]['temp_C'])}°C This data may not be accurate")
except ConnectionError:
    print("Check your internet connection")
except KeyError:
    print("City not found")
