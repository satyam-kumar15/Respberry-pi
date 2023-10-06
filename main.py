import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin number
led_pin = 17

# Setup the pin as an output
GPIO.setup(led_pin, GPIO.OUT)

# Blink the LED
try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)  # Turn on the LED
        time.sleep(1)                   # Wait for 1 second
        GPIO.output(led_pin, GPIO.LOW)   # Turn off the LED
        time.sleep(1)                   # Wait for 1 second

except KeyboardInterrupt:
    # Clean up GPIO settings when the program is interrupted
    GPIO.cleanup()
