# coding=utf-8
import json
import requests

api_base_url_cities = "https://api.teleport.org/api/cities/"
api_base_url_urban_areas = "https://api.teleport.org/api/urban_areas/"

headers = {
    "Accept": "application/vnd.teleport.v1+json"
}

def extract_id_from_url(city_url):
    last_index_of_backslash = city_url.rfind('/')
    return city_url[last_index_of_backslash + 1:]

def get_city_by_name(name):
    try:
        name = name.replace(' ', '%20')
        url = "%s?search=%s&limit=1" % (api_base_url_cities, name)
        r = requests.get(url, headers=headers)
        return r.json()
    except Exception as e:
        print("Error:", e)

def get_all_urban_areas():
    try:
        r = requests.get(api_base_url_urban_areas, headers=headers)
        return r.json()['_links']['ua:item']
    except Exception as e:
        print('Error:', e)

def get_urban_details(urban_id):
    try:
        url = "%s%s/details/" % (api_base_url_urban_areas, urban_id)
        r = requests.get(url, headers=headers)
        return r.json()['categories']
    except Exception as e:
        print('Error:', e)

def get_salaries_in_urban_area(urban_id):
    try:
        url = "%s%s/salaries/" % (api_base_url_urban_areas, urban_id)
        r = requests.get(url, headers=headers)
        return r.json()['salaries']
    except Exception as e:
        print('Error:', e)

def find_city_id_by_name(name):
    response = get_city_by_name(name)
    try:
        if response['_embedded']['city:search-results'] > 0:
            city_url = response['_embedded']['city:search-results'][0]['_links']['city:item']['href'][:-1]
            city_id = extract_id_from_url(city_url)
            return city_id
        return False
    except:
        return False

def find_urban_area_id_by_name(name):
    all_urban_areas = get_all_urban_areas()
    urban_area_filter = list(filter(lambda x: name in x['name'], all_urban_areas))
    if len(urban_area_filter) > 0:
        # Takes top result of filter
        urban_area_url = urban_area_filter[0]['href'][:-1]
        urban_area_id = extract_id_from_url(urban_area_url)
        return urban_area_id
    else:
        return False


def filter_urban_details(name):
    # Important ID:
    # HOUSING
    # COST-OF-LIVING
    # JOB-MARKET
    # NETWORK
    # STARTUPS
    important_ids = ['HOUSING', 'COST-OF-LIVING']
    urban_area_id = find_urban_area_id_by_name(name)
    categories = get_urban_details(urban_area_id)
    return list(filter(lambda x: x['id'] in important_ids, categories))

def sum_cost_of_living(category):
    data = category['data']
    total_cost = 0
    multiplier = 0
    for item in data:
        try:
            dollar_value = item['currency_dollar_value']
            item_name = item['label']
            total_cost += dollar_value
        except:
            if item['id'] == 'CONSUMER-PRICE-INDEX-TELESCORE':
                multiplier = 5
            elif item['id'] == 'RENT-INDEX-TELESCORE':
                multiplier = .33
    return total_cost * multiplier

def get_urban_cost_by_name(name):
    categories = filter_urban_details(name)
    total_sum_monthly = 0
    for category in categories:
        total_sum_monthly += sum_cost_of_living(category)
    return int(total_sum_monthly)

def filter_jobs(salaries, jobtitle):
    return list(filter(lambda x: jobtitle in x['job']['title'], salaries))

def find_salary(cityname, jobtitle):
    listy = []
    urban_id = find_urban_area_id_by_name(cityname)
    salaries = get_salaries_in_urban_area(urban_id)
    jobs = filter_jobs(salaries, jobtitle)
    print('jobs', jobs)
    return int(jobs[0]['salary_percentiles']['percentile_50'])
