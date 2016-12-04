import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

GPIO.setup("P9_11", GPIO.OUT)
GPIO.setup("P9_14", GPIO.OUT)
GPIO.setup("P9_12", GPIO.IN)

print("Program starting...")
GPIO.output("P9_14", GPIO.HIGH)

while (True):
    #print("PIR sensor is reading: ", GPIO.input("P9_12"))
    if (GPIO.input("P9_12")):
        GPIO.output("P9_11", GPIO.HIGH)
    else:
        GPIO.output("P9_11", GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()
