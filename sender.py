import json

import requests as requests
BASE_URL = 'http://127.0.0.1:8000/'

# получение датчиков
def get_sensors():
    response = requests.get(BASE_URL + 'api/sensors/', headers = {'Content-Type': 'application/json'})
    print(response.json())


def POST_sensors():
    payload = {'id': 4, 'title': 'Четвертый датчик', 'description': 'Четвертый датчик'}
    response = requests.post(BASE_URL+'api/sensors/',
                             headers={'Content-Type': 'application/json'},
                             json=payload)
    print(response.json())

def get_sensor():
    response = requests.get(BASE_URL + 'api/sensors/3', headers = {'Content-Type': 'application/json'})
    print(response.json())

def patch_sensor():
    payload = {'description': 'Третий датчик ещё раз изменён'}
    response = requests.patch(BASE_URL+'api/sensors/3',
                              headers={'Content-Type': 'application/json'},
                              json=payload)
    print(response.json())


def POST_measurements():
    payload = {  "sensorID": 3,
                 "temperature": 22.3}
    response = requests.post(BASE_URL+'api/measurements/',
                             headers={'Content-Type': 'application/json'},
                             json=payload)
    print(response.json())


if __name__ == '__main__':
    patch_sensor()
