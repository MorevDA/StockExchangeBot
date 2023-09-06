import requests


def get_all_currency_rate():
    headers = {
        'authority': 'api.bcs.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://bcs-express.ru',
        'partner-token': 'A5264D52-1510-4E42-8E90-E729FF405646',
        'referer': 'https://bcs-express.ru/',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'ticket': '',
        'token': '',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    params = {
        'portfolio_ids[0]': '-14',
        'sorting': '1',
        'sorting_order': 'asc',
        'limit': '70',
    }

    response = requests.get('https://api.bcs.ru/partner/quotations', params=params, headers=headers)
    return response.json().get('data')


def get_all_currency(currency_list: list) -> list:
    all_currency: list = []
    for curr in currency_list:
        curr_str: str = ''
        if curr['last_price'] > 0:
            curr_str += f"<b>Валюта:</b> {curr['issuer']}\n<b>Последняя цена:</b> {curr['last_price']}\n" \
                   f"<b>Изменение за день,%:</b> {curr['price_change_percent']}\n\n"
            all_currency.append(curr_str)
    return all_currency



if __name__ == '__main__':
    result =[]
    x = get_all_currency_rate()
    for i in x:
        result.append(i.get('issuer'))
    print(result)
