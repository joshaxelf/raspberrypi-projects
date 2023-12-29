from machine import Pin
from neopixel import NeoPixel
import time

# Define LED PIN number 2 and number of LEDs attacthed to PIN

GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)

while True:
    
    # Fade in first LED (left)
    
    for i in range(255):
        
        GRBled2.fill((i,0,0))
        GRBled2.write()
        time.sleep(0.008)
        
    GRBled2.fill((0,0,0))
    GRBled2.write()
    
    # "Jump" to second LED (right) and fade out
        
    for i in reversed(range(255)):
        
        GRBled1.fill((i,0,0))
        GRBled1.write()
        time.sleep(0.008)
    
