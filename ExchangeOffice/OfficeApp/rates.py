import requests
from datetime import date


def download_data(url):
    response = requests.get(url)
    with open(f'data/{date.today()}_rates.json', mode='wb') as file:
        file.write(response.content)


# download_data('https://belarusbank.by/api/kursExchange?city=%D0%9C%D0%B8%D0%BD%D1%81%D0%BA')


def retrive_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    # cont = content.split(',"GBP_in')[0][2:].split(':')
    # Осторожно! КОСТЫЛЬ!
    return content[2:112]


print(retrive_data('data/2021-12-02_rates.json'))
