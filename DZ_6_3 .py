'''

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Попробуем получать интересующие вакансии на сайте headhunter самыми первыми :)

Необходимо парсить страницу со свежими вакансиями с поиском по "Python" и городами "Москва" и "Санкт-Петербург". Эти параметры задаются по ссылке
Нужно выбрать те вакансии, у которых в описании есть ключевые слова "Django" и "Flask".
Записать в json информацию о каждой вакансии - ссылка, вилка зп, название компании, город.

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

'''
import requests # для выполнения запросов
from fake_headers import Headers # Для формирования заголовка в нашем запросе
import bs4 # для вытаскивания полезных данных из HTML
import lxml # Для обработки данных из HTML
import json
from pprint import pprint
# Генерируем случайные заголовки
headers = Headers(browser = 'firefox', os = 'win')
headers_data = headers.generate()

# Адрес страницы для начала парсинга
url = 'https://hh.ru/search/vacancy?text=python&django&flask&area=1&area=2'

# запрашиваем HTML код первой страницы, используя headers
response = requests.get(url,headers = headers_data)
soup = bs4.BeautifulSoup(response.text,'lxml')
#pprint(soup.text)

# получаем  тег с классом serp-item
vacancy = soup.find('div',class_ = 'serp-item')
vacancies = soup.find_all('a',class_ = 'serp-item__title')


