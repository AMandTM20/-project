#=================================================================================================================================================ээ
# Задача №2
# У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон.
# Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.
#
# Все ответы приходят в формате json;
# Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
# Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
# HOST: https://cloud-api.yandex.net:443
#
# Важно: Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!


import requests
import json
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token


    def upload(self, path_to_download_file: str):

        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {"path": ya_disk_file_path, "overwrite": "true"}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        # подготовка к загрузке файла
        response = requests.get(upload_url, headers=headers, params=params)
        json_resp = response.json()
        # получаем ссылку для загрузки файла
        href = json_resp.get('href')
        print("Ссылка для загрузки файла :",href)
        # загружаем файл
        resp = requests.put(url=href, data=open('test.txt', 'rb'))

if __name__ == '__main__':

    token = ''
    # откуда загружается  файл
    path_to_download_file = "C:/Users/Tanya/Documents/python_netologi/test.txt"
    # куда загружается файл
    ya_disk_file_path = "text_files/text27"
    # вызов загрузчика и загрузка файла
    uploader = YaUploader(token)
    result = uploader.upload(path_to_download_file)
