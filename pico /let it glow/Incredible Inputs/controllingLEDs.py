from machine import Pin
import time
        
## --- Buttons correspond with coloured LED --- ##
        
redLED = Pin(14, Pin.OUT)
greenLED = Pin(25, Pin.OUT)

while True:
    
    time.sleep(0.2)
    
    if redButton.value() == 1:
        print("Red button pressed, turning on Red LED...")
        redLED.value(1)
        time.sleep(5) # Keep LED on for 5 seconds, then turn off
        redLED.value(0)
        
    if greenButton.value() == 1:
        print("Green button pressed, turning on Green LED...")
        greenLED.value(1)
        time.sleep(5) # Keep LED on for 5 seconds, then turn off
        greenLED.value(0)