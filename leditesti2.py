#miksa 30.9.2016
#schema GND - resistor - led -GPIO25
#GND - resistor - led -GPIO8
#GND - resistor - led -GPIO7   

from gpiozero import LED
from time import sleep
red = LED(25)
amber = LED(8)
green = LED(7)

green.on()
amber.on()
red.on()
i=10
while i>0: 
    sleep(1)
    red.on()
    green.off()
    amber.off()

    sleep(1)
    red.off()
    amber.on()

    sleep(1)
    green.on()
    amber.off()

    i=i-1
