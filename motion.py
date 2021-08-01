import RPi.GPIO as GPIO
import time
from manager import Manager

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN = 1
GPIO.setup(PIR_PIN, GPIO.IN)

print('Starting up the PIR Module (click on STOP to exit)')
time.sleep(1)
print ('Ready')
manager = Manager()
print (1)
print (manager.var)
print (2)
while True:
  if GPIO.input(PIR_PIN):
    print('Motion Detected')
  time.sleep(5)
