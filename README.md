# clean-air-scripts

mainly copied from https://github.com/airmonitor/AirMonitorPlatform


# how run these scripts

#1 install libraries from requirements.txt

```
pip3 install -r requirements.txt

```

#2 run needed script

Script `gios.py` after run by:
```
python gios.py

```

return list of measurements from Poland
Below is example schema:

 {'id': 225,
  'lat': '52.658467',
  'lon': '19.059314',
  'sensor': 'WIOS',
  'sensor_type': 'PM2.5',
  'value': 4.4},
 {'id': 9791,
  'lat': '52.637394',
  'lon': '19.044486',
  'sensor': 'WIOS',
  'sensor_type': 'PM10',}
  (...)
]

For more information about this API enter on:
https://powietrze.gios.gov.pl/pjp/content/api


Script  `luftaden.py` after run by:
```

python3 luftaden.py
```

return list of measurements from Poland.
Below is example schema:

[{'lat': '51.156',
  'long': '17.13',
  'pm10': '4.90',
  'pm25': '1.67',
  'sensor': 'SDS011'},
  (...)
  ]

For more information about this API enter on:
https://github.com/opendata-stuttgart/meta/wiki/APIs

You could find inspiration here:
https://www.youtube.com/watch?time_continue=75&v=GVBeY1jSG9Y

You could try to work on historical data, you could use excels:

http://powietrze.gios.gov.pl/pjp/archives

You can also combine air information with other data:
https://dane.gov.pl/

