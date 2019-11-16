#musictest
import pygame
from time import sleep
from gpiozero import Button,LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


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

led1 = LED(4)
led2 = LED(27)
led3 = LED(23)

def playSound1():
    
       tone5.play()
       sleep(.2)
       led1.on()
       sleep(.4)
       led1.off()
       
btn1.when_pressed = playSound1

def playSound2():
        tone2.play()
        sleep(.2)
        led2.on()
        sleep(2)
        led2.off()
        
        #tone6.play()
btn2.when_pressed = playSound2

def playSound3():
        # tone3.play()
        tone7.play()
        sleep(.2)
        led3.on()
        sleep(2)
        led3.off()
        
btn3.when_pressed = playSound3


