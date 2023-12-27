from machine import Pin
import time
        
## --- Counting with Buttons and Lights --- ##

greenButton = Pin(2, Pin.IN, Pin.PULL_DOWN)
redButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

redLED = Pin(14, Pin.OUT)
greenLED = Pin(25, Pin.OUT)

# Start count at 0

count = 0

while True:

    time.sleep(0.2)
    
    redLED.value(0)
    greenLED.value(0)
    
    if redButton.value() == 1:
        count = count - 1
        redLED.value(1)
        print(count)
        
    if greenButton.value() == 1:
        count = count + 1
        greenLED.value(1)
        print(count)