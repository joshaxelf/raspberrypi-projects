from machine import Pin
from neopixel import NeoPixel
import time

# Define LED PIN number 2 and number of LEDs attacthed to PIN

GRBled = NeoPixel(Pin(2), 1) # This LED is GRB not RGB

while True:
    
    # Increase Green value by 1 until 255
    
    for i in range(255):
        
        GRBled.fill((i,0,0))
        GRBled.write()
        time.sleep(0.008)
        
    # Decrease Green vlaue by 1 until 255
        
    for i in reversed (range(255)):
        
        GRBled.fill((i,0,0))
        GRBled.write()
        time.sleep(0.008)
        
     # Increase Red value by 1 until 255
    
    for i in range(255):
        
        GRBled.fill((0,i,0))
        GRBled.write()
        time.sleep(0.008)
        
    # Decrease Red vlaue by 1 until 255
        
    for i in reversed (range(255)):
        
        GRBled.fill((0,i,0))
        GRBled.write()
        time.sleep(0.008)

     # Increase Blue value by 1 until 255
    
    for i in range(255):
        
        GRBled.fill((0,0,i))
        GRBled.write()
        time.sleep(0.008)
        
    # Decrease Blue vlaue by 1 until 255
        
    for i in reversed (range(255)):
        
        GRBled.fill((0,0,i))
        GRBled.write()
        time.sleep(0.008)