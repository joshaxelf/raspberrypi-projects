from machine import Pin
import time
import random

# Set up the LEDs as segments

seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Create array of segments

segments = [seg1, seg2, seg3, seg4, seg5]

while True:
    
        randomLED = random.randint(0,4) # Random integer from 0-4 for 5 LEDs
        
        segments[randomLED].value(1)
        
        time.sleep(0.2)
        
        segments[randomLED].value(0)