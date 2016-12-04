import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM


GPIO.setup("P9_14", GPIO.OUT) # red led
GPIO.setup("P9_16", GPIO.OUT) # green led
GPIO.setup("P9_22", GPIO.OUT) # blue led

GPIO.setup("P9_11", GPIO.OUT) # test led
GPIO.setup("P9_12", GPIO.IN) # pir sensor

GPIO.setup("P8_10", GPIO.OUT) # green led
GPIO.setup("P8_12", GPIO.OUT) # red led


print(bin(GPIO.input("P9_12"))) # digital input print out for pir sensor


GPIO.output("P9_11", GPIO.HIGH) # test led

GPIO.output("P9_14", GPIO.HIGH)
GPIO.output("P9_16", GPIO.HIGH)
GPIO.output("P9_22", GPIO.HIGH)

GPIO.output("P8_10", GPIO.HIGH)
GPIO.output("P8_12", GPIO.HIGH)


input = raw_input("Type something")


GPIO.cleanup()


