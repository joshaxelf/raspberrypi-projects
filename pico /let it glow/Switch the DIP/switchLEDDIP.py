from machine import Pin
import time

# Set up the DIP (Dual Inline Package)

dip1 = Pin(6, Pin.IN, Pin.PULL_DOWN)
dip2 = Pin(5, Pin.IN, Pin.PULL_DOWN)
dip3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
dip4 = Pin(3, Pin.IN, Pin.PULL_DOWN)
dip5 = Pin(2, Pin.IN, Pin.PULL_DOWN)

# Set up the LEDs as segments

seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Turn on LED with switches

while True:
    
    if dip1() == 1:
        seg1.value(1)
    else:
        seg1.value(0)
        
    if dip2() == 1:
        seg2.value(1)
    else:
        seg2.value(0)
        
    if dip3() == 1:
        seg3.value(1)
    else:
        seg3.value(0)
        
    if dip4() == 1:
        seg4.value(1)
    else:
        seg4.value(0)

    if dip5() == 1:
        seg5.value(1)
    else:
        seg5.value(0)