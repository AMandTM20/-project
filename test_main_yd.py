import requests
import pytest

url = "https://disk.yandex.ru/client/disk"
ya_token = 'y0_AgAAAABpvdOYAADLWwAAAADgJE7sOB1Wg3aCRFutbwgE1rhfqQVMp9k'
expected_result = '<Response [200]>'
class TestSomething:
    def test_create_folder(self):

        result = str(requests.get(url))
        assert result == expected_result

    @pytest.mark.xfail # Тестирование от обратного
    def test_create_folder_mistake(self):

        result = requests.get(url)
        assert result == expected_result