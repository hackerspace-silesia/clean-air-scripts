# clean-air-scripts

mainly copied from https://github.com/airmonitor/AirMonitorPlatform


# how run these scripts

## PYTHON

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

 ```
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
```

For more information about this API enter on:
https://powietrze.gios.gov.pl/pjp/content/api


Script  `luftaden.py` after run by:
```

python3 luftaden.py
```

return list of measurements from Poland.
Below is example schema:

```
[{'lat': '51.156',
  'long': '17.13',
  'pm10': '4.90',
  'pm25': '1.67',
  'sensor': 'SDS011'},
  (...)
  ]
  ```

For more information about this API enter on:
https://github.com/opendata-stuttgart/meta/wiki/APIs

## JAVA SCRIPT

#1 install libraries by

```
npm install
```


Script  `js/openaq.py` after run by:
```

node openaq.js
```

return data about

-BC\
-CO\
-NO2\
-O3\
-PM10\
-PM2.5\
-SO2\

```{ location: 'K-Koźle automat 1',
  parameter: 'pm25',
  date:
   { local: '2019-07-03T20:00:00+02:00',
     utc: '2019-07-03T18:00:00.000Z' },
  value: 3.84111,
  unit: 'µg/m³',
  coordinates: { latitude: 50.349608, longitude: 18.236575 },
  country: 'PL',
  city: 'Kędzierzyn-Koźle' }
```

##
You could find inspiration here:
https://www.youtube.com/watch?time_continue=75&v=GVBeY1jSG9Y

You could try to work on historical data, fot this you could use excels:

http://powietrze.gios.gov.pl/pjp/archives

You can also combine air information with other API:
https://dane.gov.pl/

