from machine import Pin
import time



print ("Hello World!")

print (1 + 2)

# Minus is -
# Multiply is *
# Divide is /
# Addition is +

onboardLED = Pin(25, Pin.OUT)
onboardLED.value(1)

print("Turning Light On...")

print("Waiting 5 seconds...")

time.sleep(5)

onboardLED.value(0)

print("Turning Light Off...")