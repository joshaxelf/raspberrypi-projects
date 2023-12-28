from machine import Pin
import time

# Set up the LEDs as segments

seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Create array of segments

segments = [seg1, seg2, seg3, seg4, seg5]

# Turn on all LEDs with 1 second delay

for led in segments:
    
    led.value(1)
    time.sleep(1)
    
# Turn off all LEDs at same time
    
for led in segments:
    led.value(0)