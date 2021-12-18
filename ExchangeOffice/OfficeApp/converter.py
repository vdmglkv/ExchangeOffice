import requests


def get_data():
    response = requests.get('https://v6.exchangerate-api.com/v6/59f1498aca069edffc74243d/latest/BYN')
    return response.json()['conversion_rates']


def get_pair_rates(from_, to):
    response = requests.get(f'https://v6.exchangerate-api.com/v6/59f1498aca069edffc74243d/pair/{from_}/{to}')
    return response.json()['conversion_rate']

