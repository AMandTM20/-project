'''
Задание
Кто самый умный супергерой?
Есть API по информации о супергероях с информацией по всем супергероям.
Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
'''

import requests
import json
from pprint import pprint

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'

names = ['Hulk', 'Captain America', 'Thanos']
intelligence = {}

response = requests.get(url)

all_json = response.json() #  преобразуем response в тип json(класс list почему-то)

count1 = 0
count2 = 0

for item in all_json:
  count2+=1

  if item['name'] == "Hulk" or item['name'] =="Captain America" or item['name'] == "Thanos":
    intelligence[item['powerstats']['intelligence']] = item['name']
    names.append(item)
    count1+=1

print('intelligence :',intelligence )

print('names:')
pprint(names)
print('')
print("Получено записей о героях с заданными именами: ",count1)

print("Всего получено записей о героях: ",count2)

# cортировка словаря, содержащего сведения об интеллекте выбранных героев
sorted_intelligence = dict(sorted(intelligence.items()))
print('')
# Итог
print("Самый умный персонаж: ",sorted_intelligence.get(100),", его интеллект = ",list(sorted_intelligence)[-1] )

