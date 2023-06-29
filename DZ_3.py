'''

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
Задание
Попробуем получать интересующие вакансии на сайте headhunter самыми первыми :)

Необходимо парсить страницу со свежими вакансиями с поиском по "Python" и городами "Москва" и "Санкт-Петербург".
Эти параметры задаются по ссылке.
Нужно выбрать те вакансии, у которых в описании есть ключевые слова "Django" и "Flask".
Записать в json информацию о каждой вакансии - ссылка, вилка зп, название компании, город.

Решение
Свежие акансии выбирались на первой странице запроса(наверное, они опубликованы позже других вакансий(?))
Города Москва и Санкт-Петербург указаны в url запроса  как area = 1 и area = 2

Находим список вакансий на этой странице с помощью soup.find(class_='vacancy-serp-content')
Класс  'vacancy-serp-content' определяется в HTML коде страницы путем выделения всей страницы и поиска тега
со словом 'vacancy'.

Находим HTML код каждой вакансии, выделяя на этой странице сайта информацию об одной вакансии, например, первой
Обнаруживаем, что информация о зарплате, названии компании, города, в котором находится компания и ссылка на описание
вакансии находится внутри тега <div class = 'vacancy-serp-item__layout'>

В цикле for обрабатываем все вакансии на этой странице - заполняем соответствующие переменные значениями взятыми из
соответствующих тегов HTML кода.

Для проверки того, есть ли в описании вакансии ключевые слова "Django" и "Flask" делаем запрос по ссылке на описание вакансии,
находим нужный тег и в тексте этого тега ищем "Django" и "Flask".

Если  "Django" и "Flask" нашлись,формируем словарь для этой вакансии. В словаре будут все нужные данные.
Добавляем словарь к списку вакансий.
После просмотра всех вакансий на странице сайта и формирования списка записываем полученные данные из списка  в json файл

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

'''
import requests # для выполнения запросов
from fake_headers import Headers # Для формирования заголовка в нашем запросе
import bs4  # для вытаскивания полезных данных из HTML
import lxml # Для обработки данных из HTML
import json
from pprint import pprint
import re

headers = Headers(browser = 'firefox', os = 'win')
headers_data = headers.generate()

url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

response = requests.get(url,headers = headers_data)
soup = bs4.BeautifulSoup(response.text,'lxml')

vacancy_list = soup.find(class_='vacancy-serp-content')

vacancy_card = soup.find_all('div', class_='vacancy-serp-item__layout')

json_list = []

for vacancy in vacancy_card:
    link_tag = vacancy.find('a', class_='serp-item__title')
    link = link_tag['href']
    wages_tag = vacancy.find('span', class_='bloko-header-section-3')
    if wages_tag != None:
        wages = (wages_tag).text
        wages = wages.replace('\u202f', '')
    else:
        wages = "Заработная плата не указана"
    print(" ")
    pprint(wages)
    company_name_tag = vacancy.find('a', class_='bloko-link bloko-link_kind-tertiary')
    company_name = company_name_tag.text
    company_name = company_name.replace('\xa0', '')
    pprint(company_name)

    city_tag = vacancy.find('div', class_="vacancy-serp-item__info")
    city_tag1 = city_tag.find_all('div', class_="bloko-text")# поиск тега с названием города
    city = re.findall(r'(^\w+-?\w+)(,?.+)?', (city_tag1[1].text))[0][0]# обращение ко 2 элементу списка
    pprint(city)

    vacancy_html = requests.get(link, headers=headers_data).text
    vacancy_soup = bs4.BeautifulSoup(vacancy_html, features='lxml')

    vacancy_desc_tag = vacancy_soup.find('div', class_='bloko-columns-row')
    vacancy_desc = vacancy_desc_tag.text
    
    if 'Flask' in vacancy_desc and 'Django' in vacancy_desc:
        vacancy_dic = {'link': link, 'wages': wages, 'company_name': company_name, 'city': city}
        json_list.append(vacancy_dic)

with open("vacancy.json", "w", encoding="utf-8") as file:
    json.dump(json_list, file, indent=4,ensure_ascii = False)
pprint(json_list)
