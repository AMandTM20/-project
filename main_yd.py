import requests
import yadisk

def create_folder():
    yd = yadisk.YaDisk(token="y0_AgAAAABpvdOYAADLWwAAAADgJE7sOB1Wg3aCRFutbwgE1rhfqQVMp9k")
    url = "https://disk.yandex.ru/client/disk"
    resp = requests.get(url)
    if not yd.is_dir("/New"):
        yd.mkdir("/New")
        print('Папка "New" только что создана')
    else:
        print(' Папка "New" уже есть на диске ')
    return resp

f = create_folder()
print(f)