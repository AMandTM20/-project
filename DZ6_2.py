import os
from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", 'r', encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    #pprint(contacts_list)


pattern = r"(\+7|7|8)[\s|-]*\(?(\d{1,3})\)?[\s|-]*(\d{1,3})[\s|-]*(\d{2})[\s|-]*(\d{2})[\s|\(]*(\w+\.\s\d+)?\)?"
contacts_list1 = contacts_list.copy()
headings = contacts_list1.pop(0)
new_contacts_list = []
new_contacts_list.append(headings)
for_sort_new_contacts_list = []
for el in contacts_list1:
    contact = []
    if len(el[0].split(' ')) == 3:
        contact.extend(re.findall(r'^[А-ё]+', el[0]))
        name = re.findall(r'\s[А-ё]+\s', el[0])
        name1 = str(name[0]).replace(' ', '')
        contact.append(name1)
        contact.extend(re.findall(r'[А-ё]+$', el[0]))
    elif len(el[0].split(' ')) == 2:
        contact.extend(re.findall(r'^[А-ё]+', el[0]))
        contact.extend(re.findall(r'[А-ё]+$', el[0]))
        contact.append('')
    elif len(el[0].split(' ')) == 1 and len(el[1].split(' ')) == 2:
        contact.append(el[0])
        contact.extend(re.findall(r'^[А-ё]+', el[1]))
        contact.extend(re.findall(r'[А-ё]+$', el[1]))
    else:
        contact.append(el[0])
        contact.append(el[1])
        contact.append(el[2])
    contact.append(el[3])
    contact.append(el[4])
    tell = re.sub(pattern, r"+7(\2)\3-\4-\5 \6", el[5])
    contact.append(tell)
    contact.append(el[6])
    for_sort_new_contacts_list.append(contact)

contact_dic = {}
for elem in for_sort_new_contacts_list:
    if f'{elem[0]} {elem[1]}' in contact_dic.keys():
        if len((contact_dic[f'{elem[0]} {elem[1]}'])[2]) == 0:
            (contact_dic[f'{elem[0]} {elem[1]}'])[2] = elem[2]

        if len((contact_dic[f'{elem[0]} {elem[1]}'])[3]) == 0:
            (contact_dic[f'{elem[0]} {elem[1]}'])[3] = elem[3]

        if len((contact_dic[f'{elem[0]} {elem[1]}'])[4]) == 0:
            (contact_dic[f'{elem[0]} {elem[1]}'])[4] = elem[4]

        if len((contact_dic[f'{elem[0]} {elem[1]}'])[5]) == 0:
            (contact_dic[f'{elem[0]} {elem[1]}'])[5] = elem[5]

        if len((contact_dic[f'{elem[0]} {elem[1]}'])[6]) == 0:
            (contact_dic[f'{elem[0]} {elem[1]}'])[6] = elem[6]

    else:
        contact_dic[f'{elem[0]} {elem[1]}'] = elem

for val in contact_dic.items():
    new_contacts_list.append(val[1])

print("Новый контакт_лист")
pprint(new_contacts_list)

with open("phonebook.csv", "w",encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
