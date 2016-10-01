#miksa 1.10.2016
#schema GND - LED - GPIO25
#GND - Button - GPIO21
from gpiozero import Button
from gpiozero import LED
from time import sleep
led=LED(25)
button =Button(21)
led.on()
while True:
    sleep(1)
    if button.is_pressed:
        print("Button is pressed")
        led.off()
    else:
        print("Button ei o painettu")
        led.on()
