import machine
import time

# Set the pin numbers for the two LEDs
led1_pin = 5
led2_pin = 4

# Initialize the GPIO pins for the LEDs
led1 = machine.Pin(led1_pin, machine.Pin.OUT)
led2 = machine.Pin(led2_pin, machine.Pin.OUT)

# Turn off both LEDs initially
led1.off()
led2.off()

# Loop forever
while True:
    # Check the state of LED 1
    if led1.value():
        # If LED 1 is on, turn off LED 2
        led2.off()
    else:
        # If LED 1 is off, turn on LED 2
        led2.on()
    # Check the state of LED 2
    if led2.value():
        # If LED 2 is on, turn off LED 1
        led1.off()
    else:
        # If LED 2 is off, turn on LED 1
        led1.on()
    # Wait for a short time before looping again
    time.sleep(0.1)
