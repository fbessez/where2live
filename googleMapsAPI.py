import requests
import json

googleMapsURL = 'https://maps.googleapis.com/maps/api/geocode/json'


# I could even do zip code!
def get_city_details(location):
    params = {
        "sensor": "false",
        "address": location
    }
    r = requests.get(googleMapsURL, params=params)
    results = r.json()['results']
    return results[0]['address_components']

def filter_results_for_state_name(results):
    stateObject = list(filter(lambda x: 'administrative_area_level_1' in x['types'], results))[0]
    return stateObject['long_name']

def filter_results_for_state_abbrev(results):
    stateObject = list(filter(lambda x: 'administrative_area_level_1' in x['types'], results))[0]
    return stateObject['short_name']

def filter_results_for_city_name(results):
    cityObject = list(filter(lambda x: 'locality' in x['types'], results))[0]
    return cityObject['long_name']

def convertCityToState(city):
    return filter_results_for_state_name(get_city_details(city))

def convertInputToCity(input_city):
    return filter_results_for_city_name(get_city_details(input_city))
