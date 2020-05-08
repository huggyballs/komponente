import Rpi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

buzzer=29
GPIO.setup(buzzer,GPIO.OUT)

try:

    while True:
        GPIO.output(buzzer,GPIO.HIGH)
        print("BIIIIP")
        sleep(0.5)
        GPIO.output(buzzer,GPIO.LOW)
        print("NEMA BIIIIP")
        sleep(0.5)

except KeyboardInterrupt:
    print("Gotovo!")
