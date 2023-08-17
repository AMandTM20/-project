from DZ_finished.main import visit
from DZ_finished.main import langs
from DZ_finished.main import max_val

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

geo_logs_rus = [
    {'visit1': ['Москва', 'Россия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def test_visit():
    result = len(visit(geo_logs))
    assert result == len (geo_logs_rus)


#----------------------------------------
ids = {'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]}

ids_resul = {98, 35, 15, 213, 54, 119}

def test_langs():
    result = len(langs(ids))
    assert result == len(ids_resul)


#----------------------------------------
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

stats_resul = ('yandex')

def test_max_val():
    result = len(max_val(stats))
    assert result == len (stats_resul)

