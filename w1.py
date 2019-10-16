import redis
import time
import json
from ruuvitag_sensor.ruuvi import RuuviTagSensor

r = redis.Redis()

def handle_data(found_data):
    print('MAC ' + found_data[0])
    # print(found_data[1]["temperature"])
    weather_data = {str(round(time.time())): found_data[1]}
    r.rpush("wdata", json.dumps(weather_data))

RuuviTagSensor.get_datas(handle_data)

