# Julia Ingram
# Homework 3
# 2021-11-07

import requests
import json

# PART ONE

# 1. What is the URL to the documentation?
# https://pokeapi.co/docs/v2

# 2. What pokemon has the ID of 55?
response = requests.get("https://pokeapi.co/api/v2/pokemon/slowpoke")
pokemon55 = response.json()
print(f"{pokemon55['name']} has an ID of 55")

# 3. How tall is that pokemon?
print(f"{pokemon55['name']} is {pokemon55['height']*4} inches tall")

# 4. How many versions of Pokemon games have been released?
response = requests.get("https://pokeapi.co/api/v2/version/")
versions = response.json()
#print(json.dumps(versions, indent=3))
print(f"{versions['count']} versions of Pokemon games have been released")

# 5. Print out the name of every electric-type pokemon.
response = requests.get("https://pokeapi.co/api/v2/type/electric")
electric_pokemon = response.json()
#print(json.dumps(electric_pokemon, indent=3))
#print(electric_pokemon['pokemon']) #list of dictionaries
electric_pokemon_names = []
for pokemon in electric_pokemon['pokemon']:
    electric_pokemon_names.append(pokemon['pokemon']['name'])
print(f"The names of every electric Pokemon: {electric_pokemon_names}")

# 6. What are electric-type Pokemon called in the Korean version of the game?
for name in electric_pokemon['names']:
    if name['language']['name'] == 'ko':
        electric_korean = name['name'] #should print '전 기'
print(f"In Koren, electric type pokemon are called {electric_korean}")

# 7. Who has a higher speed stat, Eevee or Pikachu?
response = requests.get("https://pokeapi.co/api/v2/pokemon/eevee")
eevee = response.json()
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
pikachu = response.json()
#print(json.dumps(eevee, indent=3))
#print(pikachu['stats'])
def get_speed(pokemon):
    for stat in pokemon['stats']:
        if stat['stat']['name'] == 'speed':
            return stat['base_stat']

if get_speed(eevee) > get_speed(pikachu):
    print("Eevee has a higher speed stat than Pikachu")
else: print("Pikachu has a higher speed stat than Eevee")


# PART TWO 
# My API key: 861adbf540334018bfc22522210511

# 1. What is the URL to the documentation?
# https://www.weatherapi.com/docs/

# 2. Make a request for the current weather where you are born, or somewhere you've lived.
response = requests.get("http://api.weatherapi.com/v1/current.json?key=861adbf540334018bfc22522210511&q=11357")
current_whitestone_weather = response.json()
print(json.dumps(current_whitestone_weather, indent=3))

# 3. Print out the country this location is in.
print(f"Whitestone, NY is in {current_whitestone_weather['location']['country']}")

# 4. Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.
realfeel_diff = round(current_whitestone_weather['current']['temp_f'] - current_whitestone_weather['current']['feelslike_f'])
if realfeel_diff > 0:
    print(f"It feels {realfeel_diff} degrees colder than it actually is")
elif realfeel_diff < 0:
    print(f"It feels {abs(realfeel_diff)} degrees warmer than it actually is")
else: print("It feels like the temperature it actually is")

# 5. What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.
response = requests.get("http://api.weatherapi.com/v1/forecast.json?key=861adbf540334018bfc22522210511&q=iata:LHR")
heathrow_airport = response.json()
print(f"The current temperature at Heathrow International Airport is {heathrow_airport['current']['temp_c']} degrees Celcius, or {heathrow_airport['current']['temp_f']} degrees Fahrenheit")

# 6. What URL would I use to request a 3-day forecast at Heathrow?
url = "http://api.weatherapi.com/v1/forecast.json?key=861adbf540334018bfc22522210511&q=iata:LHR&days=3"
print(f"The URL to request a 3-day forecast at Heathrow: {url}")
response = requests.get(url)
forecast = response.json()

# 7. Print the date of each of the 3 days you're getting a forecast for.
forecast_dates = []
for item in forecast['forecast']['forecastday']:
    forecast_dates.append(item['date'])
print(forecast_dates)
print(f"The dates of each of the three days of the forecast are: {forecast_dates}")

# 8. Print the maximum temperature of each of the days.
#print(json.dumps(forecast['forecast'], indent=3))
maxtemps = []
maxtemps_dict = {}
for item in forecast['forecast']['forecastday']:
    maxtemps.append(item['day']['maxtemp_c'])

for i in range(3):
    maxtemps_dict[forecast_dates[i]] = maxtemps[i]

print(f"The maximum temperature on each date in degrees Celcius: {maxtemps_dict}")

# 9. Print the day with the highest maximum temperature.
for key, value in maxtemps_dict.items():
    if value == max(maxtemps_dict.values()):
        print(f"The day with the highest maximum temperature is {key}")
#print(key for key, value in maxtemps_dict.items() if value == max(maxtemps_dict.values()))

