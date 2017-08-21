import requests
import googleMapsAPI
from bs4 import BeautifulSoup
try:
    from urllib.request import urlopen
except:
    from urllib import urlopen

def exPatistanScrape(query):
    query = query.replace(' ', '-')
    url = 'https://www.expatistan.com/cost-of-living/%s?currency=USD' % query
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find_all('table', {'class': 'comparison single-city'})
    res = {}
    for row in table[0].find_all('tr'):
        try:
            label = row.find('td', {'class': 'item-name'}).text.strip()
            value = row.find('td', {'class': 'price city-1'}).text.strip()
            res[label] = value
            value2 = row.find('i').text.strip() # maybe regex on the actual val??
            res[label] = value2
        except:
            continue
    return res

def nomadListScrape(query):
    query = query.replace(' ', '-').lower()
    # i could also add #sort=user_count_have_been to put most 'pupular places' first
    url = 'https://nomadlist.com/search/%s' % query
    try: 
        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        divs = soup.find_all('div', {'class': 'bottom-right'})
        val = divs[0].find('span', {'class': 'value'}).text.strip().replace(',', '')
        return int(val)
    except:
        return 0

def indeedScrape(location, job):
    city_info = googleMapsAPI.get_city_details(location)
    state_abbrev = googleMapsAPI.filter_results_for_state_abbrev(city_info)
    city_name = city_info[0]['long_name'].replace(' ', '-')
    job = job.title().replace(' ', '-')
    url = 'https://www.indeed.com/salaries/%s-Salaries,-%s-%s' % (job, city_name, state_abbrev)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    div = soup.find('div', {'class': 'cmp-sal-salary'})
    salary = div.find('span').text.replace('$', '').replace(',','')
    return int(salary)








