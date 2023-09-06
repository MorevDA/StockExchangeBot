import requests


def get_ind_info():
    headers = {
        'authority': 'api.bcs.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://bcs-express.ru',
        'referer': 'https://bcs-express.ru/',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'ticket': 'eyJpZCI6IjI1MTUxOTYyLWE5NDQtNDNhMy1hMjcxLWRjNjk0NzI3MjE5ZiIsIklzQ2xpZW50Ijp0cnVlLCJFbWFpbCI6Ik1vcmVmZkRBQHlhbmRleC5ydSIsIkRlc2NyaXB0aW9uIjpudWxsLCJBdmF0YXIiOiIiLCJBdmF0YXJUaHVtYiI6IiIsIlN0YXRlIjoicmVnaXN0ZXJlZCIsIkhhc1Byb2ZpbGUiOnRydWUsIkFncmVlIjoxLCJNYXJrZXRzIjpbImFsbHBsYWNlcyJdLCJIYXNDb25zdWx0aW5nQW5kQnJva2VyYWdlU2VydmljZXMiOmZhbHNlfQ',
        'token': 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJnVVJqazFLb1Vrd0FyZTZGLWpTbTlJUWlLbmtHUEk3Smk4dk1IVmlPUWlJIn0.eyJleHAiOjE2OTEwMDMwNjcsImlhdCI6MTY5MTAwMjc2NywianRpIjoiMTcxMDNiODEtMTVlNC00ZTM3LTg4YTItYTk0OWQ3MjNmNWM2IiwiaXNzIjoiaHR0cHM6Ly9hdXRoLWV4dC51c3ZjLmJjcy5ydS9hdXRoL3JlYWxtcy9Ccm9rZXIiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiZjplYjNhNjg0NC00ZDQ2LTQ0YzUtOGYxMi03NzhmMzA3OGQyMGM6YmZlZDRkY2QtN2Y3Zi00YjJjLWJmMjktOGM0M2ZlNzRhOTczIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYmNzZXhwcmVzcyIsInNlc3Npb25fc3RhdGUiOiI0MWQ4YmI1ZS05MmYzLTQwMTAtYTkxMy03MzdlNjc5NjllNGEiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9mZmxpbmVfYWNjZXNzIHByb2ZpbGUgZW1haWwiLCJzaWQiOiI0MWQ4YmI1ZS05MmYzLTQwMTAtYTkxMy03MzdlNjc5NjllNGEiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiY2xpZW50SWQiOiIyNTE1MTk2Mi1hOTQ0LTQzYTMtYTI3MS1kYzY5NDcyNzIxOWYiLCJwaG9uZSI6Ijc5MDQyMTE5NzcxIiwibmFtZSI6ItCU0LzQuNGC0YDQuNC5INCc0L7RgNC10LIiLCJrX2xvZ2luIjoiay0xNDU2MzY2IiwicHJlZmVycmVkX3VzZXJuYW1lIjoiay0xNDU2MzY2Iiwic291cmNlIjoi0JXQktCQIiwibWlkZGxlX25hbWUiOiLQkNC90LDRgtC-0LvRjNC10LLQuNGHIiwiZ2l2ZW5fbmFtZSI6ItCU0LzQuNGC0YDQuNC5IiwiaXNfdGVtcG9yYXJ5X3Bhc3N3b3JkIjoiZmFsc2UiLCJmYW1pbHlfbmFtZSI6ItCc0L7RgNC10LIiLCJlbWFpbCI6Ik1vcmVmZkRBQHlhbmRleC5ydSJ9.S51T5Sc8JS7yLMXrtkr-obcp39gDx8YWTqSILiZ6Xd-nXEyMmaH2w_bm3OtTGzBzu4__bQ_b2IEPHbh98L5Q9jQDNkL4uSFlwXh_JzK1B5NXYQHsJRMYAcdHsAGlpcWgMD-grmLWrrXI5oNnkQ8BzdST3SORrSnDd3SuwWWv1Rn4rqmheYu87etMOWhCBhlEJQ45YNsrKjbkFVZN3lrQQ8Ig0W2PcuXvvmwMrFqhdyTmUqAgvcRfokaIwLDNtVqsbRYi5wZ3XHt8U_M_6EKlAC4tZT9QDByWsw2YwjemLXPNvsyYFodl01H7XRsA2s-sZviJWJrPt3AzmKv6iMVPzw',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    params = {
        'instruments': [
            'INDX|IMOEX',
            'FEX|S&P500',
            'CETS|USD000UTSTOM',
            'CETS|CNYRUB_TOM',
            'CETS|EUR_RUB__TOM',
            'FEG|BRENT',
        ],
        'inOrderArray': 'true',
    }

    response = requests.get('https://api.bcs.ru/udfdatafeed/v1/info', params=params, headers=headers)
    return response.json()


def get_main_indexes(data: list) -> str:
    result_string = ''
    for i in data:
        result_string += f"<b>Наименование:</b> {i['shortName']}\n" \
                         f"<b>Текущее значение:</b> {i['info']['close']}\n" \
                         f"<b>Изменение:</b> {i['profit']} %\n\n"
    return result_string


if __name__ == '__main__':
    print(get_main_indexes(get_ind_info()).strip())


