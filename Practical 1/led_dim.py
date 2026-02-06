import RPi.GPIO as GPIO   # GPIO control library
import time              # Time delay library

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# GPIO pin connected to LED
LED_PIN = 18

# Set LED pin as OUTPUT
GPIO.setup(LED_PIN, GPIO.OUT)

# Create PWM object on LED pin with frequency 100Hz
pwm = GPIO.PWM(LED_PIN, 100)

# Start PWM with 0% duty cycle (LED OFF)
pwm.start(0)

try:
    # Gradually increase brightness
    for duty in range(0, 101, 5):
        pwm.ChangeDutyCycle(duty)
        print(f"Brightness: {duty}%")
        time.sleep(0.1)

    # Gradually decrease brightness
    for duty in range(100, -1, -5):
        pwm.ChangeDutyCycle(duty)
        print(f"Brightness: {duty}%")
        time.sleep(0.1)

# Stop execution safely on Ctrl+C
except KeyboardInterrupt:
    print("Program interrupted by user")

# Cleanup GPIO before exiting
finally:
    pwm.stop()
    GPIO.cleanup()
    print("GPIO cleanup completed")