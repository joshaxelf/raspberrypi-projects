from machine import Pin
import time

## --- Setting up button allocation --- ##

# Set variable with GPIO pin number and set as input and use pull down

redButton = Pin(3, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(2, Pin.IN, Pin.PULL_DOWN)

while True: # Loop forever
    
    time.sleep(0.2) # Needed for finger press
    
    if redButton.value() == 1:
        print("Red Button pressed...")
        
    if greenButton.value() == 1:
        print("Green Button pressed...")