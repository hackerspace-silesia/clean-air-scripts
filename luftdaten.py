import json
import os
import urllib
from urllib.request import Request

import requests
from requests.adapters import HTTPAdapter
import urllib3
from urllib3.util import Retry
from logging import getLogger
from sys import stderr

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_all_data():
    url = "http://api.luftdaten.info/v1/filter/country=PL"

    if url.lower().startswith("http"):
        luftdaten = Request(url)
    else:
        raise ValueError from None

    with urllib.request.urlopen(luftdaten, timeout=60) as resp:
        luftdaten_all_stations = json.loads(resp.read())

    for data in luftdaten_all_stations:
        yield data


def to_float(x):
    try:
        return float(x)
    except ValueError:
        return None


def _get_fancy_data_from_single_luftdaten(data):
    sensor_name = data["sensor"]["sensor_type"]["name"]
    if sensor_name != "SDS011":
        return None

    sensor_values = {
        sensor_data['value_type']: to_float(sensor_data.get('value'))
        for sensor_data in data["sensordatavalues"]
    }

    sensor_lat = float(data["location"]["latitude"])
    sensor_long = float(data["location"]["longitude"])
    return {
        "lat": sensor_lat,
        "long": sensor_long,
        "pm25": sensor_values.get('P2'),
        "pm10": sensor_values.get('P1'),
        "sensor": sensor_name,
    }


def luftdaten():
    try:
        luftdaten_all_data = get_all_data()
    except urllib.error.HTTPError as e:
        print("luftdaten returned %s" % e, file=stderr)

    parsed_data = (
        _get_fancy_data_from_single_luftdaten(data)
        for data in luftdaten_all_data
    )

    filtered_data = [data for data in parsed_data if data]
    return filtered_data


if __name__ == "__main__":
    from pprint import pprint
    pprint(luftdaten())
