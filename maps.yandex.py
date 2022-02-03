import httpx


api_key = ''
address = 'г. Москва, Пролетарский пр-кт, д. 30'

params = {
    'apikey': api_key,
    'geocode': address,
    'format': 'json'
}

res = httpx.get(f'https://geocode-maps.yandex.ru/1.x/?', params=params)
