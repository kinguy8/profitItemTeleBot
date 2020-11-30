import requests
import re
import urllib.request as req
import steammarket as sm

from bot.settings import URL, USD


def generate_title_URI(text):
    """UTIL FUNCTION FOR RETURN URI TEXT"""
    uri = req.pathname2url(text)
    return uri


def request_to_url(request_url):
    """UTIL FUNCTION FOR REQUEST TO API OF WEB-SITE AND GETTING PRICE OF ITEM"""
    r = requests.get(request_url)
    if r.status_code == 200:
        res = r.json()
        try:
            return res['objects'][0]['price']['USD'] if res['objects'][0]['price']['USD'] != "" else \
            res['objects'][0]['suggestedPrice']['USD']
        except:
            print(u'Unexpected error')
    else:
        print("error")


def return_price(item):
    """FUNCTION FOR RETURN PRICE OF ITEM"""
    uri_text = generate_title_URI(item)
    request_url = URL.format(uri_text)
    result = request_to_url(request_url)
    print("result",result)
    if (result is not None):
        price_usd = split_dollar(result)
        rus_price = translate_to_rus_rub(price_usd)
        return rus_price
    else:
        return result


def get_steam_price(item):
    """FUNCTION FOR GETTING PRICE OF ITEM IN STEAM PLANFORM"""
    steam_price = sm.get_item(570, item, currency='USD')['lowest_price'][1:]
    rus_price = translate_to_rus_rub(steam_price)
    return rus_price


def split_dollar(price):
    """FUNCTION FOR SPLIT PRICE FROM JSON DATA"""
    if re.match(r'^(\d{3})$', price) is not None:
        first = price[:1]
        second = price[1:]
        list = [first, second]
        result = '.'.join(list)
        return result
    elif re.match(r'^(\d{2})$', price) is not None:
        first = 0
        second = price[1:]
        list = [first, second]
        result = '.'.join(list)
        return result
    elif re.match(r'^(\d{4})$', price) is not None:
        first = price[:2]
        second = price[2:]
        list = [first, second]
        result = '.'.join(list)
        return result
    elif re.match(r'^(\d{5})$', price) is not None:
        first = price[:3]
        second = price[3:]
        list = [first, second]
        result = '.'.join(list)
        return result
    else:
        print("error")


def translate_to_rus_rub(price):
    """CONVERN TO RUSSIAN RUB FROM USD"""
    full_price = float(price) * float(USD)
    result = str(full_price).split('.')
    return result[0]


def save_data_to_file(message):
    """UTIL FUNCTION FOR WRITING SOME DATA ABOUT USERS"""
    d2 = {message.chat.id:message.text}
    with open('text.txt', 'a') as out:
        for key, val in d2.items():
            out.write('{}:{}\n'.format(key, val))


def read_data_file():
    d2 = {}
    with open('bot/files/file.txt') as inp:
        for i in inp.readlines():
            key, val = i.strip().split(':')
            d2[key] = val
    return d2
