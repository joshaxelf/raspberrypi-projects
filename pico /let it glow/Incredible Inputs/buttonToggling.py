from machine import Pin
import time
        
## --- Introducing Toggle Function --- ##

greenButton = Pin(2, Pin.IN, Pin.PULL_DOWN)
redButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

redLED = Pin(14, Pin.OUT)
greenLED = Pin(25, Pin.OUT)


while True:
    
    time.sleep(0.2)
    
    if redButton.value() == 1:
        redLED.toggle()
        
    if greenButton.value() == 1:
        greenLED.toggle()
        
