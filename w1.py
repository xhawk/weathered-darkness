import redis
import time
import json
from ruuvitag_sensor.ruuvi import RuuviTagSensor

r = redis.Redis()

def handle_data(found_data):
    print('MAC ' + found_data[0])
    # print(found_data[1]["temperature"])
    found_data[1]["time"] = str(int(round(time.time())))
    weather_data = {found_data[0]: found_data[1]}
    r.lpush("wdata", json.dumps(weather_data))
    r.ltrim("wdata", 0, 9)

RuuviTagSensor.get_datas(handle_data)

