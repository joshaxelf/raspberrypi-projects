from machine import Pin
from neopixel import NeoPixel
import time
import random

# Define LED PIN number 2 and number of LEDs attacthed to PIN

GRBled = NeoPixel(Pin(2), 1) # This LED is GRB not RGB

# Define bunch of colours with specific values to plug in

white = 240,140,255
red = 0,255,0
green = 255,0,0
blue = 0,0,255
yellow = 255,175,150
orange = 238, 223, 105
pink = 150,150,200
purple = 40,100,255
iceblue = 150,25,200
unicorn = 175,150,255
bogey = 215, 100, 0

# Define array

colours = [white, red, green, blue, yellow, orange, pink, purple, iceblue, unicorn, bogey]

# Randomly select a colour value from list and write it to LED

while True:
    
        randomColour = random.randint(0,10)
        new_colour = colours[randomColour]
        GRBled.fill(new_colour)
        GRBled.write()
        time.sleep(0.5)
    

