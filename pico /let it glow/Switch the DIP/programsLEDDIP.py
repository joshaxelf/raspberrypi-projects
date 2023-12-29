from machine import Pin
import time
import random

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

# Put into array

segments = [seg1, seg2, seg3, seg4, seg5]

# Define new functions used in each switch

def program1():
    
    for led in segments:
        led.value(1)
        time.sleep(0.1)
        led.value(0)
        
def program2():
    
    for led in reversed (segments):
        led.value(1)
        time.sleep(0.1)
        led.value(0)
        
def program3():

    randomLED = random.randint(0,4)
    segments[randomLED].value(1)
    time.sleep(0.1)
    segments[randomLED].value(0)
    
def caraFirstProgram():

    seg3.value(1)
    time.sleep(0.5)
    seg3.value(0)
    seg1.value(1)
    time.sleep(0.5)
    seg1.value(0)
    seg5.value(1)
    time.sleep(0.5)
    seg5.value(0)
    seg4.value(1)
    time.sleep(0.5)
    seg4.value(0)
    seg2.value(1)
    time.sleep(0.5)
    seg2.value(0)
    
    for led in segments:
        led.value(1)
        time.sleep(0.2)
    
    for led in reversed (segments):
        led.value(0)
        time.sleep(0.2)
        

# Else If to run only one program        

while True:
    
    if dip1() == 1:
        program1()
        
    elif dip2() == 1:
        program2()
        
    elif dip3() == 1 and dip4() == 1:
        program3()
        
    elif dip5() == 1:
        caraFirstProgram()