# Imports
from machine import Pin
import time
import random

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button1 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button1 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

red.value(0)
amber.value(0)
green.value(0)

# countdown var
cd = 5

# reaction time var
react = 0

# countdown timer
while cd > 0:
    # print time until challenge start
    print(cd)
    cd = cd - 1
    time.sleep(1)

# when countdown has finished 
if cd == 0:
    # sleep for randomly generated amount of time 
    timerd = random.randint(0, 10)
    time.sleep(timerd)
    
    # turn on led
    red.value(1)
    
    # calculate time for button to be pressed
    while button1.value() != 1:
        react = react + 1
        time.sleep(0.001)
        print(react)
    
    print("Reaction time: ",react,"ms")