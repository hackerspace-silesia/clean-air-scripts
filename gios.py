# coding=utf-8

import json
import os
import urllib
from urllib.request import Request
from collections import defaultdict
from time import time

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
URL = 'http://api.gios.gov.pl/pjp-api/rest/'


def all_data():
    url = URL + "station/findAll"

    if url.lower().startswith('http'):
        gios = Request(url)
    else:
        raise ValueError from None

    with urllib.request.urlopen(gios, timeout=60) as resp:
        gios_all_stations = json.loads(resp.read())

    return gios_all_stations


class ParseError(Exception):

    def __init__(self, *args, sensor_type):
        self.sensor_type = sensor_type
        super().__init__(*args)


def _get_data_from_gios_station(sensor_index, gios_sensor_data):
    sensor_type = gios_sensor_data['param']['paramFormula']
    if sensor_type not in {'PM10', 'PM2.5'}:
        return None

    sensor_id = gios_sensor_data['id']
    station_id_data = Request(URL + f"/data/getData/{sensor_id}")
    station_id = gios_sensor_data['stationId']
    station_sensor_data = urllib.request.urlopen(station_id_data, timeout=60)
    station_sensor_data = json.loads(station_sensor_data.read())

    try:
        first_sensor = next(
            val for val in station_sensor_data['values']
            if val['value'] is not None
        )
    except StopIteration:
        raise ParseError(
            f'empty not-none values, i={sensor_index}, station_id={station_id}', 
            sensor_type=sensor_type,
        )

    try:
        value = first_sensor['value']
        value = float(value)
    except TypeError:
        raise ParseError(
            f'wrong value={value}, i={sensor_index}, station_id={station_id}', 
            sensor_type=sensor_type,
        )

    return sensor_type, value


def gios():
    t_global = time()
    errors_counter = defaultdict(int)
    values = []

    gios_all_stations = all_data()

    total_values = len(gios_all_stations)
    for i, obj in enumerate(gios_all_stations):
        t = time()
        print(i, '/', total_values, '...', end='')
        result_id = obj['id']
        sensor_url = Request(URL + f'station/sensors/{result_id}')
        gios_sensor_data = urllib.request.urlopen(sensor_url, timeout=60)
        gios_sensor_data = json.loads(gios_sensor_data.read())

        for sensor_index, gios_sensor_single_data in enumerate(gios_sensor_data):
            try:
                useful_data = _get_data_from_gios_station(
                    sensor_index=sensor_index,
                    gios_sensor_data=gios_sensor_single_data,
                )
            except ParseError as error:
                errors_counter[error.sensor_type] += 1
                print('!!!', error)
                continue

            if useful_data is None:
                continue
            sensor_type, value = useful_data
            values.append({
                'sensor_type': sensor_type,
                'sensor': 'WIOS',
                'value': value,
                'id': obj['id'],
                'lat': obj['gegrLat'],
                'lon': obj['gegrLon'],
            })

        print(' time: %.2fs' % (time() - t))

    counter_by_sensor = defaultdict(int)
    for obj in values:
        counter_by_sensor[obj['sensor_type']] += 1

    print('errors', errors_counter)
    print('count by sensor type', counter_by_sensor)
    print('total time: %.2fs' % (time() - t))
    return values

if __name__ == "__main__":
    from pprint import pprint
    pprint(gios())
