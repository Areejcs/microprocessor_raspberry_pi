#READbutton
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        GPIO.output(17, not GPIO.input(4))
    sleep(.1)
finally:
    GPIO.output(17, False)
    GPIO.cleanup()
    
