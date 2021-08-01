from multiprocessing import Process
import sys
import os
import RPi.GPIO as GPIO
import time
import datetime
from picamera import PiCamera
from temp import process_temp
from fan import fan
from status import Status

if os.geteuid() != 0:
    sys.exit("This script needs to be run as root")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN = 1
GPIO.setup(PIR_PIN, GPIO.IN)


# record the temp every 60 minutes
Process(target=process_temp, name="process temp").start()

camera = PiCamera()
Status.instance()

while True:
    if GPIO.input(PIR_PIN):
        now = datetime.datetime.now().isoformat()
        print(now + ": motion detected")
        print("current temp = " + str(status.current_temp)

        camera.start_preview()
        time.sleep(1)
        camera.capture('/home/pi/Programs/Temperature/images/dog_house_' + now + '.jpg')
        camera.stop_preview()

        fan("on")
        time.sleep(30 * 60)
        fan("off")
