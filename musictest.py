#musictest
import pygame
from time import sleep
from gpiozero import Button
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


GPIO.setup(4,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pygame.init()


tone1 = pygame.mixer.Sound("/home/pi/musicbox/samples/tone1.wav")
tone2 = pygame.mixer.Sound("/home/pi/musicbox/samples/tone2.wav")
tone3 = pygame.mixer.Sound("/home/pi/musicbox/samples/tone3.wav")
tone5 = pygame.mixer.Sound("/home/pi/musicbox/samples/tone5.wav")
tone6 = pygame.mixer.Sound("/home/pi/musicbox/samples/tone6.wav")
tone7 = pygame.mixer.Sound("/home/pi/musicbox/samples/tone7.wav")

btn1 = Button(17)
btn2 = Button(22)
btn3 = Button(24)

try:
    while True:
        GPIO.output(4, not GPIO.input(17))
        GPIO.output(27, not GPIO.input(22))
        GPIO.output(23, not GPIO.input(24))
    sleep(.1)
  

def playSound1():

       tone5.play()
btn1.when_pressed = playSound1


def playSound2():
        tone2.play()

btn2.when_pressed = playSound2

def playSound3():
        # tone3.play()
        tone7.play()

btn3.when_pressed = playSound3

finally:
    GPIO.output(4, False)
    GPIO.output(27, False)
    GPIO.output(23, False)
    GPIO.cleanup()
    
