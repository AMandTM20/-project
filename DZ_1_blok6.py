# This is a sample Python script.

# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# import json
# #print('Привет!')
#
# import requests
# print("-------------------------------------------------------")
# print("            ")
# print('Упражнения по теме "Работа с библиотекой requests, http запросы"')
#
# print("--------------------------задание из теста по теме Работа с библиотекой requests, http запросы--------------------------")
# print(' ')
#
# url = "htpps://htppbin.org/get"
# resp = requests.get(url)
# print(resp)
# # print("================================яндекс===================================")
# # def test1_request():
# #     url = "https://httpbin.org/get"
# #     pt = {"model": "nike123"}
# #     headers = {"Authorization": "secret - token - 123"}
# #     params = {"model": "nike123"}  # словарь параметров
# #     response = requests.get(url=url, params=pt, headers=headers,
# #                             timeout=5)  # все параметры лучше писать в именованном виде, timeout говорит о том, через какое время прервать запрос, если он долго выполняется
# #     if response.status_code > 400:
# #         print(f"request error: {response.status_code} ")
# #     # pprint(response)
# #     # pprint(response.content)# Вывод в непонятном виде(потоком?)
# #     # pprint(response.text) # если знаем, что прислали текст
# #     pprint(response.json())  # если знаем,что прислали словарьб, если там не словарь, то будет ошибка
# # if __name__ == '__main__':
# #   ya = YandexDisk(token = TOKEN)
# #  pprint(ya.get_files_list())
#pip install psycopg2-binary
#ДЗ_5
#pip install psycopg2-binary
#pip install psycopg2-binary
#import psycopg2

