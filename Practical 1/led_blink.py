# Import GPIO library to control Raspberry Pi GPIO pins
import RPi.GPIO as GPIO

# Import time library to create delays
import time

# Set GPIO numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pin number where LED is connected
LED_PIN = 18

# Set LED pin as OUTPUT
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    # Infinite loop to blink LED continuously
    while True:
        # Turn LED ON
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)  # Wait for 1 second

        # Turn LED OFF
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)  # Wait for 1 second

# Stop program safely when Ctrl + C is pressed
except KeyboardInterrupt:
    print("Program interrupted by user")

# Cleanup GPIO pins before exiting
finally:
    GPIO.cleanup()
    print("GPIO cleanup completed")