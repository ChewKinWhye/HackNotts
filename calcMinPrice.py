import requests
import time
from ExtractFileInfo2 import get_info

def calc_min_price(item_name):
    APIKey = "IDXACACQMBQNFRSYZJXACXJRMFWLXCIWCEPALTTNFDWUGHNLXETWSXNAAOOUAZER"
    data = {
        'token': APIKey,
        'source': 'amazon',
        'country': 'gb',
        'topic': 'search_results',
        'key': 'asin',
        'values': item_name,
        'max_pages': '1',
    }
    response = requests.post('https://api.priceapi.com/v2/jobs', data=data)
    response_json = response.json()
    job_ID = response_json['job_id']

    params = (
        ('token', APIKey),
    )
    while True:
        response = requests.get('https://api.priceapi.com/v2/jobs/' + job_ID, params=params)
        response_json = response.json()
        print(response_json['completed'])
        time.sleep(1)
        if response_json['completed'] == 1:
            break
    params = (
        ('token', APIKey),
    )
    response = requests.get('https://api.priceapi.com/v2/jobs/' + job_ID + '/download', params=params)
    output = response.json()
    counter = 0
    prices = []
    urls = []
    for row in output['results'][0]['content']['search_results']:
        if row['min_price'] is not None:
            prices.append(float(row['min_price']))
            urls.append(row['url'])
            counter = counter + 1
    sorted_results = sorted(zip(prices, urls))
    return sorted_results[0], sorted_results[1], sorted_results[2]


#output = (calc_min_price('Rice'))