# #1 Функция, создающая структуру БД (таблицы).
# def create_db(conn):
#         #with conn.cursor() as cur:
#             cur.execute("""
#                 DROP TABLE IF EXISTS phone;
#                 DROP TABLE IF EXISTS client;
#
# 			  	CREATE TABLE IF NOT EXISTS client(
# 				client_id SERIAL PRIMARY KEY,
# 			 	firstname VARCHAR(20) NOT NULL,
# 			 	lastname VARCHAR(40) NOT NULL,
# 			 	email VARCHAR(40) NOT NULL UNIQUE);
#
# 			  	CREATE TABLE IF NOT EXISTS phone(
# 				phone_id SERIAL PRIMARY KEY,
# 				client_id INTEGER,
# 				phones INTEGER UNIQUE,
# 				CONSTRAINT fk
#                	FOREIGN KEY(client_id)
#                	    REFERENCES client(client_id)
#                	        ON DELETE CASCADE);
#             """)
#
# #2.Функция, позволяющая добавить нового клиента.
# def add_client(conn,cur, firstname, lastname, email, phone=None):
#     #with conn.cursor() as cur:
#         cur.execute("""
#             INSERT INTO client(firstname, lastname, email)
# 			VALUES(%s,%s,%s)
# 			RETURNING client_id, firstname, lastname, email;
# 	 		""", (firstname, lastname, email))
#         print(cur.fetchone())
#
# # #3. Функция, позволяющая добавить телефон для существующего клиента.
# # def add_phone(conn, client_id, phones ):
# #     with conn.cursor() as cur:
# #         cur.execute("""
# #             INSERT INTO phone(client_id, phones)
# # 			VALUES(%s,%s)
# # 			RETURNING phone_id, client_id, phones ;
# # 			""", (client_id, phones ))
# #         print(cur.fetchall())
# #
# # #4.Функция, позволяющая изменить данные о клиенте.
# # def change_client(conn, client_id, firstname = None, lastname = None, email=None, phone=None):
# #     with conn.cursor() as cur:
# #         cur.execute("""
# #             UPDATE client SET lastname= %s WHERE client_id = %s;
# #  			""", (lastname,client_id,))
# #
# # #5. Функция, позволяющая удалить телефон для существующего клиента.
# # def delete_phone(conn, client_id, phones):
# #     with conn.cursor() as cur:
# #         cur.execute("""
# #             DELETE FROM phone WHERE client_id = %s and phones = %s;
# #                 """, (client_id,phones))
# #         cur.execute("""
# #             SELECT * FROM phone;
# #             """)
# #         print(cur.fetchall())  # запрос данных автоматически зафиксирует изменения
# #
# # #6. Функция, позволяющая удалить существующего клиента.
# # def delete_client(conn, client_id):
# #     with conn.cursor() as cur:
# #         cur.execute("""
# #             DELETE FROM client WHERE client_id = %s;
# #                 """, (client_id,))
# #         cur.execute("""
# #             SELECT * FROM client;
# #             """)
# #         print(cur.fetchall())
# #
# # #7. Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
# # def find_client(conn, firstname=None, lastname=None, email=None, phones=None):
# #     with conn.cursor() as cur:
# #         cur.execute("""
# #             SELECT c.client_id FROM client c
# #             JOIN phone p ON c.client_id = p.client_id
# #             WHERE  c.firstname = %s
# #             """,(firstname,))
# #         print(cur.fetchall())
# #         cur.execute("""
# #             SELECT c.client_id FROM client c
# #             JOIN phone p ON c.client_id = p.client_id
# #             WHERE  c.lastname = %s
# #             """, (lastname,))
# #         print(cur.fetchall())
# #         cur.execute("""
# #             SELECT c.client_id FROM client c
# #             JOIN phone p ON c.client_id = p.client_id
# #             WHERE  c.email = %s
# #             """, (email,))
# #         print(cur.fetchall())
# #         cur.execute("""
# #             SELECT c.client_id FROM client c
# #             JOIN phone p ON c.client_id = p.client_id
# #             WHERE  p.phones = %s
# #             """, (phones,))
# #         print(cur.fetchall())
#
# with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
#     with conn.cursor() as cur:
#         create_db(conn)
#         add_client(conn,cur, 'Иван','Петров','ipiy@mailr.ru', phone=None)
#         add_client(conn,cur, 'Петр','Иванов', 'pi@mailr.ru', phone=None)
#         add_client(conn,cur,'Сидор', 'Сидоров', 'ss@mailr.ru', phone=None)
#         add_client(conn,cur, 'Иван', 'Сидоров', 'is@mailr.ru', phone=None)
#         add_client(conn,cur, 'Петр', 'Сидоров', 'ps@mailr.ru', phone=None)
#         add_client(conn,cur, 'Алексей', 'Новиков', 'an@mailr.ru', phone = None)
#     # add_phone(conn, 1, 8553552)
#     # add_phone(conn,1,8653518)
#     # add_phone(conn,2,8353757)
#     # add_phone(conn,4,8124352)
#     # add_phone(conn,4,8550059)
#     # add_phone(conn,4,8553752)
#     # add_phone(conn,5,8573585)
#     # add_phone(conn,6,8599585)
#     # change_client(conn, 3, '', 'Овечкин', '')  # работает только в таком виде
#     # delete_phone(conn,4,8550059)
#     # delete_client(conn, 3)
#     # f_find = find_client(conn, 'Петр', 'Обещалкин', 'an@mailr.ru', 8553752)
#     # print('f_find', f_find)
# conn.close()
#
#ДЗ_5
# import psycopg2
#
# #1 Функция, создающая структуру БД (таблицы).
# def create_db(conn):
#         with conn.cursor() as cur:
#             cur.execute("""
#                 DROP TABLE IF EXISTS phone;
#                 DROP TABLE IF EXISTS client;
#
# 			  	CREATE TABLE IF NOT EXISTS client(
# 				client_id SERIAL PRIMARY KEY,
# 			 	firstname VARCHAR(20) NOT NULL,
# 			 	lastname VARCHAR(40) NOT NULL,
# 			 	email VARCHAR(40) NOT NULL UNIQUE);
#
# 			  	CREATE TABLE IF NOT EXISTS phone(
# 				phone_id SERIAL PRIMARY KEY,
# 				client_id INTEGER,
# 				phones INTEGER UNIQUE,
# 				CONSTRAINT fk
#                	FOREIGN KEY(client_id)
#                	    REFERENCES client(client_id)
#                	        ON DELETE CASCADE);
#             """)
#
# #2.Функция, позволяющая добавить нового клиента.
# def add_client(conn, firstname, lastname, email, phone=None):
#     with conn.cursor() as cur:
#         cur.execute("""
#             INSERT INTO client(firstname, lastname, email)
# 			VALUES(%s,%s,%s)
# 			RETURNING client_id, firstname, lastname, email;
# 	 		""", (firstname, lastname, email))
#         print(cur.fetchone())
#
# #3. Функция, позволяющая добавить телефон для существующего клиента.
# def add_phone(conn, client_id, phones ):
#     with conn.cursor() as cur:
#         cur.execute("""
#             INSERT INTO phone(client_id, phones)
# 			VALUES(%s,%s)
# 			RETURNING phone_id, client_id, phones ;
# 			""", (client_id, phones ))
#         print(cur.fetchall())
#
# #4.Функция, позволяющая изменить данные о клиенте.
# def change_client(conn, client_id, firstname = None, lastname = None, email=None, phone=None):
#     with conn.cursor() as cur:
#         cur.execute("""
#             UPDATE client SET lastname= %s WHERE client_id = %s;
#  			""", (lastname,client_id,))
#
# #5. Функция, позволяющая удалить телефон для существующего клиента.
# def delete_phone(conn, client_id, phones):
#     with conn.cursor() as cur:
#         cur.execute("""
#             DELETE FROM phone WHERE client_id = %s and phones = %s;
#                 """, (client_id,phones))
#         cur.execute("""
#             SELECT * FROM phone;
#             """)
#         print(cur.fetchall())  # запрос данных автоматически зафиксирует изменения
#
# #6. Функция, позволяющая удалить существующего клиента.
# def delete_client(conn, client_id):
#     with conn.cursor() as cur:
#         cur.execute("""
#             DELETE FROM client WHERE client_id = %s;
#                 """, (client_id,))
#         cur.execute("""
#             SELECT * FROM client;
#             """)
#         print(cur.fetchall())
#
# #7. Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
# def find_client(conn, firstname=None, lastname=None, email=None, phones=None):
#     with conn.cursor() as cur:
#         cur.execute("""
#             SELECT c.client_id FROM client c
#             JOIN phone p ON c.client_id = p.client_id
#             WHERE  c.firstname = %s
#             """,(firstname,))
#         print(cur.fetchall())
#         cur.execute("""
#             SELECT c.client_id FROM client c
#             JOIN phone p ON c.client_id = p.client_id
#             WHERE  c.lastname = %s
#             """, (lastname,))
#         print(cur.fetchall())
#         cur.execute("""
#             SELECT c.client_id FROM client c
#             JOIN phone p ON c.client_id = p.client_id
#             WHERE  c.email = %s
#             """, (email,))
#         print(cur.fetchall())
#         cur.execute("""
#             SELECT c.client_id FROM client c
#             JOIN phone p ON c.client_id = p.client_id
#             WHERE  p.phones = %s
#             """, (phones,))
#         print(cur.fetchall())
#
# with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
#     create_db(conn)
#     add_client(conn, 'Иван','Петров','ipiy@mailr.ru', phone=None)
#     add_client(conn, 'Петр','Иванов', 'pi@mailr.ru', phone=None)
#     add_client(conn, 'Сидор', 'Сидоров', 'ss@mailr.ru', phone=None)
#     add_client(conn, 'Иван', 'Сидоров', 'is@mailr.ru', phone=None)
#     add_client(conn, 'Петр', 'Сидоров', 'ps@mailr.ru', phone=None)
#     add_client(conn, 'Алексей', 'Новиков', 'an@mailr.ru', phone = None)
#     add_phone(conn, 1, 8553552)
#     add_phone(conn,1,8653518)
#     add_phone(conn,2,8353757)
#     add_phone(conn,4,8124352)
#     add_phone(conn,4,8550059)
#     add_phone(conn,4,8553752)
#     add_phone(conn,5,8573585)
#     add_phone(conn,6,8599585)
#     change_client(conn, 3, '', 'Овечкин', '')  # работает только в таком виде
#     delete_phone(conn,4,8550059)
#     delete_client(conn, 3)
#     f_find = find_client(conn, 'Петр', 'Обещалкин', 'an@mailr.ru', 8553752)
#     print('f_find', f_find)
# conn.close()
# Тема: Модули, пакеты, импорты в Python

# ДЗ_1
# 1. Разработать структуру программы «Бухгалтерия»
# 2.Импортировать функции в модуль main.py и вызывать эти функции в конструкции  __name__ == '__main__'
from application import salary
from application.db import people
from datetime import datetime

if __name__ == '__main__':
    print(" ")
    arg_d = datetime.now()
    date = datetime.date(arg_d)
    time = datetime.time(arg_d)
    print("Текущая дата: ", date,"              ", "Текущее время: ", time )
    print(" ")
    #print("Текущее время: ", time)
    salary.calculate_salary()
    people.get_employees()

# Программный код people.py:
#def get_employees():
#    print("Из get_employees: Число сотрудников опять увеличилось ")

# #Программный код salary.py:
#def calculate_salary():
#    print("Из calculate_salary: Завтра вам повысят зарплату в два раза!")

# 3.Познакомиться с модулем datetime. При вызове функций модуля main.py выводить текущую дату.
# Сделано в модуле main.py программы бухгалтерия

# 4.Найти интересный для себя пакет на pypi и в файле requirements.txt указать его с актуальной версией.o При желании можно написать программу с этим пакетом.
