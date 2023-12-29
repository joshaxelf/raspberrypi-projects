from machine import Pin
from neopixel import NeoPixel
import time

# Define LED PIN number 2 and number of LEDs attacthed to PIN

GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)

while True:
    
    # Blue LED flash twice
    
    for i in range(255):
        
        GRBled2.fill((0,0,i))
        GRBled2.write()
        time.sleep(0.001)
        
    GRBled2.fill((0,0,0))
    GRBled2.write()
    
    for i in range(255):
        
        GRBled2.fill((0,0,i))
        GRBled2.write()
        time.sleep(0.001)
        
    GRBled2.fill((0,0,0))
    GRBled2.write()
    
    # Red LED flash twice
        
    for i in reversed(range(255)):
        
        GRBled1.fill((0,i,0))
        GRBled1.write()
        time.sleep(0.001)
        
    GRBled1.fill((0,0,0))
    GRBled1.write()
        
    for i in reversed(range(255)):
        
        GRBled1.fill((0,i,0))
        GRBled1.write()
        time.sleep(0.001)
    

