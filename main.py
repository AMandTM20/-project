import requests
import yadisk
import operator

def visit(geo_logs):
    new_list = []
    for geo_rus in geo_logs:
        for geo_r, g in geo_rus.items():
            if 'Россия' in g:
                new_list.append(geo_rus)

    return new_list

def langs(ids):
    langs = []
    for lang in ids.values():
        if type(lang) == list:
            langs += lang
        else:
            langs.append(lang)
    return (set(langs))

def max_val(stats):
    max_val = max(stats.items(), key=lambda x: x[1])
    max_val = max(stats.items(), key=operator.itemgetter(1))
    return (max_val[0])






