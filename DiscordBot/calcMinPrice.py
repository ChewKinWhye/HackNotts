import time
from PIL import Image
import pytesseract
import requests
from io import BytesIO


def obtain_item_list(url):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    text = pytesseract.image_to_string(img)
    lines = text.splitlines()

    items = []
    for line in lines:
        if len(line) != 0:
            if line[-1].isdigit() and line.find('.') != -1:
                items.append(line)
    item_name = []
    item_price = []
    for item in items:
        name = ""
        data = item.split()
        for i in range (0, len(data)-1):
            name = name + data[i] + " "
        item_price.append(data[-1])
        item_name.append(name)
    return item_name, item_price


def calc_min_price(item_name, item_price):
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
    try:
        for row in output['results'][0]['content']['search_results']:
            if row['min_price'] is not None and float(row['min_price']) < float(item_price):
                prices.append(float(row['min_price']))
                urls.append(row['url'])
                counter = counter + 1
        sorted_results = sorted(zip(prices, urls))
    except KeyError:
        return -1
    print(sorted_results)
    output = ""
    for i in range(0, len(sorted_results)):
        output = output + str(sorted_results[i][0]) + " "
        output = output + str(sorted_results[i][1]) + " "
        if i == 2:
            break
    return output


def main(url):
    item_name_list, item_price_list = obtain_item_list(url)
    item_comparison_list = []
    print(item_name_list)
    for i in range(0, len(item_name_list)):
        options = calc_min_price(item_name_list[i], item_price_list[i])
        item_comparison_list.append(options)
    return item_name_list, item_price_list, item_comparison_list


# url = 'https://cdn.discordapp.com/attachments/645328389196087357/645562700356648970/photo6235259669102831847.jpg'
# item_name_list, item_price_list, item_comparison_list = main(url)
