import requests


def get_all_stocks_lot_size():
    """ Функция для получения данных о размере лота российских ценных бумаг торгующихся на ММВБ. Функция отправляет
    запрос к api ММВБ для получения данных по размеру лота всех акций торгущихся на ММВБ. Функция возвращает
    словарь с данными по размеру лота акций"""
    result = {}
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://www.moex.com',
        'Referer': 'https://www.moex.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    for start_value in range(0, 300, 100):
        params = {'_': '1687021339014', 'lang': 'ru', 'iss.meta': 'off', 'sort_order': 'asc',
                  'sort_column': 'SECID', 'start': f'{str(start_value)}', 'limit': '100',
                  'sec_type': 'stock_common_share,stock_preferred_share,stock_russian_depositary_receipt',
                  'faceunit': 'rub', 'bg': 'stock_tplus', }

        response = requests.get(
            'https://iss.moex.com/iss/apps/infogrid/stock/rates.json', params=params, headers=headers,)

        for i in response.json()['rates']['data']:
            result[i[0]] = {'name': i[1], 'ISIN': i[4], 'lotsize': int(i[29])}
    return result


def get_calendar_json():
    """Функция отправляет запрос к api компании БКС для получения данных о дивидендных выплатах.
     На выходе функции возвращается json объект для дальнейшего анализа"""
    url = 'https://api.bcs.ru/divcalendar/v1/dividends?actual=1'
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                   'Safari/537.36',
               'Accept': '*/*'}
    response = requests.get(url=url, headers=headers).json()
    return response


def get_list_this_year(func, func_1):
    """Функция возвращает словарь с информацией по названию компании и дивидендному периоду, размеру дивидендов на
    одну акцию, процент дивидендной доходности, дате закрытия реестра, дате последнего дня покупки акций для получения
     дивидендов, ориентировочной цене одного лота акций. Цена одного лота является ориентировочной, так как базируется на
     информации о цене акций на закрытии предыдущей торговой сессии."""
    stocks_with_div = {}
    total_list = func_1
    lots_size = func
    for stock in total_list.get('data'):
        dividend_percent = stock.get('yield')
        company_name = stock.get('company_name')
        dividend_value = stock.get('dividend_value')
        last_buy_day = str(stock.get('last_buy_day')).split('T')[0]
        closing_date = str(stock.get('closing_date')).split('T')[0]
        price_one_stock = stock.get('close_price')
        secure_code = stock.get('secure_code')
        lot_price = lots_size[secure_code]['lotsize'] * float(price_one_stock)
        stocks_with_div[company_name] = {'dividend_value': dividend_value, 'dividend_percent': dividend_percent,
                                             'last_buy_day': last_buy_day, 'closing_date': closing_date,
                                             'price_one_stock': price_one_stock, 'lot_price': lot_price}
    return sorted(stocks_with_div.items(), key=lambda x: x[1]['dividend_percent'], reverse=True)


def get_div_string():
    string_list = []
    z = get_list_this_year(get_all_stocks_lot_size(), get_calendar_json())
    for i in z:
        string = f'<b>Компания и отчетный период:</b> {i[0]}\n' \
                 f'<b>Размер дивиденда:</b> {i[1]["dividend_value"]}\n' \
                 f'<b>Дивидендная доходность:</b> {i[1]["dividend_percent"]} %\n' \
                 f'<b>Последний день для покупки акций:</b> {i[1]["last_buy_day"]}\n' \
                 f'<b>Дата закрытия реестра:</b> {i[1]["closing_date"]}\n' \
                 f'<b>Цена одного лота акций:</b> {i[1]["lot_price"]}\n\n'
        string_list.append(string)
    return string_list
