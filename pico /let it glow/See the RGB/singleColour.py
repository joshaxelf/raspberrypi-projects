from machine import Pin
from neopixel import NeoPixel
import time

# Define LED PIN number 2 and number of LEDs attacthed to PIN

GRBled = NeoPixel(Pin(2), 1) # This LED is GRB not RGB

# Fill variable name with colour values

GRBled.fill((255,0,0))

# Write to LED

GRBled.write()