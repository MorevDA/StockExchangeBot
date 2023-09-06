import requests


def get_all_info_on_stocks() -> list:
    """Функция отправляет get запрос к API ММВБ и получает json содержащий актуальную цену по всем акциям
    торгующимся на ММВБ. После завершения торговой сессии информация актуальна на момент закрытия торгов.
    Функция возвращает список словарей с информацией по акциям(json-объект)."""
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://www.moex.com',
        'Referer': 'https://www.moex.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/114.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'iss.meta': 'off',
        'iss.json': 'extended',
        'lang': 'ru',
        'security_collection': '3',
        'sort_column': 'VALTODAY',
        'sort_order': 'desc',
    }

    response = requests.get(
        'https://iss.moex.com/iss/engines/stock/markets/shares/boardgroups/57/securities.json',
        params=params,
        headers=headers)
    return response.json()[1]['securities']


def get_list_stocks(all_stocks: list, buy_limit: int) -> list:
    """Функция для получения списка акций которые возможно приобрести на определенную сумму(сумма указывается при
    вызове функции).
    Функция принимает на вход список с информацией по всем акциям и сумму на которую необходимо приобрести акции.
    Функция возвращает список строк, в каждой строке содержится информация: наименование акции, цена одной акции,
    размер лота, цена одного лота, количество лотов которые можно приобрести на введенную сумму."""
    result = []
    for stock in all_stocks:
        price = float(stock.get('PREVPRICE'))
        size_lot = int(stock.get('LOTSIZE'))
        lot_price = size_lot * price
        lot_amount = int(buy_limit // lot_price)
        if lot_price <= buy_limit:
            name = stock.get('SHORTNAME')
            result.append({
                    '<b>Компания:</b>': name,
                    '<b>Цена одной акции, руб.:</b>': price,
                    '<b>Размер лота, шт.:</b>': size_lot,
                    '<b>Цена лота, руб:</b>': round(lot_price, 1),
                    '<b>Количество лотов, шт.:</b>': lot_amount
                })
    result.sort(key=lambda x: x['<b>Цена лота, руб:</b>'])
    return result if len(result) > 0 else ['К сожалению, на указанную сумму невозможно приобрести'
                                           'акции']


if __name__ == '__main__':
    print(get_list_stocks(get_all_info_on_stocks(), 10))
