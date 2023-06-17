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
url = 'https://hh.ru/search/vacancy?text=python&django&flask&area=1&area=2/'

# запрашиваем HTML код первой страницы, используя headers
response = requests.get(url,headers = headers_data)
soup = bs4.BeautifulSoup(response.text,'lxml')
pprint(soup.text)
# получаем все теги с классом serp-item__title
vacancies = soup.find_all(class_ = 'serp-item__title')

vacancy_list = []
# Просматриваем все вакансии в цикле и запоминаем теги: заголовков, описания вакансий, названия компаний
for vacancy in vacancies:
    h2_tag = vacancy.find('h2') # тег с заголовком

    # Извлечение ссылки на вакансию
    a_tag = h2_tag.find('a') #!!! ЗДЕСЬ ПОКА НЕПОНЯТНАЯ ОШИБКА!!!
    link = f'https://hh.ru{a_tag["href"]}'

    # Извлечение заголовка вакансии
    full_vacancy_html = requests.get(link, headers=headers.generate()).text
    full_vacancy_soup = bs4.BeautifulSoup(full_vacancy_html, features='lxml')

    salary = vacancy.find('span', class_='bloko-header-section-3').text

    company = vacancy.find('a', class_='bloko-link bloko-link_kind-tertiary').text

    city = vacancy.find('div',{'data-qa':'vacancy-serp__vacancy-address'}).text


    vacancy_list.append({

    'Зарплата': salary,
    'Компания': company,
    'Город': city,
    'Ссылка': link

    })
pprint(vacancy_list)