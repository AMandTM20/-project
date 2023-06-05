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
    salary.calculate_salary()
    people.get_employees()

# Программный код people.py:
#def get_employees():
#    print("Из get_employees: Число сотрудников опять увеличилось ")

#Программный код salary.py:
# def calculate_salary():
#    print("Из calculate_salary: Завтра вам повысят зарплату в два раза!")

# 3.Познакомиться с модулем datetime. При вызове функций модуля main.py выводить текущую дату.
# Сделано в модуле main.py программы бухгалтерия

# 4.Найти интересный для себя пакет на pypi и в файле requirements.txt указать его с актуальной версией.
# При желании можно написать программу с этим пакетом.