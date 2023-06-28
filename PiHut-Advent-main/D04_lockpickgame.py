#Imports
from machine import ADC, Pin, PWM
import time
import random
# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# Set up the LED pin with PWM
red = PWM(Pin(18))
amber = PWM(Pin(19))
green = PWM(Pin(20))
red.freq(1000)
amber.freq(1000)
green.freq(1000)

# sets time for correct answer to zero
rcount = 0
acount = 0
gcount = 0

# Create a variable for potentiometer reading
reading = 0

########################################################################################################

# creates a random number between 0 and 65535
potran = random.randint(0, 65535)

# devides potran number by 1000 and rounds to closest int
potrandv = round(potran/1000, 0)

# time delay so lock isnt instantly picked
while gcount < 10:

    # short delay
    time.sleep(0.1)
    
    # sets var reading to potentiometer value
    reading = potentiometer.read_u16()
    
    # devides reading by 1000 and rounds to closest int
    readingdv = round(reading/1000, 0)
    
    # if potentiometer input is equal to random number
    if readingdv == potrandv:
        
        # turn on green led
        red.duty_u16(0)
        amber.duty_u16(0)
        green.duty_u16(65535)
        
        # adds 1 to gcount
        gcount = gcount + 1
        
    # if potentiometer input is not equal to random number    
    elif readingdv != potrandv:
        
        #turns off all leds
        red.duty_u16(0)
        amber.duty_u16(0)
        green.duty_u16(0)

# prints when lock is picked
if gcount == 10:
    print("green lock picked")
    
########################################################################################################
    
potran = random.randint(0, 65535)

potrandv = round(potran/1000, 0) 

while acount < 10:

    time.sleep(0.1)
    
    reading = potentiometer.read_u16()
    
    readingdv = round(reading/1000, 0)
    
    if readingdv == potrandv:
        
        red.duty_u16(0)
        amber.duty_u16(65535)
        green.duty_u16(65535)
        acount = acount + 1
        
    elif readingdv != potrandv:
        
        red.duty_u16(0)
        amber.duty_u16(0)
        green.duty_u16(65535)
        
if acount == 10:
    print("amber lock picked")
    
########################################################################################################
    
potran = random.randint(0, 65535)

potrandv = round(potran/1000, 0) 

while rcount < 10:

    time.sleep(0.1)
    
    reading = potentiometer.read_u16()
    
    readingdv = round(reading/1000, 0)
    
    if readingdv == potrandv:
        
        red.duty_u16(65535)
        amber.duty_u16(65535)
        green.duty_u16(65535)
        rcount = rcount + 1
        
    elif readingdv != potrandv:

        red.duty_u16(0)
        amber.duty_u16(65535)
        green.duty_u16(65535)
        
if rcount == 10:
    print("red lock picked")
