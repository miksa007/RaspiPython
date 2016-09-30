# Miksa 30.09.2016
# schema: GND - resistor - led - GPIO25

from gpiozero import LED
from time import sleep

led=LED(25)
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
