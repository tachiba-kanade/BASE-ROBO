from machine import Pin
from utime import sleep

pin = Pin(27, Pin.OUT) #output pin 27

print("starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
# 3 colors have single signal power - neo pixel lib - try showing a rainbow - use hsl color to rgb

