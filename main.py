import requests
import json
from scrapper import scrapper_metod

headers = {'User-Agent': 'api-test-agent'}
params = {'area': (1, 2), 'per_page': 50, 'only_with_salary': 'True', 'currency': 'USD'}
URL = 'https://api.hh.ru/vacancies?text=python+django+flask'


def api_method():
    res = {}
    hh_data = requests.get(URL, headers=headers, params=params)
    data = hh_data.json()
    for item in data['items']:
        res[item['name']] = {
            'salary': {'from': item['salary']['from'], 'to': item['salary']['to']},
            'employer': item['employer']['name'],
            'city': item['area']['name'],
            'URL': item['alternate_url']
            }
    return res


if __name__ == '__main__':
    # выполняем через API
    with open('data_api.json', 'w', encoding='utf-8') as f:
        json.dump(api_method(), f, ensure_ascii=False, indent=2)
    # выполняем через скрапер
    with open('data_scrapper.json', 'w', encoding='utf-8') as f:
        json.dump(scrapper_metod(), f, ensure_ascii=False, indent=2)
