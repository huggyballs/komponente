import Rpi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

buzzer=5
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
    GPIO.output(buzzer,GPIO.LOW)
    print("Gotovo!")
