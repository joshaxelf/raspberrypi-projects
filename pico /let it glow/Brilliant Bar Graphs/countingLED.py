from machine import Pin
import time


# Set up the LEDs as segments

seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Set up buttons

greenButton = Pin(2, Pin.IN, Pin.PULL_DOWN)
redButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Create array of segments

segments = [seg1, seg2, seg3, seg4, seg5]

# Set count to -1, array starts at 0

count = -1

# Turn off all LEDs

for led in segments:
    led.value(0)

while True:
    
    time.sleep(0.2)
    
    if greenButton.value() == 1:
        
        if count == 4:
            print("Cannot add to counting LED")
            pass
        
        else:
            print("Green button pressed, adding one to counting LED...")
            count = count + 1
            segments[count].value(1)
            time.sleep(0.2)
       
    
    if redButton.value() == 1:
        
        if count == -1:
            print("Cannot remove from counting LED")
            pass
        
        else:
            print("Red button pressed, removing one from counting LED...")
            segments[count].value(0)
            count = count - 1
            time.sleep(0.2)
       
        
