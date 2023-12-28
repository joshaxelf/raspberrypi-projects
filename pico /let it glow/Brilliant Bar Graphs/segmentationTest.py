from machine import Pin
import time

## --- Segment Test --- ##

# Set up the LEDs as segments

seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Turn on each LED with delay of 1 second

seg1.value(1)
time.sleep(1)

seg2.value(1)
time.sleep(1)

seg3.value(1)
time.sleep(1)

seg4.value(1)
time.sleep(1)

seg5.value(1)
time.sleep(1)

# Turn off all the LEDs

seg1.value(0)
seg2.value(0)
seg3.value(0)
seg4.value(0)
seg5.value(0)
