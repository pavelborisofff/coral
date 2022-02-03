import json
import time

from dadata import Dadata


def get_from_dadata(address):
    token = '23b745d44057a81028a784469002b25449c35fd8'
    secret = '63a93c725705dc772721adb16bfd43cef5fa187b'
    dadata = Dadata(token, secret)
    _result = dadata.clean('address', address)

    return _result


with open('./data/offices.txt', 'r') as f:
    offices = [line.strip() for line in f.readlines()]

data = []

with open('./data/offices_geotag.json', 'w') as f:
    for office in offices:
        print(office)
        res = get_from_dadata(office)
        print(res)
        data.append(res)
        time.sleep(1)

json_data = json.dumps(data, indent=4, ensure_ascii=False)


