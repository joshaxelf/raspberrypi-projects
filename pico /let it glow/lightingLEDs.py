from machine import Pin
import time


## --- Turn on Diffuser Light and off with delay --- ##

print("Turning on Block Light...")

blockLED = Pin(14, Pin.OUT)
blockLED.value(1)
time.sleep(2)

print("Turning off Block Light...")
blockLED.value(0)

# Wait between functions

time.sleep(3)

## --- Turn on Diffuser and Onboard with delay --- ##

red = Pin(14, Pin.OUT) # Set red to Pin 14
green = Pin(25, Pin.OUT) # Set green to Pin 25

print("Turning on Green Light...")
green.value(1)
time.sleep(2)

print("Turning on Red Light...")
red.value(1)
time.sleep(2)

print("Turning off lights...")
red.value(0)
green.value(0)

# Wait between functions

time.sleep(3)

##  --- Flashing Diffuser and Onboard LED with Loop --- ##

loop_end = time.time() + 5 # Make variable equal to current time in seconds plus 5

print("Flashing Red Light for 5 seconds...") # Loop while current time is less than loop_end (i.e. do this for 5 seconds)

while time.time() < loop_end: 
    
    red.value(1)
    time.sleep(0.5)
    
    red.value(0)
    time.sleep(0.5)
    
# Wait between functions

time.sleep(3)

## --- Flashing Diffuser and Onboard LED with Range --- ##

# Use range to do this for 20 times

print("Flashing Red Light 10 times...")

for i in range(10):
    
    red.value(1)
    time.sleep(0.25)
    
    red.value(0)
    time.sleep(0.25)
    
print("Program Finished")