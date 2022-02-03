import json

import httpx

from settings import YANDEX_MAPS_API_KEY


class Maps:
    def __init__(self, api_key: str, addresses: list):
        self.api_key = api_key
        self.addresses = addresses
        self.coordinates = []
        self.base_url = 'https://geocode-maps.yandex.ru/1.x/'

        for address in self.addresses:
            coordinate = self.get_coordinates(address)
            self.coordinates.append(coordinate)

        self.write_to_file('./data/coordinates.json')

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.coordinates, file, ensure_ascii=False, indent=4)

    def get_coordinates(self, address):
        params = {
            'apikey': self.api_key,
            'geocode': address,
            'format': 'json'
        }

        response = httpx.get(self.base_url, params=params)

        if response.status_code == 200:
            try:
                json_data = response.json()
                count = json_data['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData'][
                    'found']

                if count == '0':
                    name = json_data['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData'][
                        'request']
                    coord = None
                else:
                    coord = json_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                    name = json_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'][
                        'metaDataProperty']['GeocoderMetaData']['text']
                return {'name': name, 'coordinates': coord, 'processed': False}
            except Exception as e:
                print(e)
        else:
            print('!!!', response.text)
            return None

    def get_address(self, coordinates):
        url = f'https://geocode-maps.yandex.ru/1.x/?apikey={self.api_key}&format=json&geocode={coordinates}'
        response = httpx.get(url)

        if response.status_code == 200:
            return response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
        else:
            return None

    def get_distance(self, coordinates1, coordinates2):
        url = f'https://geocode-maps.yandex.ru/1.x/?apikey={self.api_key}&format=json&geocode={coordinates1}&rspn=1&results=1&ll={coordinates2}'
        response = httpx.get(url)

        if response.status_code == 200:
            return response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Distance']
        else:
            return None

    def get_distance_in_km(self, coordinates1, coordinates2):
        distance = self.get_distance(coordinates1, coordinates2)
        if distance:
            return float(distance['value']) / 1000
        else:
            return None


with open('./data/offices.txt', 'r') as f:
    addresses = [line.strip() for line in f.readlines()]

maps = Maps(YANDEX_MAPS_API_KEY, addresses)

