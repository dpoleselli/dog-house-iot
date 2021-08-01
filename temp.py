import Adafruit_DHT
import time
import datetime
import gspread
from requests import get
from status import Status

status = Status()

def get_temp():
    sensor = Adafruit_DHT.DHT11
    gpio = 4

    humidity, temp_c = Adafruit_DHT.read_retry(sensor, gpio)
    temp_f = temp_c * 9.0 / 5.0 + 32.0

    status.current_temp = temp_f

    return humidity, temp_c, temp_f

def process_temp(interval=60):
    ip = get('https://api.ipify.org').text
    latlong = get('https://ipapi.co/{}/latlong/'.format(ip)).text.split(',')
    WEATHER_KEY = os.env.get("OPEN_WEATHER_API")

    gc = gspread.service_account(filename='./service_account.json')

    sh = gc.open("Dog House Temp")

    while True:
         humidity, temp_c, temp_f = get_temp()
         weather = get('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=imperial&appid={}'.format(latlong[0], latlong[1], WEATHER_KEY)).json()

         now = datetime.datetime.now().isoformat()
         fan = "On" if status.fan_on else "Off"
         data = [now, humidity, weather["main"]["humidity"], temp_f, weather["main"]["temp"], fan]
         sh.sheet1.append_row(data)
         print("sending data: " + str(data))

         time.sleep(60 * interval)

if __name__ == "__main__":
    process_temp()
