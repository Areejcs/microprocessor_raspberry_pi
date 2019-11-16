#READbutton
from gpiozero import LED, Button


myled = LED(17)
mybutton = Button(4)

mybutton.when_pressed= myled.on
mybutton.when_released=myled.off