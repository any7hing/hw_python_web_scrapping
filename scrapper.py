import requests
import json
from bs4 import BeautifulSoup
from fake_headers import Headers
headers = Headers(browser='chrome', os='win')
url = 'https://spb.hh.ru/search/vacancy?text=Python+django+flask&salary=&area=1&area=2&ored_clusters=true&only_with_salary=true'
result_dict = {}
def scrapper_metod():
    data = requests.get(url,headers=headers.generate()).text
    soup = BeautifulSoup(data,'lxml')
    all_tag = soup.find('main',class_='vacancy-serp-content')
    tag = all_tag.find_all('div',class_='vacancy-serp-item-body__main-info')
    for i in tag:
        result_dict[i.find('a',class_='serp-item__title').text] = {
            'salary':i.find('span',class_='bloko-header-section-3').text,
            'employer':i.find('div',class_='bloko-text').text,
            'city':i.find('div',attrs={'data-qa':'vacancy-serp__vacancy-address'}).text.split(',')[0],
            'URL':i.find('a',class_='serp-item__title')['href']
        }
    return result_dict

if __name__ =='__main__':
    scrapper_metod()
    with open('data_scrapper.json', 'w',encoding='utf-8') as f:
        json.dump(result_dict,f,ensure_ascii=False,indent=2)