import requests # для выполнения запросов
from fake_headers import Headers # Для формирования заголовка в нашем запросе. В этом заголовке будет информация, которая меняется при кождом заходе
import bs4 # для вытаскивания полезных данных из HTML
import lxml # ДЛя обработки данных из HTML, здесь парсер для управления модулями, которые находятся в bs4. Делает данные более читабельными/ Не работает?

# Чтобы не забанили, генерируем разные заголовки
headers = Headers(browser = 'firefox', os = 'win')
headers_data = headers.generate()

# запрашиваем HTML код первой страницы, используя headers.
main_page_html = requests.get('https://habr.com/ru/all/',headers = headers_data).text
main_page_soup = bs4.BeautifulSoup(main_page_html,'lxml')

# находим тег div(первое вхождение) , содержащий информацию о классе tm-articles-list'(?)
div_article_list_tag = main_page_soup.find('div', class_ = 'tm-articles-list')
article_tags = div_article_list_tag.find_all('article')#получаем все теги с "article"  - заголовками статей

# Список словарей для хранения данных
parsed_articles = []
# Просматриваем все статьи в цикле и запоминаем теги: заголовков, времени и ссылок на текст статьи
for article_tag in article_tags:
    h2_tag = article_tag.find('h2')#тег с заголовком
    title = h2_tag.text

    time_tag = article_tag.find('time')# тег с датой
    time_str = time_tag['datetime']

    a_tag = h2_tag.find('a')# тег со ссылкой на текст статьи

    # Извлечение ссылки на статью
    link = f'https://habr.com{a_tag["href"]}'

    # Извлечение заголовка статьи
    full_article_html = requests.get(link,headers = headers.generate()).text
    full_article_soup = bs4.BeautifulSoup(full_article_html,features = 'lxml')

    # Извлечение текста статьи
    ful_article_tag = full_article_soup.find('div', id = 'post-content-body')# доступ к атрибутам тегов
    ful_article_text = ful_article_tag.text

    # Формирование словаря
    parsed_article ={
        'title': title,
        'time': time_str,
        'link': link,
        #'text': ful_article_text
    }
    # Добавление словаря в список словарей
    parsed_articles.append(parsed_article)
    print(parsed_article, sep='\n')  # печать словарей
#print(parsed_articles)
